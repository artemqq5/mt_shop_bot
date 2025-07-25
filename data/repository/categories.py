from data.database import MyDataBase


class CategoryRepository(MyDataBase):

    def category(self, name):
        query = "SELECT * FROM `categories` WHERE `name` = %s AND `visibility` = '1';"
        return self._select_one(query, (name,))

    def category_all(self, name):
        query = "SELECT * FROM `categories` WHERE `name` = %s;"
        return self._select_one(query, (name,))

    def categories(self):
        query = "SELECT * FROM `categories` WHERE `visibility` = '1' ORDER BY `date` DESC;"
        return self._select(query)

    def categories_all(self):
        query = "SELECT * FROM `categories` ORDER BY `date` DESC;"
        return self._select(query)

    def add(self, name):
        query = "INSERT INTO `categories` (`name`) VALUES (%s);"
        return self._insert(query, (name,))

    def delete(self, name):
        query = "DELETE FROM `categories` WHERE `name` = %s;"
        return self._delete(query, (name,))

    def update_visibility(self, name, visibility):
        query = "UPDATE `categories` SET `visibility` = %s WHERE `name` = %s;"
        return self._update(query, (visibility, name))
