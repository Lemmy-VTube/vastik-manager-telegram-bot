from aiogram.types import InlineKeyboardMarkup

from src.config import config
from src.services.i18n_service import i18n_manager
from src.utils.i18n_aiogram import gettext as _
from src.utils.keyboards.builders import keyboard_builder


def change_language_keyboard() -> InlineKeyboardMarkup:
    languages = i18n_manager.get_languages()
    return keyboard_builder.inline(
        text=[
            _(f"button_language_{lang}")
            for lang in languages
        ] + [_("button_back_to_old_version")],
        callback_data=[f"change_language_{lang}" for lang in languages] + ["old_version_menu"]
    )


def main_menu_keyboard() -> InlineKeyboardMarkup:
    return keyboard_builder.inline(
        text=[_("button_open_app"), _("button_old_version")],
        callback_data=[None, "old_version_menu"], # type: ignore
        web_app=[config.WEBAPP_URL.get_secret_value()],
        sizes=1
    )


def old_version_keyboard() -> InlineKeyboardMarkup:
    return keyboard_builder.inline(
        text=[
            _("button_information"), _("button_tepropose_ideast"), _("button_links"),
            _("button_references"), _("button_ent_personage"), _("command_schedule"),
            _("command_language"), _("button_back_to_main_menu")
        ],
        callback_data=[
            "information", "tepropose_ideast", "links", "references",
            "ent_personage", "schedule", "change_language", "main_menu"
        ],
        sizes=[1,1,2]
    )


def back_to_main_menu_keyboard() -> InlineKeyboardMarkup:
    return keyboard_builder.inline(
        text=[_("button_back_to_main_menu")],
        callback_data=["main_menu"]
    )


def back_to_old_version_keyboard() -> InlineKeyboardMarkup:
    return keyboard_builder.inline(
        text=[_("button_back_to_old_version")],
        callback_data=["old_version_menu"]
    )


def admin_menu_keyboard() -> InlineKeyboardMarkup:
    return keyboard_builder.inline(
        text=[_("button_open_admin")],
        web_app=[config.WEBAPP_URL_ADMIN.get_secret_value()],
    )


def watch_on_twitch_keyboard(user_name: str) -> InlineKeyboardMarkup:
    return keyboard_builder.inline(
        text=[_("button_watch_on_twitch")],
        url=[f"https://twitch.tv/{user_name}"],
        sizes=1
    )