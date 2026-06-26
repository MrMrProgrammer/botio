from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from botio.models.update import Update
from botio.responses import Response

if TYPE_CHECKING:
    from botio.context import Context


class BaseAdapter(ABC):

    @abstractmethod
    async def parse_update(self, payload) -> Update:
        """Convert platform payload to BotKit Update."""
        raise NotImplementedError

    @abstractmethod
    async def send_response(
        self,
        context: Context,
        response: Response,
    ) -> None:
        """Send response to platform."""
        raise NotImplementedError
