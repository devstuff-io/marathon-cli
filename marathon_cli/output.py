try:
    import simplejson as json
except ImportError:
    import json

from datetime import datetime

from pygments import highlight
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.styles import get_all_styles
from pygson.json_lexer import JSONLexer

from marathon_cli.settings import MARATHON_STYLE

AVAILABLE_STYLES = list(get_all_styles())


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code

    :param obj: **required**. Ensures obj can be json serializable.
    """
    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial


def jdump(obj, *args, **kwargs):
    return json.dumps(obj, default=json_serial, **kwargs)


def pretty_print(obj, sort_keys=True, indent=4, separators=(',', ': ')):
    """Pretty prints json object.

    :param obj: **required**. The json.
    :type obj: dict/json.
    :param sort_keys: Sort the keys.
    :type sort_keys: bool.
    :param indent: Indent each depth by n * int.
    :type indent: int.
    :param separators: element separators
    :type separators: set.
    :return: str
    """
    return jdump(obj, sort_keys=sort_keys, indent=indent, separators=separators)


def format_json(content, style=MARATHON_STYLE):
    """Prettify JSON.

    :param content: **required**.
    :type content: json.
    """
    return highlight(
        pretty_print(content, sort_keys=False),
        JSONLexer(),
        Terminal256Formatter(style=style)
    ).strip()
