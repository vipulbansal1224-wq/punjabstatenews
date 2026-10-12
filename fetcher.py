"""
PunjabState News - Automated City-Wise News Fetcher Engine
Fetches real-time hyper-local news for all 23 districts of Punjab,
parses RSS feeds, runs content enhancement, deduplicates, and saves to database.
"""
import feedparser
import urllib.parse
from datetime import datetime
import time
from config import PUNJAB_DISTRICTS, GOOGLE_NEWS_RSS_URL, MAX_ITEMS_PER_CITY, CATEGORY_IMAGES
from database import article_exists, insert_article
from rewriter import rewrite_article
from image_processor import process_article_real_image

BREAKING_KEYWORDS = [
    "breaking", "killed", "dead", "arrested", "encounter", "blast", "fire", "accident",
    "scam", "protest", "dharna", "strike", "emergency", "alert", "warning", "high court"
]

def parse_published_date(entry):
    if hasattr(entry, 'published_parsed') and entry.published_parsed:
        try:
            return time.strftime('%Y-%m-%d %H:%M:%S', entry.published_parsed)
        except:
            pass
    return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

def is_breaking_story(title):
    t_lower = title.lower()
    return any(bk in t_lower for bk in BREAKING_KEYWORDS)

def fetch_news_for_city(city_info, max_items=MAX_ITEMS_PER_CITY):
    """
    Fetches real-time news for a specific Punjab district
    """
    query = city_info.get("query", f"{city_info['name']} Punjab news")
    encoded_query = urllib.parse.quote(query)
    feed_url = GOOGLE_NEWS_RSS_URL.format(query=encoded_query)

    new_articles = []
    try:
        feed = feedparser.parse(feed_url)
        if not feed.entries:
            return []

        for entry in feed.entries[:max_items]:
            raw_title = getattr(entry, 'title', '').strip()
            source_url = getattr(entry, 'link', '').strip()
            raw_summary = getattr(entry, 'summary', '').strip()
            source_name = "PunjabState Desk"

            if not raw_title or not source_url:
                continue

            # Deduplication Check
            if article_exists(source_url, raw_title):
                continue

            # Process & Rewrite Content
            enhanced = rewrite_article(raw_title, raw_summary, city_info, source_name)

            # Assign Real Converted News Image
            category = enhanced['category']
            fallback_img = city_info.get('image') or CATEGORY_IMAGES.get(category) or CATEGORY_IMAGES['general']
            image_url = process_article_real_image(source_url, fallback_img)

            # Check Breaking & Featured
            is_breaking = 1 if is_breaking_story(raw_title) else 0
            is_featured = 1 if len(new_articles) == 0 else 0
            published_at = parse_published_date(entry)

            # Insert into database
            art_id = insert_article(
                title=enhanced['title'],
                original_title=enhanced['original_title'],
                summary=enhanced['summary'],
                highlights=enhanced['highlights'],
                content=enhanced['content'],
                city=enhanced['city'],
                city_name=enhanced['city_name'],
                category=enhanced['category'],
                source_name=source_name,
                source_url=source_url,
                image_url=image_url,
                published_at=published_at,
                is_breaking=is_breaking,
                is_featured=is_featured
            )

            if art_id:
                new_articles.append({
                    "id": art_id,
                    "title": enhanced['title'],
                    "city": enhanced['city_name']
                })

    except Exception as e:
        print(f"Error fetching news for {city_info['name']}: {e}")

    return new_articles

def fetch_all_punjab_news(max_items_per_city=3):
    """
    Main job that sweeps all 23 districts of Punjab
    """
    total_added = 0
    start_time = time.time()
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting PunjabState News automated sweep across 23 districts...")

    for city in PUNJAB_DISTRICTS:
        added = fetch_news_for_city(city, max_items=max_items_per_city)
        if added:
            total_added += len(added)
            print(f"  [+] {city['name']}: +{len(added)} new stories")
        # Gentle pacing between requests
        time.sleep(0.3)

    elapsed = round(time.time() - start_time, 2)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Sweep completed in {elapsed}s. Total new articles: {total_added}")
    return total_added

if __name__ == "__main__":
    from database import init_db
    init_db()
    fetch_all_punjab_news(max_items_per_city=2)
