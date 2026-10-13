"""
PunjabState News - Background Automation Scheduler
Runs periodic sweeps of Punjab districts in a background daemon thread
"""
import threading
import time
import schedule
from fetcher import fetch_all_punjab_news
from config import FETCH_INTERVAL_MINUTES

_scheduler_running = False
_is_fetching = False
_last_run_time = None
_last_fetched_count = 0

def run_job():
    global _last_run_time, _last_fetched_count, _is_fetching
    if _is_fetching:
        print("[Scheduler] Sweep already in progress, skipping duplicate run.")
        return
    _is_fetching = True
    try:
        count = fetch_all_punjab_news(max_items_per_city=3)
        _last_run_time = time.strftime('%Y-%m-%d %H:%M:%S')
        _last_fetched_count = count
    except Exception as e:
        print(f"Error during scheduled sweep: {e}")
    finally:
        _is_fetching = False

def scheduler_worker():
    # Initial gentle sweep 10s after startup so fresh news is ready on boot/deploy
    time.sleep(10)
    run_job()
    schedule.every(FETCH_INTERVAL_MINUTES).minutes.do(run_job)
    while True:
        schedule.run_pending()
        time.sleep(10)

def start_background_scheduler():
    global _scheduler_running
    if not _scheduler_running:
        _scheduler_running = True
        t = threading.Thread(target=scheduler_worker, daemon=True)
        t.start()
        print(f"[Scheduler] Background auto-fetch started (Runs every {FETCH_INTERVAL_MINUTES} mins)")

def trigger_manual_fetch_async():
    """Triggers an immediate fetch in background thread"""
    t = threading.Thread(target=run_job, daemon=True)
    t.start()
    return True

def get_scheduler_status():
    return {
        "running": _scheduler_running,
        "interval_minutes": FETCH_INTERVAL_MINUTES,
        "last_run": _last_run_time,
        "last_count": _last_fetched_count
    }
