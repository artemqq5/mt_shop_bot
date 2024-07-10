from data.database import MyDataBase


class CreoRepository(MyDataBase):

    def get_creo(self, id_order):
        return self._get_creo_sql(id_order)

    def add_creo(
            self, format_creo, type_creo, category, description, id_user, geo, language, currency, format_res,
            offer, voice, source, deadline, count, sub_desc
    ):
        return self._add_creo_sql(
            format_creo, type_creo, category, description, id_user, geo, language, currency, format_res, offer,
            voice, source, deadline, count, sub_desc
        )

    def update_dropbox_link(self, id_order, link):
        return self._update_dropbox_link_sql(id_order, link)

