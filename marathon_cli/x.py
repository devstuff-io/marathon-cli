import requests

from marathon_cli.settings import MARATHON_URL, MARATHON_AUTH


def get(uri, params=None, *args, **kwargs):
    if uri.startswith('/'):
        uri = uri[1:]
    if uri.endswith('/'):
        uri = uri[:-1]

    return requests.get(
        MARATHON_URL + uri,
        params=params,
        auth=MARATHON_AUTH
    )
