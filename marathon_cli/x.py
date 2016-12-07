import requests

from marathon_cli.exceptions import MethodNotSupported
from marathon_cli.settings import MARATHON_AUTH, MARATHON_URL, MARATHON_VERSION


def build_url(uri, with_version=True):
    url = MARATHON_URL
    if with_version:
        url += MARATHON_VERSION
    return url + uri


def clean_uri(uri):
    uri.replace('//', '/')
    if uri.startswith('/'):
        uri = uri[1:]
    if uri.endswith('/'):
        uri = uri[:-1]
    return uri


def get(uri, with_version=True, *args, **kwargs):
    uri = clean_uri(uri)
    return requests.get(
        build_url(uri, with_version),
        auth=MARATHON_AUTH,
        **kwargs
    )


def delete(uri, with_version=True, *args, **kwargs):
    uri = clean_uri(uri)
    return requests.delete(
        build_url(uri, with_version),
        auth=MARATHON_AUTH,
        **kwargs
    )


def post(uri, with_version=True, *args, **kwargs):
    uri = clean_uri(uri)
    return requests.post(
        build_url(uri, with_version),
        auth=MARATHON_AUTH,
        **kwargs
    )


def put(uri, with_version=True, *args, **kwargs):
    uri = clean_uri(uri)
    return requests.put(
        build_url(uri, with_version),
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
