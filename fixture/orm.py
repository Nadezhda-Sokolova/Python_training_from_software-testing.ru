from pony.orm import *

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        __table__='group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column = 'group_header')
        footer = Optional(str, cplumn='group_footer')

    class ORMContact(db.Entity):
        __table__ = 'addressbook'
        id = PrimaryKey(int, column='id')
        first_name = Optional(str, column='firstname')
        last_name = Optional(str, column='lastname')
        address = Optional(str, column='address')
        home_phone = Optional(str, column='home')
        mobile_phone = Optional(str, column='mobile')
        work_phone = Optional(str, column='work')
        fax = Optional(str, column='fax')
        mail_1 = Optional(str, column='email')
        mail_2 = Optional(str, column='email2')
        mail_3 = Optional(str, column='email3')
        deprecated = Optional(datetime, column='depricated')

