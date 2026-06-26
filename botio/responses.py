from dataclasses import dataclass


class Response:
    pass


@dataclass(slots=True)
class TextResponse(Response):
    text: str
