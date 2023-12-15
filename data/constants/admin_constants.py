# admin menu ----------------------------------------
# orders
from data.constants.accounts_constants import ACCOUNTS
from data.constants.design_constants import DESIGN

ALL_ORDERS = "Посмотреть заказы"
STATUS_OF_ORDERS = "Статус заказов"
# sub category orders
REVIEW_ORDERS = "Заказы на рассмотрении"
ACTIVE_ORDERS = "Активные заказы"
ON_APPROVE_ORDERS = "Ждет апрува"
COMPLETED_ORDERS = "Выполненные заказы"
CANCELED_ORDERS = "Отмененные заказы"

ORDERS_IS_EMPTY = "Нет заказов"

TYPE_OF_ORDERS = (ACCOUNTS, DESIGN)
CHOICE_TYPE_OF_ORDERS = "Выбирите тип заказов"

ORDER_TYPES_LIST = (REVIEW_ORDERS, ACTIVE_ORDERS, ON_APPROVE_ORDERS, COMPLETED_ORDERS, CANCELED_ORDERS)
# for orders
CHANGE_STATUS_ORDER = "Изменить статус заказа"
STATUS_NOT_EXCHANGE = "Не удалось изменить статус заказа"
STATUS_SUCCESFULY_EXCHANGE = "Статус заказа успешно изменен"
REFINEMENT_SUCCESFULY_SEND = "Правки успешно отправлены"
# status
REVIEW = "review"
ACTIVE = "active"
ON_APPROVE = "on_approve"
COMPLETED = "completed"
CANCELED = "canceled"

# status_item
HIDE_STATE = "hide"
OPEN_STATE = "open"

# table type orders
CREO_TYPE = "creo"
ACCOUNT_TYPE = "account"

# order managment
SET_REVIEW_STATUS = "На рассмотрении"
SET_ACTIVE_STATUS = "Активно"
SET_COMAPLETED_STATUS = "Выполненно"
SET_CANCELED_STATUS = "Отменено"

ORDER_STATUS_LIST = {SET_ACTIVE_STATUS: ACTIVE, SET_REVIEW_STATUS: REVIEW, SET_COMAPLETED_STATUS: COMPLETED,
                     SET_CANCELED_STATUS: CANCELED}

# TRELLO ========================================
SEND_TASK_TO_TRELLO = "Отправить таск в трелло"
TRELLO_ = "trellomng"

SEND_COMMENT_TO_TRELLO = "Отправить прави в трелло"
COMMENT_TO_REFINEMENT = "Напишите что необходимо изменить"

COMMENT_AND_REFINEMENT = "Внести правки"
REFINEMENT_ = "refinement"

TASK_NOT_IN_REVIEW = "Задание не на review, измените статус чтобы отправить таск"
TASK_SUCCESFUL_SEND = "Заказ успешно отправлен"
TASK_FAIL_SEND = "Не удалось отправить заказ"

# ADD ITEMS =========================
ADD_ITEMS = "Добавить товары"
SUCCSESFULL_ADDED = "Товар добавлен"
FAIL_ADDED = "Не вышло добавить товар"
CHOICE_TYPE_OF_ADD = "Выберите что хотите добавить"

# SHOW ITEMS =========================
SHOW_ITEMS = "Список товаров"
CHOICE_TYPE_OF_SHOW = "Выберите категорию товаров для просмотра"

# Manage Items ========
HIDE_ITEM = "Скрыть позицию"
OPEN_ITEM = "Показать позицию"
SUCCESULL_UPDATE_VISIBILITY = "Видимость товара обновлена"
FAIL_UPDATE_VISIBILITY = "Не вышло обновить видимость товара"

# ITEMS TYPE ============================
ACCOUNT_ITEM = "Аккаунты"
LIST_OF_ITEMS_TYPE = (ACCOUNT_ITEM,)

# PUSH NOTIFYCATION ===========================
PUSH_NOTIFICATION = "Отправить сообщение"
TYPE_PUSH = "Выбирите тип сообщений"
PUSH_ALL_CLIENTS = "Сообщение всем клиентам"
PUSH_INDIVIDUAL = "Индивидуальное оповещение"
PUSH_TYPE_LIST = (PUSH_INDIVIDUAL, PUSH_ALL_CLIENTS)

SET_USER_TO_PUSH = "Укажите telegram id пользователя:"
SET_MESSAGE_TO_PUSH = "Ваше сообщение:"

PUSH_HAVE_SENT = "Сообщение доставлено"
PUSH_HAVE_NOT_SENT = "Сообщение не доставлено"
PUSH_HAVE_SENT_ALL = lambda total, succesful: "Сообщение доставлено {0} из {1}".format(succesful, total)
PUSH_ERROR_SENT_USER_NOT_EXIST = "Пользователя не существует"
PUSH_ERROR_SENT_USER_NOT_START_BOT = "Пользователь не запустил бота или заблокировал его"
