from data.database import MyDataBase


class CategoryRepository(MyDataBase):

    def category(self, name):
        query = "SELECT * FROM `categories` WHERE `name` = %s;"
        return self._select_one(query, (name,))

    def categories(self):
        query = "SELECT * FROM `categories` ORDER BY `date` DESC;"
        return self._select(query)

    def add(self, name):
        query = "INSERT INTO `categories` (`name`) VALUES (%s);"
        return self._insert(query, (name,))
