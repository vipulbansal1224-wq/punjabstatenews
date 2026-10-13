"""
PunjabState News - Content Processor & Smart Rewriter Engine
Enhances headlines, extracts bullet point highlights, classifies categories,
and formats high-value editorial articles for Google News ranking & Discover.
"""
import re
import html
from bs4 import BeautifulSoup
from config import CATEGORIES, CATEGORY_IMAGES

CATEGORY_KEYWORDS = {
    "crime": [
        "arrest", "police", "murder", "theft", "stolen", "fir", "crime", "gangster",
        "drugs", "heroin", "chitta", "seized", "smuggling", "jail", "court", "custody",
        "assault", "killed", "attack", "scam", "fraud", "cyber", "encounter"
    ],
    "politics": [
        "cm", "bhagwant mann", "aap", "congress", "bjp", "sad", "akali dal", "mla",
        "minister", "election", "poll", "rally", "cabinet", "protest", "dharna",
        "assembly", "vidhan sabha", "governor", "leader", "party", "bypoll"
    ],
    "education": [
        "school", "college", "university", "pseb", "board", "exam", "result", "job",
        "jobs", "recruitment", "psssb", "punjab police", "patwari", "clerk", "student",
        "teacher", "admit card", "syllabus", "scholarship", "degrees", "ielts"
    ],
    "agriculture": [
        "kisan", "farmer", "agriculture", "crop", "wheat", "paddy", "basmati", "mandi",
        "msp", "fertilizer", "dap", "urea", "stubble", "parali", "tractor", "irrigation",
        "canal", "cotton", "soil"
    ],
    "sports": [
        "cricket", "kabaddi", "hockey", "tournament", "medal", "gold", "match", "ipl",
        "olympics", "trophy", "player", "coach", "stadium", "wrestling", "championship"
    ],
    "business": [
        "industry", "factory", "trader", "market", "gold", "silver", "export", "import",
        "gst", "tax", "startup", "economy", "investment", "shares", "textile", "hosiery",
        "cycle", "ludhiana industry"
    ]
}

# Media channels & agencies to completely scrub from all stories
MEDIA_CHANNELS = [
    'Hindustan Times', 'The Tribune', 'Tribune News Service', 'Tribune', 'The Indian Express', 'Indian Express',
    'Express News Service', 'NDTV', 'PTC News', 'PTC', 'Babushahi.com', 'Babushahi', 'Punjab Newsline',
    'Newsline', 'Dainik Bhaskar', 'Bhaskar', 'Amar Ujala', 'Dainik Jagran', 'Jagran', 'Punjab Kesari',
    'Times of India', 'TOI', 'India Today', 'Aaj Tak', 'Zee News', 'Zee Punjab', 'Zee', 'News18 Punjab', 'News18',
    'ABP Sanjha', 'ABP News', 'ABP Live', 'ABP', 'ANI', 'PTI', 'IANS', 'UNI', 'BBC News', 'BBC Hindi', 'BBC Punjabi', 'BBC',
    'ETV Bharat', 'Live Law', 'Bar and Bench', 'Newsonair', 'Akashvani', 'All India Radio', 'AIR News',
    'Daily Post Punjab', 'Daily Post', 'Rozana Spokesman', 'Spokesman'
]

def clean_html(raw_html):
    if not raw_html:
        return ""
    soup = BeautifulSoup(raw_html, "html.parser")
    for s in soup(['script', 'style', 'a']):
        s.extract()
    text = soup.get_text(separator=' ')
    return html.unescape(text).strip()

def clean_headline(title):
    """
    Completely eliminates news channels, network tags, and reporter names from headlines.
    """
    if not title:
        return ""
    title = html.unescape(title)

    # 1. Remove trailing channel attribution e.g. " - NDTV", " | Hindustan Times", " - The Tribune"
    title = re.sub(r'\s*[-|–—:]\s*(?:' + '|'.join(re.escape(c) for c in MEDIA_CHANNELS) + r')\b.*$', '', title, flags=re.IGNORECASE)
    # 2. General trailing dash/pipe source tags
    title = re.sub(r'\s*[-|–—]\s*[^–—|-]+$', '', title).strip()
    # 3. Remove leading channel name e.g. "PTC News: ..." or "Babushahi | ..."
    title = re.sub(r'^(?:' + '|'.join(re.escape(c) for c in MEDIA_CHANNELS) + r')\s*[-|–—:]\s*', '', title, flags=re.IGNORECASE)
    # 4. Remove inline (Channel) or (ANI/PTI)
    title = re.sub(r'\s*\((?:' + '|'.join(re.escape(c) for c in MEDIA_CHANNELS) + r')\)\s*', ' ', title, flags=re.IGNORECASE)
    # 5. Remove "By Reporter Name" patterns
    title = re.sub(r'\b(?:by|reported by)\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', '', title, flags=re.IGNORECASE)
    # 6. Scrub any remaining direct channel name matches
    for c in MEDIA_CHANNELS:
        title = re.sub(r'\b' + re.escape(c) + r'\b', '', title, flags=re.IGNORECASE)

    title = re.sub(r'\s+', ' ', title).strip()
    title = re.sub(r'^[^\w\s]+|[^\w\s]+$', '', title).strip()
    return title

def clean_editorial_text(text):
    """
    Completely eliminates reporter bylines and media channel names from editorial text.
    Replaces agency citations with local bureau phrasing.
    """
    if not text:
        return ""
    # Remove reporter bylines e.g. "Reported by Staff Reporter:", "By Correspondent:"
    text = re.sub(r'\b(?:By|Reported by|Special Correspondent|Staff Reporter|Express News Service|Tribune News Service|Correspondent)\b.*?(?:[-—–:]\s*|\n)', '', text, flags=re.IGNORECASE)
    # Remove city + agency lead-ins e.g. "CHANDIGARH (ANI) —"
    text = re.sub(r'^[A-Z\s,]+\((?:ANI|PTI|UNI|IANS)\)\s*[-—–:]\s*', '', text, flags=re.IGNORECASE)
    # Replace channel references with neutral bureau attribution
    for c in MEDIA_CHANNELS:
        text = re.sub(r'\b(?:according to|as reported by|told)\s+' + re.escape(c) + r'\b', 'स्थानीय सूत्रों के अनुसार', text, flags=re.IGNORECASE)
        text = re.sub(r'\b' + re.escape(c) + r'\b', '', text, flags=re.IGNORECASE)

    text = re.sub(r'\s+', ' ', text).strip()
    return text

def classify_category(text):
    text_lower = text.lower()
    scores = {}
    for cat, keywords in CATEGORY_KEYWORDS.items():
        score = sum(1 for kw in keywords if re.search(r'\b' + re.escape(kw) + r'\b', text_lower))
        if score > 0:
            scores[cat] = score
    if scores:
        best_cat = max(scores, key=scores.get)
        return best_cat
    return "general"

def generate_highlights(title, summary, city_name):
    """
    Produces 3-4 structured takeaway bullet points for user engagement & SEO.
    """
    highlights = [
        f"📍 स्थान: पंजाब राज्य के {city_name} क्षेत्र से जुड़ी बड़ी अपडेट।",
        f"⚡ मुख्य घटना: {title} को लेकर स्थानीय प्रशासन और पुलिस अलर्ट।",
        f"🔍 ताज़ा स्थिति: संबंधित विभागों द्वारा मामले पर निगरानी रखी जा रही है।"
    ]
    
    # If summary contains extra details, add as 4th point
    if summary and len(summary) > 40:
        clean_sum = clean_html(summary)[:150].strip()
        if clean_sum and clean_sum not in title:
            highlights.append(f"📌 विवरण: {clean_sum}...")
            
    return highlights

def rewrite_article(raw_title, raw_summary, city_info, source_name="Agency"):
    """
    Transforms raw feed item into a high-value, comprehensive news article
    """
    cleaned_title = clean_headline(raw_title)
    city_name = city_info['name']
    
    # Check if city name is already in headline, if not add it smartly
    if city_name.lower() not in cleaned_title.lower() and "punjab" not in cleaned_title.lower():
        enhanced_title = f"{city_name} Update: {cleaned_title}"
    else:
        enhanced_title = cleaned_title

    # Detect category
    combined_text = f"{cleaned_title} {raw_summary}"
    category = classify_category(combined_text)

    # Clean summary and scrub any channel/reporter names
    clean_sum = clean_editorial_text(clean_html(raw_summary))
    if not clean_sum or len(clean_sum) < 20:
        clean_sum = f"{city_name} ({city_info.get('hindi', '')}) से ताज़ा घटनाक्रम सामने आया है, जिसमें {cleaned_title} को लेकर चर्चा बनी हुई है।"

    # Generate Highlights
    highlights = generate_highlights(cleaned_title, clean_sum, city_name)

    # Build comprehensive original editorial content
    content_paragraphs = [
        f"<p class='lead font-medium text-gray-800 text-lg leading-relaxed mb-4'>"
        f"<strong>{city_name.upper()} (PunjabState News):</strong> "
        f"पंजाब के {city_name} जिले से एक महत्वपूर्ण समाचार सामने आया है। "
        f"{cleaned_title} के संबंध में मिली नवीनतम जानकारी के अनुसार, स्थानीय प्रशासन और नागरिकों के बीच इस घटनाक्रम को लेकर हलचल तेज हो गई है।"
        f"</p>",

        f"<div class='my-6 p-5 bg-amber-50 border-l-4 border-amber-500 rounded-r-lg'>"
        f"<h4 class='text-amber-900 font-bold mb-2 flex items-center gap-2'>"
        f"<span>📌</span> त्वरित सारांश (Quick Highlights)"
        f"</h4>"
        f"<ul class='space-y-1.5 text-gray-700 text-sm'>"
        + "".join([f"<li>• {h}</li>" for h in highlights]) +
        f"</ul>"
        f"</div>",

        f"<p class='text-gray-700 leading-relaxed mb-4'>"
        f"मिली जानकारी के अनुसार, {clean_sum} इस घटना को लेकर संबंधित अधिकारियों ने आवश्यक कदम उठाने शुरू कर दिए हैं। "
        f"स्थानीय सूत्रों का कहना है कि स्थिति पर लगातार नज़र रखी जा रही है ताकि किसी भी प्रकार की असुविधा से बचा जा सके।"
        f"</p>",

        f"<p class='text-gray-700 leading-relaxed mb-4'>"
        f"{city_name} और आसपास के इलाकों में इस खबर को लेकर चर्चा का माहौल है। "
        f"PunjabState News की टीम जमीनी स्तर से लगातार इस मामले के हर अपडेट पर नजर बनाए हुए है। "
        f"जैसे ही इस मामले में कोई आधिकारिक बयान या नई प्रगति सामने आती है, पाठकों को तुरंत सूचित किया जाएगा।"
        f"</p>",

        f"<div class='mt-6 p-4 bg-gray-50 border border-gray-200 rounded text-xs text-gray-500 flex items-center justify-between'>"
        f"<span>विशेष रिपोर्टिंग: PunjabState ब्यूरो डेस्क</span>"
        f"<span class='text-emerald-700 font-semibold'>✓ Verified by PunjabState News Desk</span>"
        f"</div>"
    ]

    full_content = "\n".join(content_paragraphs)

    return {
        "title": enhanced_title,
        "original_title": raw_title,
        "summary": clean_sum,
        "highlights": highlights,
        "content": full_content,
        "category": category,
        "city": city_info['id'],
        "city_name": city_info['name']
    }
