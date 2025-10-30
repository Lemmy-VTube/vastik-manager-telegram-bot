from time import time
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

from src.config import config_telegram_bot
from src.services.redis_service import redis_service
from src.utils.i18n_aiogram import gettext as _


class RateLimitMiddleware(BaseMiddleware):
    def __init__(
        self,
        max_requests: int = config_telegram_bot.RATELIMIT_MAX_REQUESTS,
        window_seconds: int = config_telegram_bot.RATELIMIT_WINDOW_SECONDS,
        ban_seconds: int = config_telegram_bot.RATELIMIT_BAN_SECONDS,
    ):
        super().__init__()
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.ban_seconds = ban_seconds

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        if isinstance(event, Message) and event.text and event.text.startswith("/"):
            user_id = event.from_user.id
            now = int(time())
            ban_until = await redis_service.get_ban(f"tg:{user_id}")

            if ban_until and ban_until > now:
                seconds_left = ban_until - now
                return await event.answer(_("message_baned").format(seconds_left=seconds_left))
                
            count = await redis_service.count_requests(f"tg:{user_id}", self.window_seconds)
            await redis_service.add_request(f"tg:{user_id}", self.window_seconds)
            if count + 1 > self.max_requests:
                await redis_service.ban_ip(f"tg:{user_id}", self.ban_seconds)
                await redis_service.clear_requests(f"tg:{user_id}")
                return await event.answer(
                    _("message_limit_exceeded").format(seconds_left=self.ban_seconds)
                )
        return await handler(event, data)
