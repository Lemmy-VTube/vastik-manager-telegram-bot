from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto, Message

from src.config import IMAGES_DIR, config
from src.services.user_service import user_service
from src.utils.i18n_aiogram import gettext as _
from src.utils.keyboards.inline import main_menu_keyboard

router = Router()


@router.message(CommandStart())
@router.callback_query(F.data == "main_menu")
async def cmd_start(message: Message | CallbackQuery, state: FSMContext):
    await state.clear()

    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    full_name = message.from_user.mention_html(
        f"{first_name} {last_name}"
        if last_name else first_name
    )

    photo = FSInputFile(IMAGES_DIR / "hello.jpg")
    msg = _("message_welcome").format(
        full_name=full_name,
        github_url=config.GITHUB_URL,
        project_version=config.PROJECT_VERSION,
        developer_username=config.DEVELOPER_USERNAME,
    )

    await user_service.register_user(user_id)
    if isinstance(message, CallbackQuery):
        await message.message.edit_media(
            media=InputMediaPhoto(media=photo, caption=msg),
            reply_markup=main_menu_keyboard()
        )
        return await message.answer()
    await message.answer_sticker(FSInputFile(IMAGES_DIR / "heart.webp"))
    await message.reply_photo(photo=photo, caption=msg, reply_markup=main_menu_keyboard())