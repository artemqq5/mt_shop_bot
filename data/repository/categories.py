from data.database import MyDataBase


class CategoryRepository(MyDataBase):

    def categories(self):
        query = "SELECT * FROM `categories` ORDER BY `date` DESC;"
        return self._select(query)

    def add(self, name):
        query = "INSERT INTO `categories` (`name`) VALUES (%s);"
        return self._insert(query, (name,))
