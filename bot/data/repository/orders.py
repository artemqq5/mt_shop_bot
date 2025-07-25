from bot.data.database import MyDataBase


class OrderRepository(MyDataBase):

    def orders(self):
        query = "SELECT * FROM `orders` ORDER BY `date` DESC;"
        return self._select(query)

    def orders_by_user_id(self, user_id):
        query = "SELECT * FROM `orders` WHERE `user_id` = %s ORDER BY `date` DESC;"
        return self._select(query, (user_id,))

    def order(self, order_id):
        query = "SELECT * FROM `orders` WHERE `id` = %s;"
        return self._select_one(query, (order_id,))

    def order_by_identify(self, identify):
        query = "SELECT * FROM `orders` WHERE `identify` = %s;"
        return self._select_one(query, (identify,))

    def add(self, user_id, category, item_id, item_title, desc, count, total_cost, identify):
        query = "INSERT INTO `orders` (`user_id`, `category`, `item_id`, `item_title`, `desc`, `count`, `total_cost`, `identify`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        return self._insert(query, (user_id, category, item_id, item_title, desc, count, total_cost, identify))

    def last_order_id(self):
        query = "SELECT LAST_INSERT_ID() AS last_id;"
        return self._select_one(query)
