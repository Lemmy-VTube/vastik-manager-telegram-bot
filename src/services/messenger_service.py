from aiogram import Bot
from aiogram.types import FSInputFile


class Messenger:
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    async def send_message(self, user_id: int, msg: str) -> None:
        await self.bot.send_message(user_id, msg)

    async def send_photo(
        self,
        user_id: int,
        photo: FSInputFile | str,
        caption: str | None = None,
    ) -> None:
        await self.bot.send_photo(user_id, photo=photo, caption=caption)

    async def send_video(
        self,
        user_id: int,
        video: FSInputFile | str,
        caption: str | None = None,
    ) -> None:
        await self.bot.send_video(user_id, video=video, caption=caption)

    async def send_audio(
        self,
        user_id: int,
        audio: FSInputFile | str,
        caption: str | None = None,
    ) -> None:
        await self.bot.send_audio(user_id, audio=audio, caption=caption)

    async def send_document(
        self,
        user_id: int,
        document: FSInputFile | str,
        caption: str | None = None,
    ) -> None:
        await self.bot.send_document(chat_id=user_id, document=document, caption=caption)
