#import pymysql.cursors

from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name='addressbook', user="root", password="")

try:
    l = db.get_contacts_not_in_group(Group(id='145'))
    for item in l:
        print(item)
    print(len(l))

finally:
    pass



# from fixture.db import DBFixture
#
# db = DBFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#
# # try:
# #     groups = db.get_group_list()
# #     for group in groups:
# #         print(group)
# #     print(len(groups))
#
# try:
#     contacts = db.get_contacts_list()
#     for contact in contacts:
#         print(contact)
#     print(len(contacts))
#
# finally:
#     db.distroy()


# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
#
# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()
