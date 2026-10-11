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

# Fetcher Settings
FETCH_INTERVAL_MINUTES = 20
MAX_ITEMS_PER_CITY = 5
GOOGLE_NEWS_RSS_URL = "https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
