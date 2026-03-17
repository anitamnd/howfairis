from .session import get_session


def get_from_gitlab_no_auth_raw(url):
    """ """
    return get_session().get(url, timeout=10)
