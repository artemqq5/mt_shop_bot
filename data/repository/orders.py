from data.database import MyDataBase


class OrderRepository(MyDataBase):

    def orders(self):
        query = "SELECT * FROM `orders` ORDER BY `date` DESC;"
        return self._select(query)

    def order(self, order_id):
        query = "SELECT * FROM `orders` WHERE `id` = %s;"
        return self._select_one(query, (order_id,))

    def add(self, user_id, category, desc, count, total_cost):
        query = "INSERT INTO `orders` (`user_id`, `category`, `desc`, `count`, `total_cost`) VALUES (%s, %s, %s, %s, %s);"
        return self._insert(query, (user_id, category, desc, count, total_cost))

    def last_order_id(self):
        query = "SELECT LAST_INSERT_ID() AS last_id;"
        return self._select_one(query)
