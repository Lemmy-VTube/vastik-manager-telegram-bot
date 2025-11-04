from datetime import datetime

from aiogram import F, Router
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto

from src.config import IMAGES_DIR, config
from src.utils.i18n_aiogram import gettext as _
from src.utils.keyboards.inline import old_version_keyboard

router = Router()


@router.callback_query(F.data == "old_version_menu")
async def call_old_version_menu(callback: CallbackQuery):
    first_name = callback.from_user.first_name
    last_name = callback.from_user.last_name
    full_name = callback.from_user.mention_html(
        f"{first_name} {last_name}"
        if last_name else first_name
    )

    today = datetime.now().date()
    birthday_message = ""
    if today.day == 7 and today.month == 10:
        birthday_message = _("message_birthday_lemmy")
    elif today.day == 13 and today.month == 10:
        birthday_message = _("message_birthday_developer")

    photo = FSInputFile(IMAGES_DIR / "old_version.jpg")
    msg = _("message_old_version").format(
        full_name=full_name,
        birthday_message=birthday_message,
        project_version=config.PROJECT_VERSION,
        developer_username=config.DEVELOPER_USERNAME,
    )

    await callback.message.edit_media( # type: ignore
        media=InputMediaPhoto(media=photo, caption=msg),
        reply_markup=old_version_keyboard()
    )
    await callback.answer()