from trello_mng.send_task import TrelloCard


def parse_to_trello_card_format(task_creo, user):

    desk = ""

    for i in task_creo:
        if i not in ('id', ):
            if task_creo[i] is not None:
                desk += f"{i}: {task_creo[i]}\n"

    desk += "\n"
    desk += f"username: @{user['name']}\n"
    desk += f"telegram id: {user['id']}\n"

    trello_card = TrelloCard(
        name=f"#{task_creo['id']} {task_creo['category']} | {task_creo['format']}",
        desc=desk,
        date=task_creo['deadline']
    )

    return trello_card
