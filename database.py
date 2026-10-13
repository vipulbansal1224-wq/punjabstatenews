"""
PunjabState News - Database Layer (SQLite)
"""
import sqlite3
import json
import re
import unicodedata
from datetime import datetime
from config import DB_PATH, PUNJAB_DISTRICTS

def get_db():
    conn = sqlite3.connect(DB_PATH, timeout=30.0, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA busy_timeout = 30000;")
    return conn

def slugify(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[-\s]+', '-', text).strip('-_')
    return text[:120] if text else "news-update"

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    # Enable WAL mode for high concurrency (readers never block writers, zero lag)
    try:
        cursor.execute("PRAGMA journal_mode = WAL;")
        cursor.execute("PRAGMA synchronous = NORMAL;")
    except Exception:
        pass

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        slug TEXT UNIQUE NOT NULL,
        original_title TEXT,
        summary TEXT,
        highlights TEXT,
        content TEXT,
        city TEXT NOT NULL,
        city_name TEXT,
        category TEXT DEFAULT 'general',
        source_name TEXT,
        source_url TEXT UNIQUE,
        image_url TEXT,
        published_at TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        views_count INTEGER DEFAULT 0,
        is_breaking INTEGER DEFAULT 0,
        is_featured INTEGER DEFAULT 0
    )
    """)

    # Performance indexes for ultra-fast query responses on refresh
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_articles_city ON articles(city);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_articles_category ON articles(category);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_articles_published ON articles(published_at DESC);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_articles_breaking ON articles(is_breaking);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_articles_featured ON articles(is_featured);")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ad_slots (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        slot_key TEXT UNIQUE NOT NULL,
        title TEXT,
        image_url TEXT,
        target_url TEXT,
        sponsor_name TEXT,
        is_active INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS settings (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    """)

    # Default ad slots if not present
    default_ads = [
        (
            "header_banner",
            "Book IELTS & Study Visa in Canada/UK - Top Consultants Punjab",
            "/static/images/banner_ielts.jpg",
            "https://example.com/visa",
            "Apex Visa Punjab",
            1
        ),
        (
            "sidebar_banner_1",
            "Luxury Flats & Plots in Aerocity Mohali - Direct Builder Offer",
            "/static/images/banner_real_estate.jpg",
            "https://example.com/realty",
            "Punjab Royal Builders",
            1
        ),
        (
            "in_article_banner",
            "Tractor & Agri Equipment Festival - 50% Subsidy Scheme",
            "/static/images/banner_kisan.jpg",
            "https://example.com/agri",
            "Punjab Kisan Agri",
            1
        )
    ]

    for slot in default_ads:
        cursor.execute("""
        INSERT OR IGNORE INTO ad_slots (slot_key, title, image_url, target_url, sponsor_name, is_active)
        VALUES (?, ?, ?, ?, ?, ?)
        """, slot)

    # Default settings
    default_settings = [
        ("auto_fetch", "1"),
        ("fetch_interval", "20"),
        ("site_notice", "पंजाब के सभी 23 जिलों की हर ताज़ा खबर सबसे पहले PunjabState News पर")
    ]
    for key, val in default_settings:
        cursor.execute("INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)", (key, val))

    conn.commit()
    conn.close()

def article_exists(source_url, title):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM articles WHERE source_url = ? OR title = ?", (source_url, title))
    row = cursor.fetchone()
    conn.close()
    return row is not None

def insert_article(title, original_title, summary, highlights, content, city, city_name,
                   category, source_name, source_url, image_url, published_at=None,
                   is_breaking=0, is_featured=0):
    conn = get_db()
    cursor = conn.cursor()

    base_slug = slugify(title)
    slug = base_slug
    counter = 1
    while True:
        cursor.execute("SELECT id FROM articles WHERE slug = ?", (slug,))
        if not cursor.fetchone():
            break
        slug = f"{base_slug}-{counter}"
        counter += 1

    pub_at = published_at or datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    highlights_json = json.dumps(highlights) if isinstance(highlights, list) else json.dumps([])

    try:
        cursor.execute("""
        INSERT INTO articles (
            title, slug, original_title, summary, highlights, content,
            city, city_name, category, source_name, source_url, image_url,
            published_at, is_breaking, is_featured
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            title, slug, original_title, summary, highlights_json, content,
            city, city_name, category, source_name, source_url, image_url,
            pub_at, is_breaking, is_featured
        ))
        conn.commit()
        art_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        art_id = None
    finally:
        conn.close()

    return art_id

def get_recent_articles(limit=24, offset=0):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM articles
    ORDER BY id DESC
    LIMIT ? OFFSET ?
    """, (limit, offset))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_articles_by_city(city_id, limit=20, offset=0):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM articles
    WHERE city = ?
    ORDER BY id DESC
    LIMIT ? OFFSET ?
    """, (city_id, limit, offset))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_articles_by_category(category_id, limit=20, offset=0):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM articles
    WHERE category = ?
    ORDER BY id DESC
    LIMIT ? OFFSET ?
    """, (category_id, limit, offset))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_breaking_news(limit=8):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT id, title, slug, city_name, published_at FROM articles
    WHERE is_breaking = 1 OR id IN (SELECT id FROM articles ORDER BY id DESC LIMIT ?)
    ORDER BY id DESC
    LIMIT ?
    """, (limit, limit))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_featured_news(limit=5):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM articles
    ORDER BY is_featured DESC, id DESC
    LIMIT ?
    """, (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_article_by_slug(slug):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles WHERE slug = ?", (slug,))
    row = cursor.fetchone()
    if row:
        data = dict(row)
        try:
            data['highlights_list'] = json.loads(data.get('highlights') or '[]')
        except:
            data['highlights_list'] = []
        conn.close()
        return data
    conn.close()
    return None

def increment_views(article_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE articles SET views_count = views_count + 1 WHERE id = ?", (article_id,))
    conn.commit()
    conn.close()

def search_articles(query, limit=25):
    conn = get_db()
    cursor = conn.cursor()
    search_term = f"%{query}%"
    cursor.execute("""
    SELECT * FROM articles
    WHERE title LIKE ? OR summary LIKE ? OR city_name LIKE ?
    ORDER BY id DESC
    LIMIT ?
    """, (search_term, search_term, search_term, limit))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_related_articles(city, exclude_id, limit=4):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM articles
    WHERE city = ? AND id != ?
    ORDER BY id DESC
    LIMIT ?
    """, (city, exclude_id, limit))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_city_counts():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT city, count(*) as count FROM articles GROUP BY city")
    rows = cursor.fetchall()
    conn.close()
    return {row['city']: row['count'] for row in rows}

def get_total_stats():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) as total, sum(views_count) as views FROM articles")
    stats = cursor.fetchone()
    cursor.execute("SELECT count(DISTINCT city) as active_cities FROM articles")
    cities = cursor.fetchone()
    conn.close()
    return {
        "total_news": stats['total'] if stats else 0,
        "total_views": stats['views'] if stats and stats['views'] else 0,
        "active_cities": cities['active_cities'] if cities else 0
    }

def get_active_ads():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ad_slots WHERE is_active = 1")
    rows = cursor.fetchall()
    conn.close()
    return {row['slot_key']: dict(row) for row in rows}

def update_ad_slot(slot_key, title, image_url, target_url, sponsor_name, is_active):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE ad_slots
    SET title = ?, image_url = ?, target_url = ?, sponsor_name = ?, is_active = ?
    WHERE slot_key = ?
    """, (title, image_url, target_url, sponsor_name, is_active, slot_key))
    conn.commit()
    conn.close()

def delete_article(article_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles WHERE id = ?", (article_id,))
    conn.commit()
    conn.close()
