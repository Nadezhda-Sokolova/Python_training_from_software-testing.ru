
Scenario Outline: Add new contact
    Given a contact list
    Given a contact with <first_name>, <last_name>, <address>, <home_phone>, <work_phone>, <mobile_phone>, <fax>, <mail_1>, <mail_2> and <mail_3>
    When I add a new contact to the list
    Then the new contact list is equal to the old list with the added contact

    Examples:
    | first_name  | last_name  | address  | home_phone  |  work_phone  | mobile_phone  |  fax  |  mail_1  | mail_2  | mail_3 |
    |oleg         |popov       |NN        |123          |       222    |678            |as34   |nn@ya.ru |jj@ya.ru |u@ya.ru|
    |oleg2        |popov2      | NN2      |  123        |     222      |  678          | as34  | 9n@ya.ru | 2j@ya.ru| 6@ya.ru|



Scenario: Delete a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete the contact from list
    Then the new contact list is equal to the old list without the delete contact


Scenario: Edit contact
    Given a non-empty contact list
    Given a random contact from the list
    When I modify the contact from list
    Then the new contact list is equal to the old list