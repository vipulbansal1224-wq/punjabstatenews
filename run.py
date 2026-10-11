"""
PunjabState News - 1-Click Launcher
"""
import sys
import os

# Ensure local directory is in path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from database import init_db, get_total_stats
from app import app

def main():
    print("=" * 65)
    print("  PUNJABSTATE NEWS (पंजाब स्टेट न्यूज़) - AUTOMATED PORTAL")
    print("  Covering all 23 Districts of Punjab with 24x7 Auto-Fetcher")
    print("=" * 65)

    init_db()
    stats = get_total_stats()
    print(f"[*] Database Status: {stats['total_news']} articles active across {stats['active_cities']} districts.")
    print(f"[*] Web Server starting at: http://localhost:8000")
    print(f"[*] Admin Panel at:         http://localhost:8000/admin")
    print("=" * 65)
    print("Press CTRL+C to stop the server anytime.\n")

    app.run(host="127.0.0.1", port=8000, debug=False)

if __name__ == "__main__":
    main()
