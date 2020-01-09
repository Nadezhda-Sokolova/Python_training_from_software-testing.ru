from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "Data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + ''.join([random.choice(symbols) for i in range (random.randrange(maxlen))])

def random_address(prefix, maxlen):
    symbols = string.ascii_letters + string.punctuation + " "*10 + string.digits
    return prefix + ''.join([random.choice(symbols) for i in range (random.randrange(maxlen))])

def random_mails(maxlen, domen):
    symbols = string.ascii_letters + string.digits
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + domen

def random_phones(prefix, maxlen):
    symbols = string.digits
    return prefix + ''.join([random.choice(symbols) for i in range (random.randrange(maxlen))])


contact_data = [Contact(first_name='Oleg', last_name='Petrov', address='Moscow',
             home_phone='111', work_phone='222', mobile_phone='333', fax='123',
             mail_1='kk@ya.ru', mail_2='ii@ya.by', mail_3='lala@gmail.com')] + \
               [
                   Contact(first_name=random_string("first_name is ", 8), last_name=random_string("last_name is ", 10),
                        address=random_address("address is ", 15), home_phone=random_phones("home_phone is ", 10),
                        work_phone=random_phones("work_phone is ", 10), mobile_phone=random_phones("mobile_phone is ", 10),
                        fax=random_phones("fax is ", 10), mail_1=random_mails(10, "@mail_1.ru;"),
                        mail_2=random_mails(10, "@mail_2.by;", ), mail_3=random_mails(10, "@mail_3.com;")) for i in range(5)]



file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(contact_data))
