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

IN_FILE = "./basic_info.csv"
OUT_FILE = "./ready_for_modoboa.csv"
SEP = ';'
ACCOUNT_KWD = "account"
DEF_PWD = "PAssword12"
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

    in_file = IN_FILE
    out_file = OUT_FILE
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
        """
        Hmmm.
        Modoboa import seems to expect the delimiter to be followed by a space.
        But now that I'm writing using the CSV module, that's non-trivial.
        So the output file must be hand-opened and all ';'s replaced with '; '.
        No... that's not the problem. The password must contain an uppercase char.
        (Unless they're BOTH problems!)
        Still failed to login, even with the uppercase char. So hand-editing to add the space again.
        Still failing, weirdly. And when I updated the password for the user as "admin", the interface
        language changed to Czech.
        Going back to not hand-editing the email address file.
        """
        with open(self.out_file, mode='w', newline='') as csvFile:
            writer = csv.writer(csvFile, delimiter=DELIM)
            for address in self:
                # print(address)
                writer.writerow(address.__repr__())

    def read(self):
        with open(self.in_file, mode='r', newline='') as csvfile:
             reader = csv.reader(csvfile, delimiter=DELIM)
             for row in reader:
                addr = Address(row[2], DEF_PWD, row[0], row[1])
                self.append(addr)



if __name__ == "__main__":

    addr_list = AddressList()
    addr_list.read()
    for addr in addr_list:
        for field in addr.__repr__():
            print(field,)

    addr_list.write()

    import sys
    sys.exit()


    # print(addr)
    addr_list.append(addr)

    addr = Address('fake2', DEF_PWD, "Roger", "Thornhill", address = 'rlo.uganda@gmail.com')
    # print(addr)
    addr_list.append(addr)

    addr = Address('fake33', DEF_PWD, "Sandra", "Smith", address = 'rlo.uganda@gmail.com')
    # print(addr)
    addr_list.append(addr)

    addr_list.write()

