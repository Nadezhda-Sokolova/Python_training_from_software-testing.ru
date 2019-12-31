from sys import maxsize

class Contact:
    def __init__(self, first_name=None, last_name=None, id = None, address=None,
                 all_phones_from_home_page=None, home_phone=None, mobile_phone=None, work_phone=None, fax=None,
                 all_emails_from_home_page=None, mail_1=None, mail_2=None, mail_3=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.all_phones_from_home_page = all_phones_from_home_page
        self.mail_1 = mail_1
        self.mail_2 = mail_2
        self.mail_3 = mail_3
        self.all_emails_from_home_page = all_emails_from_home_page
        # self.day = day
        # self.month = month
        # self.year = year
        self.id = id


    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.first_name, self.last_name, self.address, self.home_phone,
                                                  self.work_phone, self.mobile_phone, self.fax, self.mail_1, self.mail_2,
                                                  self.mail_3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name \
               and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
