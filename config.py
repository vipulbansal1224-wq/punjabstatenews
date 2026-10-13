"""
PunjabState News - Configuration & Constants
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "news.db")

SITE_NAME = "PunjabState News"
SITE_TAGLINE = "पंजाब के हर शहर की सबसे तेज़ और सटीक ख़बरें"
SITE_DESCRIPTION = "PunjabState News provides real-time automated news coverage from all 23 districts of Punjab, including Ludhiana, Amritsar, Jalandhar, Patiala, Bathinda, Mohali, and more."

# Punjab Districts and Cities
PUNJAB_DISTRICTS = [
    {
        "id": "amritsar",
        "name": "Amritsar",
        "punjabi": "ਅੰਮ੍ਰਿਤਸਰ",
        "hindi": "अमृतसर",
        "region": "Majha",
        "image": "https://images.unsplash.com/photo-1588096344356-9b634865d4b0?auto=format&fit=crop&w=800&q=80",
        "query": "Amritsar Punjab news"
    },
    {
        "id": "ludhiana",
        "name": "Ludhiana",
        "punjabi": "ਲੁਧਿਆਣਾ",
        "hindi": "लुधियाना",
        "region": "Malwa",
        "image": "https://images.unsplash.com/photo-1596178065887-1198b6148b2b?auto=format&fit=crop&w=800&q=80",
        "query": "Ludhiana Punjab news"
    },
    {
        "id": "jalandhar",
        "name": "Jalandhar",
        "punjabi": "ਜਲੰਧਰ",
        "hindi": "जालंधर",
        "region": "Doaba",
        "image": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=800&q=80",
        "query": "Jalandhar Punjab news"
    },
    {
        "id": "patiala",
        "name": "Patiala",
        "punjabi": "ਪਟਿਆਲਾ",
        "hindi": "पटियाला",
        "region": "Malwa",
        "image": "https://images.unsplash.com/photo-1590053344605-728b704fb335?auto=format&fit=crop&w=800&q=80",
        "query": "Patiala Punjab news"
    },
    {
        "id": "bathinda",
        "name": "Bathinda",
        "punjabi": "ਬਠਿੰਡਾ",
        "hindi": "बठिंडा",
        "region": "Malwa",
        "image": "https://images.unsplash.com/photo-1508873696983-2df5703bc20d?auto=format&fit=crop&w=800&q=80",
        "query": "Bathinda Punjab news"
    },
    {
        "id": "mohali",
        "name": "Mohali (SAS Nagar)",
        "punjabi": "ਮੋਹਾਲੀ",
        "hindi": "मोहाली",
        "region": "Malwa",
        "image": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800&q=80",
        "query": "Mohali SAS Nagar Punjab news"
    },
    {
        "id": "hoshiarpur",
        "name": "Hoshiarpur",
        "punjabi": "ਹੁਸ਼ਿਆਰਪੁਰ",
        "hindi": "होशियारपुर",
        "region": "Doaba",
        "image": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=800&q=80",
        "query": "Hoshiarpur Punjab news"
    },
    {
        "id": "pathankot",
        "name": "Pathankot",
        "punjabi": "ਪਠਾਨਕੋਟ",
        "hindi": "पठानकोट",
        "region": "Majha",
        "image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
        "query": "Pathankot Punjab news"
    },
    {
        "id": "moga",
        "name": "Moga",
        "punjabi": "ਮੋਗਾ",
        "hindi": "मोगा",
        "region": "Malwa",
        "image": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=800&q=80",
        "query": "Moga Punjab news"
    },
    {
        "id": "firozpur",
        "name": "Firozpur",
        "punjabi": "ਫ਼ਿਰੋਜ਼ਪੁਰ",
        "hindi": "फ़िरोज़पुर",
        "region": "Malwa",
        "image": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=800&q=80",
        "query": "Firozpur Punjab news"
    },
    {
        "id": "gurdaspur",
        "name": "Gurdaspur",
        "punjabi": "ਗੁਰਦਾਸਪੁਰ",
        "hindi": "गुरदासपुर",
        "region": "Majha",
        "image": "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=800&q=80",
        "query": "Gurdaspur Punjab news"
    },
    {
        "id": "sangrur",
        "name": "Sangrur",
        "punjabi": "ਸੰਗਰੂਰ",
        "hindi": "संगरूर",
        "region": "Malwa",
        "image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=800&q=80",
        "query": "Sangrur Punjab news"
    },
    {
        "id": "kapurthala",
        "name": "Kapurthala",
        "punjabi": "ਕਪੂਰਥਲਾ",
        "hindi": "कपूरथला",
        "region": "Doaba",
        "image": "https://images.unsplash.com/photo-1541888946425-d0fbb186c5f9?auto=format&fit=crop&w=800&q=80",
        "query": "Kapurthala Punjab news"
    },
    {
        "id": "faridkot",
        "name": "Faridkot",
        "punjabi": "ਫ਼ਰੀਦਕੋਟ",
        "hindi": "फरीदकोट",
        "region": "Malwa",
        "image": "https://images.unsplash.com/photo-1472214103451-9374bd1c798e?auto=format&fit=crop&w=800&q=80",
        "query": "Faridkot Punjab news"
    },
    {
        "id": "fazilka",
        "name": "Fazilka",
        "punjabi": "ਫ਼ਾਜ਼ਿਲਕਾ",
        "hindi": "फाजिल्का",
        "region": "Malwa",
        "image": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=800&q=80",
        "query": "Fazilka Punjab news"
    },
    {
        "id": "muktsar",
        "name": "Sri Muktsar Sahib",
        "punjabi": "ਸ੍ਰੀ ਮੁਕਤਸਰ ਸਾਹਿਬ",
        "hindi": "श्री मुक्तसर साहिब",
        "region": "Malwa",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
        "query": "Sri Muktsar Sahib Punjab news"
    },
    {
        "id": "barnala",
        "name": "Barnala",
        "punjabi": "ਬਰਨਾਲਾ",
        "hindi": "बरनाला",
        "region": "Malwa",
        "image": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=800&q=80",
        "query": "Barnala Punjab news"
    },
    {
        "id": "mansa",
        "name": "Mansa",
        "punjabi": "ਮਾਨਸਾ",
        "hindi": "मानसा",
        "region": "Malwa",
        "image": "https://images.unsplash.com/photo-1473448912268-2022ce9509d8?auto=format&fit=crop&w=800&q=80",
        "query": "Mansa Punjab news"
    },
    {
        "id": "rupnagar",
        "name": "Rupnagar (Ropar)",
        "punjabi": "ਰੂਪਨਗਰ",
        "hindi": "रूपनगर",
        "region": "Malwa",
        "image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=80",
        "query": "Rupnagar Ropar Punjab news"
    },
    {
        "id": "fatehgarh",
        "name": "Fatehgarh Sahib",
        "punjabi": "ਫ਼ਤਹਿਗੜ੍ਹ ਸਾਹਿਬ",
        "hindi": "फतेहगढ़ साहिब",
        "region": "Malwa",
        "image": "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=800&q=80",
        "query": "Fatehgarh Sahib Punjab news"
    },
    {
        "id": "tarntaran",
        "name": "Tarn Taran",
        "punjabi": "ਤਰਨ ਤਾਰਨ",
        "hindi": "तरन तारण",
        "region": "Majha",
        "image": "https://images.unsplash.com/photo-1470246973918-29a93221c455?auto=format&fit=crop&w=800&q=80",
        "query": "Tarn Taran Punjab news"
    },
    {
        "id": "nawanshahr",
        "name": "SBS Nagar (Nawanshahr)",
        "punjabi": "ਨਵਾਂਸ਼ਹਿਰ",
        "hindi": "नवांशहर",
        "region": "Doaba",
        "image": "https://images.unsplash.com/photo-1477959858617-67f30bc75b82?auto=format&fit=crop&w=800&q=80",
        "query": "Nawanshahr Shaheed Bhagat Singh Nagar Punjab news"
    },
    {
        "id": "malerkotla",
        "name": "Malerkotla",
        "punjabi": "ਮਾਲੇਰਕੋਟਲਾ",
        "hindi": "मालेरकोटला",
        "region": "Malwa",
        "image": "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?auto=format&fit=crop&w=800&q=80",
        "query": "Malerkotla Punjab news"
    }
]

# News Categories
CATEGORIES = [
    {"id": "politics", "name": "Politics", "hindi": "राजनीति", "punjabi": "ਰਾਜਨੀਤੀ", "icon": "landmark"},
    {"id": "crime", "name": "Crime & Law", "hindi": "अपराध एवं कानून", "punjabi": "ਅਪਰਾਧ ਅਤੇ ਕਾਨੂੰਨ", "icon": "shield-alert"},
    {"id": "education", "name": "Education & Jobs", "hindi": "शिक्षा एवं नौकरी", "punjabi": "ਸਿੱਖਿਆ ਅਤੇ ਨੌਕਰੀਆਂ", "icon": "graduation-cap"},
    {"id": "agriculture", "name": "Agriculture & Farmers", "hindi": "कृषि एवं किसान", "punjabi": "ਖੇਤੀਬਾੜੀ ਅਤੇ ਕਿਸਾਨ", "icon": "sprout"},
    {"id": "sports", "name": "Sports", "hindi": "खेल", "punjabi": "ਖੇਡਾਂ", "icon": "trophy"},
    {"id": "business", "name": "Business & Trade", "hindi": "व्यापार", "punjabi": "ਵਪਾਰ", "icon": "trending-up"},
    {"id": "general", "name": "General News", "hindi": "ताज़ा हलचल", "punjabi": "ਤਾਜ਼ਾ ਖ਼ਬਰਾਂ", "icon": "newspaper"}
]

# Category Curated Fallback Images
CATEGORY_IMAGES = {
    "politics": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?auto=format&fit=crop&w=800&q=80",
    "crime": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=800&q=80",
    "education": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=800&q=80",
    "agriculture": "https://images.unsplash.com/photo-1500937386664-56d1dfef3854?auto=format&fit=crop&w=800&q=80",
    "sports": "https://images.unsplash.com/photo-1530549387789-4c1017266635?auto=format&fit=crop&w=800&q=80",
    "business": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
    "general": "https://images.unsplash.com/photo-1585829365295-ab7cd400c167?auto=format&fit=crop&w=800&q=80"
}

# Fetcher Settings - Auto updates every 1 hour (60 minutes)
FETCH_INTERVAL_MINUTES = 60
MAX_ITEMS_PER_CITY = 5
GOOGLE_NEWS_RSS_URL = "https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"

# Multilingual UI Dictionary (Hindi, Punjabi, English)
LANGUAGES = {
    "hi": {"name": "हिंदी", "code": "hi", "flag": "🇮🇳"},
    "pa": {"name": "ਪੰਜਾਬੀ", "code": "pa", "flag": "☬"},
    "en": {"name": "English", "code": "en", "flag": "🇬🇧"}
}

TRANSLATIONS = {
    "hi": {
        "home": "होम",
        "select_district": "पंजाब के 23 ज़िले",
        "district_filter": "ज़िला अनुसार ताज़ा समाचार (City Filter)",
        "all_districts": "सभी ज़िले",
        "search_placeholder": "खबर या शहर खोजें...",
        "breaking": "ब्रेकिंग",
        "read_more": "पूरी खबर पढ़ें",
        "read": "पढ़ें",
        "views": "देखे गए",
        "published": "प्रकाशित",
        "highlights": "त्वरित सारांश (Quick Highlights)",
        "share_whatsapp": "WhatsApp पर शेयर करें",
        "share_msg": "इस खबर को अपने दोस्तों और ग्रुप में शेयर करें:",
        "related_news": "की अन्य ख़बरें",
        "all_news": "सभी देखें",
        "verified_desk": "प्रमाणित संपादकीय डेस्क",
        "special_report": "PunjabState विशेष रिपोर्टिंग",
        "about_us": "हमारे बारे में",
        "contact_us": "संपर्क एवं संपादकीय डेस्क",
        "admin_panel": "एडमिन पैनल",
        "tagline": "पंजाब के हर शहर की सबसे तेज़ और सटीक ख़बरें",
        "all_districts_live": "पंजाब के सभी 23 ज़िले लाइव"
    },
    "pa": {
        "home": "ਮੁੱਖ ਪੰਨਾ",
        "select_district": "ਪੰਜਾਬ ਦੇ 23 ਜ਼ਿਲ੍ਹੇ",
        "district_filter": "ਜ਼ਿਲ੍ਹਾ ਵਾਰ ਤਾਜ਼ਾ ਖ਼ਬਰਾਂ (City Filter)",
        "all_districts": "ਸਾਰੇ ਜ਼ਿਲ੍ਹੇ",
        "search_placeholder": "ਖ਼ਬਰ ਜਾਂ ਸ਼ਹਿਰ ਖੋਜੋ...",
        "breaking": "ਤਾਜ਼ਾ ਖ਼ਬਰ",
        "read_more": "ਪੂਰੀ ਖ਼ਬਰ ਪੜ੍ਹੋ",
        "read": "ਪੜ੍ਹੋ",
        "views": "ਵੇਖੀਆਂ ਗਈਆਂ",
        "published": "ਪ੍ਰਕਾਸ਼ਿਤ",
        "highlights": "ਮੁੱਖ ਨੁਕਤੇ (Quick Highlights)",
        "share_whatsapp": "WhatsApp 'ਤੇ ਸ਼ੇਅਰ ਕਰੋ",
        "share_msg": "ਇਸ ਖ਼ਬਰ ਨੂੰ ਆਪਣੇ ਦੋਸਤਾਂ ਅਤੇ ਗਰੁੱਪਾਂ ਵਿੱਚ ਸ਼ੇਅਰ ਕਰੋ:",
        "related_news": "ਦੀਆਂ ਹੋਰ ਖ਼ਬਰਾਂ",
        "all_news": "ਸਭ ਵੇਖੋ",
        "verified_desk": "ਪ੍ਰਮਾਣਿਤ ਸੰਪਾਦਕੀ ਡੈਸਕ",
        "special_report": "PunjabState ਵਿਸ਼ੇਸ਼ ਰਿਪੋਰਟਿੰਗ",
        "about_us": "ਸਾਡੇ ਬਾਰੇ",
        "contact_us": "ਸੰਪਰਕ ਅਤੇ ਸੰਪਾਦਕੀ ਡੈਸਕ",
        "admin_panel": "ਐਡਮਿਨ ਪੈਨਲ",
        "tagline": "ਪੰਜਾਬ ਦੇ ਹਰ ਸ਼ਹਿਰ ਦੀ ਸਭ ਤੋਂ ਤੇਜ਼ ਅਤੇ ਸਹੀ ਖ਼ਬਰ",
        "all_districts_live": "ਪੰਜਾਬ ਦੇ ਸਾਰੇ 23 ਜ਼ਿਲ੍ਹੇ ਲਾਈਵ"
    },
    "en": {
        "home": "Home",
        "select_district": "All 23 Punjab Districts",
        "district_filter": "District-Wise News (City Filter)",
        "all_districts": "All Districts",
        "search_placeholder": "Search news or city...",
        "breaking": "BREAKING",
        "read_more": "Read Full Story",
        "read": "Read",
        "views": "Views",
        "published": "Published",
        "highlights": "Quick Highlights",
        "share_whatsapp": "Share on WhatsApp",
        "share_msg": "Share this news with friends & groups:",
        "related_news": "More Stories from",
        "all_news": "View All",
        "verified_desk": "Verified Editorial Desk",
        "special_report": "PunjabState Special Report",
        "about_us": "About Us",
        "contact_us": "Contact & Newsdesk",
        "admin_panel": "Admin Panel",
        "tagline": "Fastest & Most Accurate Hyperlocal News from Punjab",
        "all_districts_live": "All 23 Punjab Districts Live"
    }
}
