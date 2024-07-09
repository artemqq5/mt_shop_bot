from data.database import MyDataBase


class CategoryRepository(MyDataBase):

    def categories(self):
        query = "SELECT * FROM `category_items`;"
        return self._select(query)

    def add(self, name):
        query = "INSERT INTO `category_items` (`name`) VALUES (%s);"
        return self._insert(query, (name,))
