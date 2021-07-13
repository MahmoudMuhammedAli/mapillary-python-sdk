# -*- coding: utf-8 -*-

"""
mapillary.models.exceptions

This module contains the set of Mapillary's exceptions
"""


class MapillaryException(Exception):
    """Base class for exceptions in this module"""

    pass


class InvalidTokenError(MapillaryException):
    """Raised when an invalid token is given
    to access Mapillary's API, primarily used in mapillary.set_access_token

    :var message: The error message returned
    :var type: The type of error that occurred
    :var code: The error code returned,
    most like 190, "Access token has expired",
    see
    https://developers.facebook.com/docs/graph-api/using-graph-api/error-handling/
    for more information
    :fbtrace_id: A unique ID to track the issue/exception
    """

    def __init__(self, message, type, code, fbtrace_id):
        """ """
        self.message = message
        self.type = type
        self.code = code
        self.fbtrace_id = fbtrace_id

    def __str__(self):
        return f"{self.message}"

    def __repr__(self):
        return (
            "InvalidTokenError: An exception occured."
            + f'Message: "{self.message}", Type: "{self.type}",'
            + f'Code: "{self.code}",'
            + f'fbtrace_id: "{self.fbtrace_id}"'
        )


class InvalidFieldError(MapillaryException):
    """Raised when an API endpoint is passed invalid
    field elements
    :var endpoint: The API endpoint that was targeted
    :var field: The invalid field that was passed
    """

    def __init__(
        self,
        endpoint: str,
        field: str,
    ):
        """Initializing InvalidFieldError constructor"""
        self.endpoint = endpoint
        self.field = field

    def __str__(self):
        return (
            f'InvalidFieldError: The invalid field, "{self.field}" was '
            f'passed to the endpoint, "{self.endpoint}"'
        )

    def __repr__(self):
        return (
            f'InvalidFieldError: The invalid field, "{self.field}" was '
            f'passed to the endpoint, "{self.endpoint}"'
        )
