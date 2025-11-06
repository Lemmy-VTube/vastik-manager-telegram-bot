from datetime import datetime

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto, Message

from src.config import IMAGES_DIR, config
from src.schemas import UserCreate
from src.services.user_service import user_service
from src.utils.i18n_aiogram import gettext as _
from src.utils.keyboards.inline import main_menu_keyboard

router = Router()


@router.message(CommandStart())
@router.callback_query(F.data == "main_menu")
async def cmd_start(message: Message | CallbackQuery, state: FSMContext) -> None | bool:
    await state.clear()

    tg_id = message.from_user.id # type: ignore
    username = message.from_user.username # type: ignore
    first_name = message.from_user.first_name  # type: ignore
    last_name = message.from_user.last_name  # type: ignore 
    full_name = message.from_user.mention_html(  # type: ignore
        f"{first_name} {last_name}"
        if last_name else first_name
    )

    photo_url = None
    try:
        photos = await message.bot.get_user_profile_photos(tg_id, limit=1) # type: ignore
        if photos.total_count > 0:
            token = config.TOKEN_BOT.get_secret_value()
            file_id = photos.photos[0][-1].file_id
            file_info = await message.bot.get_file(file_id) # type: ignore
            photo_url = f"https://api.telegram.org/file/bot{token}/{file_info.file_path}"
    except Exception:
        photo_url = None

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

    await user_service.create_user(
        UserCreate(
            tg_id=tg_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            photo_url=photo_url
        )
    )
    if isinstance(message, CallbackQuery):
        await message.message.edit_media( # type: ignore
            media=InputMediaPhoto(media=photo, caption=msg),
            reply_markup=main_menu_keyboard()
        )
        return await message.answer()
    await message.answer_sticker(FSInputFile(IMAGES_DIR / "heart.webm"))
    await message.reply_photo(photo=photo, caption=msg, reply_markup=main_menu_keyboard())