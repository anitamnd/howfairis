from .session import get_session


def get_from_gitlab_no_auth_api(url):
    """ """
    headers = {
        "Accept": "application/json"
    }

    return get_session().get(url, headers=headers, timeout=10)
