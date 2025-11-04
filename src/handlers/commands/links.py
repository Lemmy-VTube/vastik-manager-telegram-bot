from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto, Message

from src.config import IMAGES_DIR
from src.utils.i18n_aiogram import gettext as _
from src.utils.keyboards.inline import back_to_old_version_keyboard

router = Router()


@router.message(Command("links"))
@router.callback_query(F.data == "links")
async def cmd_links(message: Message | CallbackQuery, state: FSMContext) -> None | bool:
    await state.clear()
    
    twitch_link = "https://www.twitch.tv/lemmychka"
    tg_channel_link = "https://t.me/lemmychka"
    tiktok_link = "https://www.tiktok.com/@lemmychka?_t=ZS-908LDeF8Rft&_r=1"
    youtube_link = "https://youtube.com/@lemmychka?si=xB6hp-qtpeLE3VCE"
    public_vk_link = "https://vk.com/lemmychka"
    discord_link = "https://discord.gg/YVDkkZjt"
    dalink_link = "https://dalink.to/lemmychka"

    photo = FSInputFile(IMAGES_DIR / "social.jpg")
    msg = _("message_links").format(
        twitch_link=twitch_link,
        tg_channel_link=tg_channel_link,
        tiktok_link=tiktok_link,
        youtube_link=youtube_link,
        public_vk_link=public_vk_link,
        discord_link=discord_link,
        dalink_link=dalink_link,
    )
    
    if isinstance(message, CallbackQuery):
        await message.message.edit_media( # type: ignore
            media=InputMediaPhoto(media=photo, caption=msg),
            reply_markup=back_to_old_version_keyboard()
        )
        return await message.answer()
    await message.reply_photo(photo, caption=msg, reply_markup=back_to_old_version_keyboard())
