from telegram.ext import Application

from src.bot.core.settings import settings
from src.bot.handlers import main_handler


def main() -> None:
    """Initialize a Telegram bot application with a main handler."""
    application = Application.builder().token(settings.telegram_token).build()
    application.add_handler(main_handler)
    application.run_polling()


if __name__ == "__main__":
    main()
