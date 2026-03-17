"""
Shared requests.Session() for connection pooling and reuse.

- Connection pooling: reuses TCP connections
- TLS session resumption: avoids repeated TLS handshakes
"""
import requests


# Global session instance for connection pooling
_session = None


def get_session():
    """Get or create the shared requests session."""
    global _session
    if _session is None:
        _session = requests.Session()

        adapter = requests.adapters.HTTPAdapter(
            pool_connections=10,
            pool_maxsize=20,
            max_retries=0  # retries are handled by decorators
        )
        _session.mount('http://', adapter)
        _session.mount('https://', adapter)
    return _session


def close_session():
    """Close the shared session. Useful for cleanup in tests."""
    global _session
    if _session is not None:
        _session.close()
        _session = None
