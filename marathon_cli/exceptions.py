from click.exceptions import ClickException


class MissingEnvironmentVariable(ClickException):
    """Raised when a required environment variable is not set..

    .. versionadded:: 1.0.3

    """

    def __init__(self, missing_var):
        message = 'MissingEnvironmentVariable: %s' % missing_var
        super(MissingEnvironmentVariable, self).__init__(message)
