import requests

from marathon_cli.exceptions import MethodNotSupported
from marathon_cli.settings import MARATHON_URL, MARATHON_AUTH


def clean_uri(uri):
    if uri.startswith('/'):
        uri = uri[1:]
    if uri.endswith('/'):
        uri = uri[:-1]
    return uri


def get(uri, *args, **kwargs):
    uri = clean_uri(uri)
    return requests.get(
        MARATHON_URL + uri,
        auth=MARATHON_AUTH,
        **kwargs
    )


def delete(uri, *args, **kwargs):
    uri = clean_uri(uri)
    return requests.delete(
        MARATHON_URL + uri,
        auth=MARATHON_AUTH,
        **kwargs
    )


def post(uri, *args, **kwargs):
    uri = clean_uri(uri)
    return requests.post(
        MARATHON_URL + uri,
        auth=MARATHON_AUTH,
        **kwargs
    )


def put(uri, *args, **kwargs):
    uri = clean_uri(uri)
    return requests.put(
        MARATHON_URL + uri,
        auth=MARATHON_AUTH,
        **kwargs
    )


def get_method(name):
    if name.lower() == 'get':
        return get
    if name.lower() == 'delete':
        return delete
    if name.lower() == 'post':
        return post
    if name.lower() == 'put':
        return put
    raise MethodNotSupported(name)
