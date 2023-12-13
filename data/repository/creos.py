from data.database import MyDataBase


class CreosRepository(MyDataBase):

    def get_creo(self, id_order):
        return self.get_creo_sql(id_order)

    def add_creo(
            self, format_creo, type_creo, category, description, id_user, geo, language, currency, format_res,
            offer, voice, source, deadline
    ):
        return self.add_creo_sql(
            format_creo, type_creo, category, description, id_user, geo, language, currency, format_res, offer,
            voice, source, deadline
        )