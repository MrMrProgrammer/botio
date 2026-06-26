from botio.responses import Response, TextResponse


class Context:

    def __init__(
        self,
        update,
        adapter,
        app,
    ):
        self.update = update
        self.adapter = adapter
        self.app = app

    @property
    def user(self):
        return self.update.user

    @property
    def chat(self):
        return self.update.chat

    @property
    def message(self):
        return self.update.message

    async def send(
        self,
        response: Response,
    ) -> None:
        await self.adapter.send_response(
            self,
            response,
        )

    async def reply(
        self,
        text: str,
    ) -> None:
        await self.send(
            TextResponse(text=text)
        )
