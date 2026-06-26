from botio.adapters.telegram import TelegramAdapter


class AdapterFactory:

    @staticmethod
    def create(
        platform: str,
        token: str,
    ):
        if platform == "telegram":
            return TelegramAdapter(token)

        raise ValueError(
            f"Unsupported platform: {platform}"
        )
