from datetime import datetime


def log_event(event: str, request_id: str):
    print({
        "event": event,
        "request_id": request_id,
        "timestamp": datetime.utcnow().isoformat()
    })