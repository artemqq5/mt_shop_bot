import logging

from aiogram.types import Update
from fastapi import HTTPException, Request

from bot import app, bot, config, dp, i18n_middleware
from bot.domain.handlers import change_lang_handler_
from bot.domain.handlers.admin import main_admin
from bot.domain.handlers.client import main_client
from bot.domain.middlewares.TrackingMiddleware import TrackingMiddleware
from bot.domain.middlewares.UserRegistrationMiddleware import UserRegistrationMiddleware

dp.include_routers(main_client.router, main_admin.router, change_lang_handler_.router)


@app.on_event("startup")
async def on_startup():
    i18n_middleware.setup(dp)
    await i18n_middleware.core.startup()

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(url=config.WEBHOOK_BASE_URL + config.WEBHOOK_PATH, drop_pending_updates=True)

    dp.message.outer_middleware(UserRegistrationMiddleware())  # register if client not registered
    dp.callback_query.outer_middleware(UserRegistrationMiddleware())  # register if client not registered
    dp.message.outer_middleware(TrackingMiddleware())  # tracking
    dp.callback_query.outer_middleware(TrackingMiddleware())  # tracking


@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()
    # await engine.dispose()


@app.post(config.WEBHOOK_PATH)
async def receive_update(request: Request):
    print(request)
    data = await request.json()
    update = Update.model_validate(data)

    try:
        await dp.feed_update(bot, update)
    except Exception as e:
        logging.exception("Exception handled")
        logging.error(e)
        return {"ok": False}

    return {"ok": True}


@app.api_route("/mt-shop-bot/alive", methods=["GET", "POST"])
async def check_alive_bot(request: Request):
    if request.headers.get("X-Auth") != config.SECRET_SERVER_BOT_ALIVE:
        raise HTTPException(status_code=403)
    return {"status": "ok"}
