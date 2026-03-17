from .session import get_session


def get_from_github_no_auth_api(url):
    """ """
    return get_session().get(url, timeout=10)
