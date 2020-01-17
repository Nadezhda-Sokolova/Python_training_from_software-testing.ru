import mysql.connector
from model.group import Group
from model.contact import Contact

class DBFixture():

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
           cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
           for row in cursor:
               (id, name, header, footer) = row
               list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
           cursor.execute("select id, firstname, lastname, address, home, mobile, work, fax, email, email2, email3 from addressbook")
           for row in cursor:
               (id, first_name, last_name, address, home_phone, mobile_phone, work_phone, fax, mail_1, mail_2, mail_3 ) = row
               list.append(Contact(id=str(id), first_name=first_name, last_name=last_name, address=address,
                                 home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, fax=fax, mail_1=mail_1, mail_2=mail_2, mail_3=mail_3 ))
        finally:
            cursor.close()
        return list


    def distroy(self):
        self.connection.close()
