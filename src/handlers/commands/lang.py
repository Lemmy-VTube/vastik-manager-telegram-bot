from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile, Message

from src.config import IMAGES_DIR
from src.utils.i18n_aiogram import gettext as _
from src.utils.keyboards.inline import change_language_keyboard

router = Router()


@router.message(Command("language"))
@router.callback_query(F.data == "change_language")
async def start_command(message: Message | CallbackQuery, state: FSMContext) -> None | bool:
    await state.clear()
    
    photo = FSInputFile(IMAGES_DIR / "old_version.jpg")
    msg = _("message_choose_language")

    if isinstance(message, CallbackQuery):
        await message.message.edit_caption( # type: ignore
            caption=msg,
            reply_markup=change_language_keyboard()
        )
        return await message.answer()
    await message.reply_photo(photo=photo, caption=msg, reply_markup=change_language_keyboard())
