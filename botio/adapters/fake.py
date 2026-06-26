from botio.adapters.base import BaseAdapter
from botio.models.update import Update
from botio.responses import Response, TextResponse


class FakeAdapter(BaseAdapter):

    async def parse_update(
        self,
        payload,
    ) -> Update:
        return payload

    async def send_response(
        self,
        context,
        response: Response,
    ) -> None:

        if isinstance(response, TextResponse):
            print(f">>> {response.text}")
            return

        raise NotImplementedError(
            f"Unsupported response type: {type(response).__name__}"
        )
