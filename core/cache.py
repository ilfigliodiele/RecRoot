import threading
import time

class Cache:
    """Thread-safe in-memory cache with optional TTL."""

    def __init__(self):
        self._store = {}
        self._lock = threading.Lock()

    def set(self, key: str, value, ttl: int = None):
        """Store a value. ttl in seconds, None = forever."""
        expire_at = time.time() + ttl if ttl else None
        with self._lock:
            self._store[key] = {"value": value, "expire_at": expire_at}

    def get(self, key: str):
        """Return value or None if missing/expired."""
        with self._lock:
            entry = self._store.get(key)
            if not entry:
                return None
            if entry["expire_at"] and time.time() > entry["expire_at"]:
                del self._store[key]
                return None
            return entry["value"]

    def delete(self, key: str):
        with self._lock:
            self._store.pop(key, None)

    def clear(self):
        with self._lock:
            self._store.clear()

    def has(self, key: str) -> bool:
        return self.get(key) is not None


# Global cache instance
cache = Cache()
