from dataclasses import dataclass, field


@dataclass(slots=True)
class Message:
    id: str
    text: str | None = None
    attachments: list = field(default_factory=list)
    extra: dict = field(default_factory=dict)
