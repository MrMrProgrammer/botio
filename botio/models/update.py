from dataclasses import dataclass

from .chat import Chat
from .message import Message
from .user import User


@dataclass(slots=True)
class Update:
    id: str
    platform: str
    user: User
    chat: Chat
    message: Message
