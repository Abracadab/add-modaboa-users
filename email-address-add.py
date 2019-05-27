"""
Easy entry of Modaboa-formatted email addresses.

Modaboa import file requirements:
Provide a CSV file where lines respect one of the following formats:
account; loginname; password; first name; last name; enabled; group; address; quota; [, domain, ...]
alias; address; enabled; recipient; recipient; ...
The first element of each line is mandatory and must be equal to one of the previous values.
You can use a different character as separator.
"""

import csv

FILE_NAME = "./addresses.csv"
SEP = ';'
ACCOUNT_KWD = "account"
DEF_PWD = "default12"
DOMAIN = 's8-software.com'
DELIM = ';'

class Address(object):

    sep = SEP
    domain = DOMAIN

    def __init__(self, username, pwd, f_name, l_name, enabled = 1, group = '', address = "", quota = '', acct_kwd = ACCOUNT_KWD):
        self.acct_kwd = acct_kwd
        self.username = username + "@" + self.domain
        self.pwd = pwd
        self.f_name = f_name
        self.l_name = l_name
        self.enabled = enabled
        self.group = group
        self.address = address
        self.quota = quota

    def __repr__(self):
        """
        [ account (literal word); username; password; first name; last name; enabled; group; address; quota; [, domain, ...]
        """

        # Works fine when final "address" and "quota" are empty strings
        # return ['account', self.username, self.pwd, self.f_name, self.l_name, self.enabled, self.group, self.address, self.quota ]
        return ['account', self.username, self.pwd, self.f_name, self.l_name, self.enabled, self.group, '', '' ]
        """
        return "{}{} {}{} {}{} {}{} {}{} {}{} {}{} {}{} {}{}".format(self.acct_kwd, self.sep, self.username, self.sep, self.pwd, self.sep, self.f_name, self.sep, self.l_name, self.sep, self.enabled, self.sep, self.group, self.sep, self.address, self.sep, self.quota, self.sep)
        """

class AddressList(list):

    file_name = FILE_NAME
    def __init__(self):
        pass

    """
    def write(self):
        with open(self.file_name, 'w+') as f:
            for addr in self:
                f.seek(0,2) ################################

                f.write(str(addr))
                f.write('\n')
    """

    def write(self):
        with open(self.file_name, mode='w', newline='') as csvFile:
            writer = csv.writer(csvFile, delimiter=DELIM)
            for address in self:
                # print(address)
                writer.writerow(address.__repr__())



if __name__ == "__main__":

    addr_list = AddressList()

    addr = Address('fake1', DEF_PWD, "Joe", "Smith", address='rlo.uganda@gmail.com')
    # print(addr)
    addr_list.append(addr)

    addr = Address('fake2', DEF_PWD, "Roger", "Thornhill", address = 'rlo.uganda@gmail.com')
    # print(addr)
    addr_list.append(addr)

    addr = Address('fake3', DEF_PWD, "Sandra", "Smith", address = 'rlo.uganda@gmail.com')
    # print(addr)
    addr_list.append(addr)

    addr_list.write()

