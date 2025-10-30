from argparse import ArgumentParser
from logging import getLogger

from src.config import BABEL_CONFIG_FILE
from src.utils.command_runner import run_command
from src.utils.logger import setup_logging

logger = getLogger(__name__)


def main() -> None:
    setup_logging()
    
    parser = ArgumentParser(description="Babel locale tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_init = subparsers.add_parser("init", help="Initialize locale (babel)")
    parser_init.add_argument("locale", help="Language code, e.g.: ru, en")

    subparsers.add_parser("update", help="Update .po from source files")
    subparsers.add_parser("compile", help="Compile .mo from .po files")
    subparsers.add_parser("update-compile", help="Update and compile translations")

    args = parser.parse_args()

    if not BABEL_CONFIG_FILE.exists():
        raise FileNotFoundError(f"babel.cfg file not found at: {BABEL_CONFIG_FILE}")

    if args.command == "init":
        locale = args.locale
        logger.info(f"Initializing locale: {locale}")
        cmd_extract = "pybabel extract -F babel.cfg -o locales/messages.pot ."
        ok, out = run_command(cmd_extract)
        if not ok:
            return logger.error("Extract failed")

        cmd_init = f"pybabel init -i locales/messages.pot -d locales -l {locale}"
        ok, out = run_command(cmd_init)
        if not ok:
            return logger.error("Init failed")

        cmd_compile = "pybabel compile -d locales"
        ok, out = run_command(cmd_compile)
        if not ok:
            return logger.error("Compile failed")

        logger.info("Locale initialized and compiled")

    elif args.command == "update":
        logger.info("Updating translations from source files")
        cmd_extract = "pybabel extract -F babel.cfg -o locales/messages.pot ."
        ok, out = run_command(cmd_extract)
        if not ok:
            return logger.error("Extract failed")

        cmd_update = "pybabel update -i locales/messages.pot -d locales"
        ok, out = run_command(cmd_update)
        if not ok:
            return logger.error("Update failed")

        logger.info("PO files updated. Don\"t forget to translate new strings.")

    elif args.command == "compile":
        logger.info("Compiling translation files (.mo)")
        cmd_compile = "pybabel compile -d locales"
        ok, out = run_command(cmd_compile)
        if not ok:
            return logger.error("Compile failed")
        logger.info("Translations compiled successfully")

    elif args.command == "update-compile":
        logger.info("Updating and compiling translations")
        cmd_extract = "pybabel extract -F babel.cfg -o locales/messages.pot ."
        ok, out = run_command(cmd_extract)
        if not ok:
            return logger.error("Extract failed")

        cmd_update = "pybabel update -i locales/messages.pot -d locales"
        ok, out = run_command(cmd_update)
        if not ok:
            return logger.error("Update failed")

        logger.info("PO files updated")
        cmd_compile = "pybabel compile -d locales"
        ok, out = run_command(cmd_compile)
        if not ok:
            return logger.error("Compile failed")

        logger.info("Translations updated and compiled successfully")


if __name__ == "__main__":
    main()


