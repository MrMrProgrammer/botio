from dataclasses import dataclass, field


@dataclass(slots=True)
class Chat:
    id: str
    type: str = "private"
    title: str | None = None
    extra: dict = field(default_factory=dict)
