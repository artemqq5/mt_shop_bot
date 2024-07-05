def creo_notify_formatted(task, text, user) -> str:
    final_message = f"#{task['id']} <b>{task['format']}</b> | <b>{task['type']}</b> | <b>{task['category']}</b>\n\n"
    final_message += f"<b>message:</b> {text}\n\n"
    final_message += f"<b>username:</b> {user['name']}\n"
    final_message += f"<b>user id:</b> {user['id']}\n"

    return final_message


def account_notify_formatted(task, text, user) -> str:
    final_message = f"#{task['id']} <b>{task['name']}</b> | <b>{task['type']}</b>\n\n"
    final_message += f"<b>message:</b> {text}\n\n"
    final_message += f"<b>username:</b> {user['name']}\n"
    final_message += f"<b>user id:</b> {user['id']}\n"

    return final_message
