class Dispatcher:

    def __init__(self, app):
        self.app = app

    async def dispatch(self, context):

        if self.app._message_handler is None:
            return

        await self.app._message_handler(
            context,
        )
