from dataclasses import dataclass, field


@dataclass(slots=True)
class User:
    id: str
    name: str | None = None
    username: str | None = None
    language: str | None = None
    extra: dict = field(default_factory=dict)
