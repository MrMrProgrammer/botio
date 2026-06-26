from botio.adapters.factory import AdapterFactory
from botio.context import Context
from botio.dispatcher import Dispatcher


class BotKit:

    def __init__(self):
        self.adapters = {}

        self._message_handler = None

        self.dispatcher = Dispatcher(self)

    def add(
        self,
        platform: str,
        token: str,
    ):
        adapter = AdapterFactory.create(
            platform=platform,
            token=token,
        )

        self.adapters[platform] = adapter

        return self

    def message(self, func):
        self._message_handler = func
        return func

    async def process_update(
        self,
        platform: str,
        payload: dict,
    ):
        adapter = self.adapters[platform]

        update = await adapter.parse_update(
            payload,
        )

        await self.handle(
            update,
            adapter,
        )

    async def handle(
        self,
        update,
        adapter,
    ):
        context = Context(
            update=update,
            adapter=adapter,
            app=self,
        )

        await self.dispatcher.dispatch(
            context,
        )
