from .session import get_session


def get_from_github_with_auth_api(url, apikeys):
    """ """
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    username = apikeys.get("github-user")
    key = apikeys.get("github-key")

    return get_session().get(url, headers=headers, auth=(username, key), timeout=10)
