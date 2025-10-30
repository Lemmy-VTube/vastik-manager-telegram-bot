from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware

from src.services.redis_service import redis_service
from src.utils.i18n_aiogram import i18n


class I18nMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any],
    ) -> Any:
        user = getattr(event, "from_user", None)
        if not user:
            return await handler(event, data)
        lang = await redis_service.get_user_lang(user.id)
        if not lang:
            if user.language_code and user.language_code[:2] in i18n.available_locales:
                lang = user.language_code[:2]
            else:
                lang = i18n.default_locale
            await redis_service.set_user_lang(user.id, lang)
        with i18n.use_locale(lang):
            return await handler(event, data)
