
from dataclasses import dataclass
from rest_framework import status


@dataclass(frozen=True)
class APIBaseException(Exception):
    item: str
    message: str
    status_code: int = status.HTTP_400_BAD_REQUEST

    def error_data(self) -> dict:
        error_data = {"item": self.item, "message": self.message}
        return error_data

    def __str__(self):
        return "{}: {}".format(self.item, self.message)


class Status400Exception(APIBaseException):
    def __init__(self, item, message):
        super().__init__(
            item, message, status_code=status.HTTP_400_BAD_REQUEST
        )

class Status500Exception(APIBaseException):
    def __init__(self, item, message):
        super().__init__(
            item, message, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )