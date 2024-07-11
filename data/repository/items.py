from data.database import MyDataBase


class ItemRepository(MyDataBase):

    def add(self, title, desc, category, cost):
        query = "INSERT INTO `items` (`title`, `desc`, `category`, `cost`) VALUES(%s, %s, %s, %s);"
        return self._insert(query, (title, desc, category, cost))

    def items_by_category(self, category):
        query = "SELECT * FROM `items` WHERE `category` = %s;"
        return self._select(query, (category,))
