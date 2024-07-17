from data.database import MyDataBase


class OrderRepository(MyDataBase):

    def orders(self):
        query = "SELECT * FROM `orders` ORDER BY `date` DESC;"
        return self._select(query)

    def order(self, order_id):
        query = "SELECT * FROM `orders` WHERE `id` = %s;"
        return self._select_one(query, (order_id,))
