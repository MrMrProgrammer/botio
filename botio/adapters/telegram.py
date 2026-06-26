import httpx

from botio.adapters.base import BaseAdapter
from botio.models.chat import Chat
from botio.models.message import Message
from botio.models.update import Update
from botio.models.user import User
from botio.responses import Response, TextResponse


class TelegramAdapter(BaseAdapter):

    def __init__(
        self,
        token: str,
    ):
        self.token = token

    async def parse_update(
        self,
        payload: dict,
    ) -> Update:

        message = payload["message"]

        return Update(
            id=str(payload["update_id"]),
            platform="telegram",
            user=User(
                id=str(message["from"]["id"]),
                name=message["from"].get(
                    "first_name"
                ),
                username=message["from"].get(
                    "username"
                ),
            ),
            chat=Chat(
                id=str(message["chat"]["id"]),
                type=message["chat"].get(
                    "type",
                    "private",
                ),
            ),
            message=Message(
                id=str(message["message_id"]),
                text=message.get("text"),
            ),
        )

    async def send_response(
        self,
        context,
        response: Response,
    ) -> None:

        if not isinstance(
            response,
            TextResponse,
        ):
            return

        async with httpx.AsyncClient() as client:

            await client.post(
                f"https://api.telegram.org/bot{self.token}/sendMessage",
                json={
                    "chat_id": context.chat.id,
                    "text": response.text,
                },
            )

    async def handle_webhook(
        self,
        payload,
        app,
    ):

        update = await self.parse_update(
            payload,
        )

        await app.handle(
            update,
            self,
        )
