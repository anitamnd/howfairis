from backoff import expo
from backoff import on_exception
from ratelimit import RateLimitException
from ratelimit import limits
from .session import get_session


# https://docs.gitlab.com/ee/user/gitlab_com/index.html#gitlabcom-specific-rate-limits
@on_exception(expo, RateLimitException, max_tries=8)
@limits(calls=2000, period=60)
def get_from_gitlab_with_auth_api(url, apikeys):
    """ """
    headers = {
        "Accept": "application/json"
    }

    username = apikeys.get("gitlab-user")
    key = apikeys.get("gitlab-key")

    return get_session().get(url, headers=headers, auth=(username, key), timeout=10)
