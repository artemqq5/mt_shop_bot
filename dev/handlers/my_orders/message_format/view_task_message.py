def creo_task_view(task) -> str:
    task_message = f"#{task['id']} <b>{task['format']}</b> | <b>{task['type']}</b> | <b>{task['category']}</b>\n\n"
    task_message += f"<b>desc:</b> {task['description']}\n\n"
    task_message += f"<b>geo:</b> {task['geo']}\n"
    task_message += f"<b>language:</b> {task['language']}\n"
    task_message += f"<b>currency:</b> {task['currency']}\n"
    task_message += f"<b>format_res:</b> {task['format_res']}\n"
    task_message += f"<b>offer:</b> {task['offer']}\n"
    task_message += f"<b>voice:</b> {task['voice']}\n"
    task_message += f"<b>source:</b> {task['source']}\n\n"
    task_message += f"<b>dropbox:</b> {task['dropbox']}\n"

    return task_message


def account_task_view(task) -> str:
    task_message = f"#{task['id']} <b>{task['name']}</b> | <b>{task['type']}</b>\n\n"
    task_message += f"<b>desc:</b> {task['desc']}\n\n"
    task_message += f"<b>geo:</b> {task['geo']}\n"
    task_message += f"<b>count:</b> {task['count']}\n"
    task_message += f"<b>second desc:</b> {task['desc_from_user']}\n\n"

    return task_message
