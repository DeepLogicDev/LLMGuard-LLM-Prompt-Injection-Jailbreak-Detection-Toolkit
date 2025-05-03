import datetime

def log_event(event_type, message):
    now = datetime.datetime.now().isoformat()
    print(f"[{now}] [{event_type.upper()}] {message}")
