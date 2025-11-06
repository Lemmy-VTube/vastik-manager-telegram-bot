from logging import getLogger

from aiogram import Bot
from aiogram.types import FSInputFile
from faststream.rabbit import RabbitRouter
from pydantic import BaseModel

from src.config import IMAGES_DIR, config
from src.services.user_service import user_service
from src.utils.keyboards.inline import watch_on_twitch_keyboard

router = RabbitRouter()
logger = getLogger(__name__)


class TwitchStreamEvent(BaseModel):
    event: str
    user_name: str
    title: str | None
    game_name: str | None
    

@router.subscriber("twitch_streams")
async def handle_twitch_stream_event(data: TwitchStreamEvent):
    event = data.event
    user_name = data.user_name
    reply_markup = None
    if event == "stream_online":
        title = data.title
        game_name = data.game_name
        message = (
            f"🎬 {user_name} запустила стрим!\n"
            f"Название стримчика: {title}\n"
            f"Играет в {game_name}\n"
            f"Смотреть: twitch.tv/{user_name}"
        )
        reply_markup = watch_on_twitch_keyboard(user_name)
    elif event == "stream_offline":
        message = (
            f"🛑 {user_name} завершил стрим.\n"
            f"Канал: twitch.tv/{user_name}"
        )
    else:
        return

    bot = Bot(token=config.TOKEN_BOT.get_secret_value())
    try:
        offset = 0
        page_size = 200
        while True:
            users = await user_service.get_all_users(limit=page_size, offset=offset)
            if not users:
                break

            for user in users:
                try:
                    await bot.send_photo(
                        chat_id=user.tg_id,
                        photo=FSInputFile(IMAGES_DIR / "hello.jpg"),
                        caption=message,
                        reply_markup=reply_markup
                    )
                except Exception as e:
                    logger.warning(f"Failed to send stream notification to {user.tg_id}: {e}")

            if len(users) < page_size:
                break
            offset += page_size
    finally:
        await bot.session.close()
    