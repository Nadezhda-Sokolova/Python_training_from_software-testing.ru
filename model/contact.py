from sys import maxsize

class Contact:
    def __init__(self, first_name=None, last_name=None, id = None,
                 all_phones_from_home_page=None, home_phone=None, mobile_phone=None, work_phone=None, fax=None):
        self.first_name = first_name
        self.last_name = last_name
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.all_phones_from_home_page = all_phones_from_home_page
        # self.address = address
        # self.mail = mail
        # self.day = day
        # self.month = month
        # self.year = year
        self.id = id


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name \
               and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
