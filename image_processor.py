"""
PunjabState News - Real Image Fetcher & Processing Engine
Decodes Google News URLs to original publisher, extracts real news image,
downloads, converts, optimizes via Pillow, and saves locally to prevent copyright and hotlinking issues.
"""
import os
import io
import hashlib
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NEWS_IMAGES_DIR = os.path.join(BASE_DIR, "static", "news_images")
os.makedirs(NEWS_IMAGES_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

def decode_google_news_url(google_url):
    """
    Decodes Google News RSS article URL to get original publisher URL
    """
    try:
        from googlenewsdecoder import gnewsdecoder
        res = gnewsdecoder(google_url)
        if isinstance(res, dict) and res.get('success') and res.get('decoded_url'):
            return res['decoded_url']
    except Exception as e:
        # Fallback: if decoding fails, try direct request
        pass
    return google_url

def extract_real_image_url(publisher_url):
    """
    Scrapes the original news article page to find og:image or main article image
    """
    try:
        resp = requests.get(publisher_url, headers=HEADERS, timeout=8, allow_redirects=True)
        if resp.status_code != 200:
            return None
        
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        # 1. Check og:image
        og_img = soup.find('meta', property='og:image') or soup.find('meta', attrs={'name': 'og:image'})
        if og_img and og_img.get('content') and 'http' in og_img['content']:
            img_url = og_img['content'].strip()
            # Ignore tiny icons/placeholders
            if not any(bad in img_url.lower() for bad in ['favicon', 'logo', 'default', 'blank', 'placeholder']):
                return img_url
        
        # 2. Check twitter:image
        tw_img = soup.find('meta', attrs={'name': 'twitter:image'}) or soup.find('meta', attrs={'property': 'twitter:image'})
        if tw_img and tw_img.get('content') and 'http' in tw_img['content']:
            img_url = tw_img['content'].strip()
            if not any(bad in img_url.lower() for bad in ['favicon', 'logo', 'default']):
                return img_url

        # 3. Check first large article image
        for img in soup.find_all('img'):
            src = img.get('src') or img.get('data-src')
            if src and 'http' in src and not any(bad in src.lower() for bad in ['icon', 'logo', 'avatar', 'ad']):
                return src

    except Exception as e:
        pass
    return None

def download_and_convert_image(image_url, article_id_str):
    """
    Downloads original image, processes it with Pillow:
    - Re-encodes to RGB JPEG
    - Resizes to standard 16:9 news proportion (800x450 max)
    - Adds subtle bottom-right brand watermark 'PunjabState News'
    - Saves locally as /static/news_images/<hash>.jpg
    Returns relative URL e.g. '/static/news_images/<hash>.jpg'
    """
    if not image_url or not image_url.startswith('http'):
        return None
    
    url_hash = hashlib.md5(image_url.encode('utf-8')).hexdigest()[:12]
    filename = f"news_{url_hash}.jpg"
    local_path = os.path.join(NEWS_IMAGES_DIR, filename)
    relative_url = f"/static/news_images/{filename}"

    # If already downloaded and converted, return it
    if os.path.exists(local_path) and os.path.getsize(local_path) > 2000:
        return relative_url

    try:
        resp = requests.get(image_url, headers=HEADERS, timeout=10)
        if resp.status_code != 200 or len(resp.content) < 1500:
            return None

        img = Image.open(io.BytesIO(resp.content))
        
        # Convert to RGB (handles RGBA / Palette)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Target standard width 800
        target_w = 800
        w, h = img.size
        if w > 0:
            target_h = int((target_w / w) * h)
            # Cap extreme heights
            if target_h > 600:
                target_h = 500
            img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)

        # Add subtle, professional watermark badge on bottom right
        draw = ImageDraw.Draw(img)
        text = "PunjabState News"
        
        # Draw translucent badge box on bottom right
        box_w = 140
        box_h = 24
        box_x = img.width - box_w - 12
        box_y = img.height - box_h - 10
        
        # Semi-transparent dark overlay for watermark text
        draw.rectangle([box_x, box_y, box_x + box_w, box_y + box_h], fill=(15, 23, 42))
        draw.text((box_x + 12, box_y + 5), text, fill=(255, 255, 255))

        # Save with optimized JPEG quality
        img.save(local_path, "JPEG", quality=85, optimize=True)
        return relative_url

    except Exception as e:
        return None

def generate_news_card(title, city_name="Punjab", category="general"):
    """
    Generates an authentic PunjabState News headline card when no photo is provided
    Never uses third-party dummy stock images!
    """
    card_hash = hashlib.md5((title + city_name).encode('utf-8')).hexdigest()[:12]
    filename = f"card_{card_hash}.jpg"
    local_path = os.path.join(NEWS_IMAGES_DIR, filename)
    relative_url = f"/static/news_images/{filename}"

    if os.path.exists(local_path) and os.path.getsize(local_path) > 2000:
        return relative_url

    try:
        # 800x450 standard 16:9 canvas
        img = Image.new('RGB', (800, 450), color=(15, 23, 42))
        draw = ImageDraw.Draw(img)

        # Gradient / decorative header bar
        draw.rectangle([0, 0, 800, 60], fill=(30, 58, 138))
        draw.rectangle([0, 58, 800, 62], fill=(245, 158, 11))

        # Brand header
        draw.text((25, 20), "PunjabState News  |  विशेष ग्राउंड रिपोर्टिंग", fill=(255, 255, 255))
        
        # City & Category Badges
        draw.rectangle([25, 90, 180, 125], fill=(220, 38, 38))
        draw.text((38, 98), f"📍 {city_name.upper()}", fill=(255, 255, 255))

        draw.rectangle([195, 90, 320, 125], fill=(37, 99, 235))
        draw.text((210, 98), f"● {category.upper()}", fill=(255, 255, 255))

        # Headline wrap
        words = title.split()
        lines = []
        curr_line = []
        for w in words:
            curr_line.append(w)
            if len(" ".join(curr_line)) > 38:
                lines.append(" ".join(curr_line))
                curr_line = []
        if curr_line:
            lines.append(" ".join(curr_line))

        y = 155
        for line in lines[:4]:
            draw.text((25, y), line, fill=(248, 250, 252))
            y += 42

        # Bottom footer bar
        draw.rectangle([0, 410, 800, 450], fill=(2, 6, 23))
        draw.text((25, 422), "ਪੰਜਾਬ ਦੇ ਸਾਰੇ 23 ਜ਼ਿਲ੍ਹੇ  •  24x7 Digital Media Network  •  Verified Desk", fill=(148, 163, 184))

        img.save(local_path, "JPEG", quality=90)
        return relative_url
    except Exception as e:
        return relative_url

def process_article_real_image(google_url, fallback_image=None, title="", city_name="Punjab", category="general"):
    """
    Full pipeline:
    Google RSS link -> Real Publisher URL -> Real image URL -> Downloaded, converted local image.
    If no real photo exists, generates authentic branded PunjabState News card.
    Never returns third-party dummy stock images!
    """
    try:
        # Step 1: Decode to real publisher
        pub_url = decode_google_news_url(google_url)
        
        # Step 2: Extract real image URL from original publisher
        if pub_url and pub_url != google_url:
            real_img_url = extract_real_image_url(pub_url)
            if real_img_url:
                local_img = download_and_convert_image(real_img_url, pub_url)
                if local_img:
                    return local_img
    except Exception as e:
        pass
    
    # If title provided, generate branded breaking news card
    if title:
        return generate_news_card(title, city_name, category)
        
    return fallback_image or "/static/images/logo.svg"
