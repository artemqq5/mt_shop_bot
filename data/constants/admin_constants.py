# admin menu ----------------------------------------
# orders
ALL_ORDERS = "Посмотреть заказы"
ALL_ORDERS_LABEL = "Заказы"
# sub category orders
REVIEW_ORDERS = "Заказы на рассмотрении"
ACTIVE_ORDERS = "Активные заказы"
COMPLETED_ORDERS = "Выполненные заказы"
CANCELED_ORDERS = "Отмененные заказы"

ORDERS_IS_EMPTY = "Нет заказов"

ORDER_TYPES_LIST = (REVIEW_ORDERS, ACTIVE_ORDERS, COMPLETED_ORDERS, CANCELED_ORDERS)
# for orders
CHANGE_STATUS_ORDER = "Изменить статус заказа"
STATUS_NOT_EXCHANGE = "Не удалось изменить статус заказа"
STATUS_SUCCESFULY_EXCHANGE = "Статус заказа успешно изменен"
# status
REVIEW = "review"
ACTIVE = "active"
COMPLETED = "completed"
CANCELED = "canceled"

# status_item
HIDE_STATE = "hide"
OPEN_STATE = "open"

# table type orders
CREO_TYPE = "creo"
ACCOUNT_TYPE = "account"

# order managment
SET_ACTIVE_STATUS = "Активно"
SET_REVIEW_STATUS = "На рассмотрении"
SET_COMAPLETED_STATUS = "Выполненно"
SET_CANCELED_STATUS = "Отменено"

ORDER_STATUS_LIST = {SET_ACTIVE_STATUS: ACTIVE, SET_REVIEW_STATUS: REVIEW, SET_COMAPLETED_STATUS: COMPLETED,
                     SET_CANCELED_STATUS: CANCELED}

# TRELLO ========================================
SEND_TASK_TO_TRELLO = "Отправить таск в трелло"
TRELLO_ = "trello"
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
LIST_OF_ITEMS_TYPE = (ACCOUNT_ITEM, )
