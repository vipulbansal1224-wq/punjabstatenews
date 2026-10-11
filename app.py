"""
PunjabState News - Main Flask Web Application
"""
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import os
from config import (
    SITE_NAME, SITE_TAGLINE, SITE_DESCRIPTION,
    PUNJAB_DISTRICTS, CATEGORIES, BASE_DIR
)
from database import (
    init_db, get_recent_articles, get_articles_by_city,
    get_articles_by_category, get_breaking_news, get_featured_news,
    get_article_by_slug, increment_views, search_articles,
    get_related_articles, get_city_counts, get_total_stats,
    get_active_ads, update_ad_slot, insert_article, delete_article
)
from scheduler import start_background_scheduler, trigger_manual_fetch_async, get_scheduler_status

app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, 'templates'),
            static_folder=os.path.join(BASE_DIR, 'static'))
app.secret_key = "punjabstate_super_secret_key_news_portal"

# Initialize Database on launch
init_db()

# Start background automated news sweep
start_background_scheduler()

# Context Processor for Global Variables
@app.context_processor
def inject_globals():
    ads = get_active_ads()
    breaking = get_breaking_news(limit=8)
    city_counts = get_city_counts()
    return {
        "site_name": SITE_NAME,
        "site_tagline": SITE_TAGLINE,
        "site_description": SITE_DESCRIPTION,
        "districts": PUNJAB_DISTRICTS,
        "categories": CATEGORIES,
        "ads": ads,
        "breaking_news": breaking,
        "city_counts": city_counts
    }

@app.route("/")
def index():
    featured = get_featured_news(limit=5)
    recent = get_recent_articles(limit=24)
    # City highlights: pick top 3 big districts
    ludhiana_news = get_articles_by_city("ludhiana", limit=4)
    amritsar_news = get_articles_by_city("amritsar", limit=4)
    jalandhar_news = get_articles_by_city("jalandhar", limit=4)
    mohali_news = get_articles_by_city("mohali", limit=4)
    
    return render_template(
        "index.html",
        featured=featured,
        recent=recent,
        ludhiana_news=ludhiana_news,
        amritsar_news=amritsar_news,
        jalandhar_news=jalandhar_news,
        mohali_news=mohali_news,
        active_tab="all"
    )

@app.route("/city/<city_id>")
def city_page(city_id):
    city_info = next((c for c in PUNJAB_DISTRICTS if c['id'] == city_id), None)
    if not city_info:
        return redirect(url_for("index"))
    articles = get_articles_by_city(city_id, limit=30)
    return render_template("city.html", city=city_info, articles=articles)

@app.route("/category/<category_id>")
def category_page(category_id):
    cat_info = next((c for c in CATEGORIES if c['id'] == category_id), None)
    if not cat_info:
        return redirect(url_for("index"))
    articles = get_articles_by_category(category_id, limit=30)
    return render_template("category.html", category=cat_info, articles=articles)

@app.route("/article/<slug>")
def article_detail(slug):
    article = get_article_by_slug(slug)
    if not article:
        flash("खबर नहीं मिली या हटा दी गई है।", "warning")
        return redirect(url_for("index"))
    
    # Increment views
    increment_views(article['id'])
    
    # Get related articles from the same city
    related = get_related_articles(article['city'], article['id'], limit=4)
    
    # Generate canonical URL for SEO
    current_url = request.url
    
    return render_template("article.html", article=article, related=related, current_url=current_url)

@app.route("/search")
def search():
    query = request.args.get("q", "").strip()
    articles = search_articles(query) if query else []
    return render_template("search.html", query=query, articles=articles)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        action = request.form.get("action")
        if action == "manual_add":
            title = request.form.get("title")
            city = request.form.get("city")
            category = request.form.get("category", "general")
            summary = request.form.get("summary", "")
            content = request.form.get("content", "")
            is_breaking = 1 if request.form.get("is_breaking") else 0
            
            city_info = next((c for c in PUNJAB_DISTRICTS if c['id'] == city), None)
            city_name = city_info['name'] if city_info else city
            image_url = city_info['image'] if city_info else "https://images.unsplash.com/photo-1585829365295-ab7cd400c167"
            
            insert_article(
                title=title,
                original_title=title,
                summary=summary,
                highlights=[f"ताज़ा समाचार: {title}", f"क्षेत्र: {city_name}"],
                content=f"<p>{content}</p>",
                city=city,
                city_name=city_name,
                category=category,
                source_name="PunjabState Desk",
                source_url=f"custom-{int(os.times()[4]*1000)}",
                image_url=image_url,
                is_breaking=is_breaking,
                is_featured=1
            )
            flash("विशेष खबर सफलतापूर्वक पब्लिश की गई!", "success")
        elif action == "update_ad":
            slot_key = request.form.get("slot_key")
            title = request.form.get("title")
            image_url = request.form.get("image_url")
            target_url = request.form.get("target_url")
            sponsor_name = request.form.get("sponsor_name")
            is_active = 1 if request.form.get("is_active") else 0
            update_ad_slot(slot_key, title, image_url, target_url, sponsor_name, is_active)
            flash("विज्ञापन बैनर अपडेट हो गया!", "success")
        elif action == "delete_article":
            art_id = request.form.get("article_id")
            if art_id:
                delete_article(art_id)
                flash("खबर हटा दी गई।", "info")
        return redirect(url_for("admin"))

    stats = get_total_stats()
    scheduler_status = get_scheduler_status()
    recent = get_recent_articles(limit=50)
    return render_template("admin.html", stats=stats, scheduler=scheduler_status, recent=recent)

@app.route("/api/fetch-now", methods=["POST"])
def api_fetch_now():
    trigger_manual_fetch_async()
    return jsonify({
        "status": "success",
        "message": "ऑटोमैटिक फेचर बैकग्राउंड में शुरू हो गया है। कुछ सेकंड में नई खबरें लोड हो जाएंगी।"
    })

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
