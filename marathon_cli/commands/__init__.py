from pretty_json import format_json

from marathon_cli.utils import pickle_object
from marathon_cli.x import get


def get_request(ctx, uri, pickle_it, with_version=True):
    """Send GET request to Marathon instance.

    .. versionadded:: 1.1.8

    """
    response = get(uri, with_version=with_version)
    ctx.obj['logger'].debug({
        'connection.config': response.connection.config,
        'elapsed': str(response.elapsed),
        'encoding': response.encoding,
        'headers': dict((k, v) for k, v in response.headers.iteritems()),
        'status_code': response.status_code,
        'url': response.url,
    })

    if pickle_it:
        pickle_object(response, uri.replace('/', '-'))

    try:
        return format_json(response.json())
    except:
        return response.text
