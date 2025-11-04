from datetime import datetime

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto, Message

from src.config import IMAGES_DIR, config
from src.utils.i18n_aiogram import gettext as _
from src.utils.keyboards.inline import main_menu_keyboard

router = Router()


@router.message(CommandStart())
@router.callback_query(F.data == "main_menu")
async def cmd_start(message: Message | CallbackQuery, state: FSMContext) -> None | bool:
    await state.clear()

    first_name = message.from_user.first_name  # type: ignore
    last_name = message.from_user.last_name  # type: ignore 
    full_name = message.from_user.mention_html(  # type: ignore
        f"{first_name} {last_name}"
        if last_name else first_name
    )

    today = datetime.now().date()
    birthday_message = ""
    if today.day == 7 and today.month == 10:
        birthday_message = _("message_birthday_lemmy")
    elif today.day == 13 and today.month == 10:
        birthday_message = _("message_birthday_developer")

    photo = FSInputFile(IMAGES_DIR / "hello.jpg")
    msg = _("message_welcome").format(
        full_name=full_name,
        birthday_message=birthday_message,
        project_version=config.PROJECT_VERSION,
        developer_username=config.DEVELOPER_USERNAME,
    )

    if isinstance(message, CallbackQuery):
        await message.message.edit_media( # type: ignore
            media=InputMediaPhoto(media=photo, caption=msg),
            reply_markup=main_menu_keyboard()
        )
        return await message.answer()
    await message.answer_sticker(FSInputFile(IMAGES_DIR / "heart.webm"))
    await message.reply_photo(photo=photo, caption=msg, reply_markup=main_menu_keyboard())