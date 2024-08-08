from telegram_bot import start_telegram_bot
import asyncio

async def main() -> None:
    await start_telegram_bot()

if __name__ == '__main__':
    asyncio.run(main())
        