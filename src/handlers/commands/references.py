from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile, Message

from src.config import IMAGES_DIR
from src.utils.i18n_aiogram import gettext as _
from src.utils.keyboards.inline import back_to_old_version_keyboard

router = Router()


@router.message(Command("references"))
@router.callback_query(F.data == "references")
async def cmd_references(message: Message | CallbackQuery, state: FSMContext) -> None | bool:
    await state.clear()

    photo = FSInputFile(IMAGES_DIR / "old_version.jpg")
    caption = _("message_not_supported_references_old_version")
    
    if isinstance(message, CallbackQuery):
        await message.message.edit_caption( # type: ignore
            caption=caption,
            reply_markup=back_to_old_version_keyboard()
        )
        return await message.answer()
    await message.reply_photo(photo, caption=caption, reply_markup=back_to_old_version_keyboard())
