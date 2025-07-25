import logging

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message

from bot.data.tracking.mixpanel import set_user_profile, track_event


class TrackingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        try:
            user = event.from_user
            user_id = user.id

            base_props = {
                "lang": user.language_code,
                "username": user.username or "none",
                "first_name": user.first_name,
            }

            # Встановлення профілю користувача
            try:
                set_user_profile(user_id, base_props)
            except Exception as e:
                logging.warning(f"[Tracking] set_user_profile error for user {user_id}: {e}")

            # Трекінг подій
            if isinstance(event, Message):
                text = event.text or ""
                try:
                    track_event(
                        user_id,
                        "UserMessage",
                        {
                            **base_props,
                            "text": text,
                            "message_type": "command" if text.startswith("/") else "text",
                        },
                    )
                except Exception as e:
                    logging.warning(f"[Tracking] track_event (UserMessage) error for user {user_id}: {e}")

            elif isinstance(event, CallbackQuery):
                try:
                    track_event(
                        user_id,
                        "UserCallback",
                        {
                            **base_props,
                            "callback_data": event.data,
                            "callback_type": event.data.split(":")[0] if ":" in event.data else "raw",
                        },
                    )
                except Exception as e:
                    logging.warning(f"[Tracking] track_event (UserCallback) error for user {user_id}: {e}")

        except Exception as middleware_error:
            logging.exception(f"[TrackingMiddleware] Unexpected error: {middleware_error}")

        return await handler(event, data)
