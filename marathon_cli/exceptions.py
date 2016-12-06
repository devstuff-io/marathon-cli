from click.exceptions import ClickException


class MissingEnvironmentVariable(ClickException):
    """Raised when a required environment variable is not set..

    .. versionadded:: 1.0.3

    """

    def __init__(self, missing_var):
        message = 'MissingEnvironmentVariable: %s' % missing_var
        super(MissingEnvironmentVariable, self).__init__(message)


class MethodNotSupported(ClickException):
    """Raised when an invalid http method is requested.

    .. versionadded:: 1.1.7

    """

    def __init__(self, method):
        message = 'MethodNotSupported: %s' % method
        super(MethodNotSupported, self).__init__(message)
