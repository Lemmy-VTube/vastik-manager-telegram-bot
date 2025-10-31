from aiogram import F, Router
from aiogram.types import CallbackQuery

from src.services.redis_service import redis_service
from src.utils.i18n_aiogram import gettext as _
from src.utils.i18n_aiogram import i18n
from src.utils.keyboards.inline import back_to_main_menu_keyboard

router = Router()


@router.callback_query(F.data.startswith("change_language_"))
async def call_change_language(callback: CallbackQuery):
    lang = callback.data.split("_")[-1]

    if lang not in i18n.available_locales:
        return await callback.answer(_("message_language_not_supported"), show_alert=True)

    i18n.current_locale = lang
    lang_name = _(f"button_language_{lang}")
    text = _("message_change_language_success").format(lang=lang_name)

    await redis_service.set_user_lang(callback.from_user.id, lang)
    await callback.message.edit_caption(
        caption=text,
        reply_markup=back_to_main_menu_keyboard()
    )
    await callback.answer()