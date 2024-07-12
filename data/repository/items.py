from data.database import MyDataBase


class ItemRepository(MyDataBase):

    def item(self, item_id):
        query = "SELECT * FROM `items` WHERE `id` = %s;"
        return self._select_one(query, (item_id,))

    def add(self, title, desc, category, cost):
        query = "INSERT INTO `items` (`title`, `desc`, `category`, `cost`) VALUES(%s, %s, %s, %s);"
        return self._insert(query, (title, desc, category, cost))

    def delete(self, item_id):
        query = "DELETE FROM `items` WHERE `id` = %s;"
        return self._delete(query, (item_id,))

    def items_by_category(self, category):
        query = "SELECT * FROM `items` WHERE `category` = %s ORDER BY `id` DESC;"
        return self._select(query, (category,))

    def delete_by_category(self, category):
        query = "DELETE FROM `items` WHERE `category` = %s;"
        return self._delete(query, (category,))

    def update_visibility(self, item_id, visibility):
        query = "UPDATE `items` SET `visibility` = %s WHERE `id` = %s;"
        return self._update(query, (visibility, item_id))

