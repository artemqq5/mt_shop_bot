from mixpanel import Mixpanel

from bot.config import MIXPANEL_TOKEN

mp = Mixpanel(MIXPANEL_TOKEN)


def track_event(user_id: int, event: str, props: dict = None):
    mp.track(distinct_id=str(user_id), event_name=event, properties=props or {})


def set_user_profile(user_id: int, user_props: dict):
    mp.people_set(distinct_id=str(user_id), properties=user_props)
