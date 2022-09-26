import csv
import sys
import pwinput
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ACCOUNT_PATH = OUTPUT_PATH / Path("./Login_info")


def relative_to_account(path: str) -> Path:
    return ACCOUNT_PATH / Path(path)


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


class LOGIN():
    def __init__(self):
        self.name = ''
        self.account = ''
        self.password = ''

    def READ_GOOGLE(self, login_info = '', pos = -1, name = ''):
        """login_info: 'NAME', 'ACCOUNT', 'PASSWORD', pos: position, name: for search key"""
        self.name_list = []
        self.account_list = []
        self.password_list = []
        self.info_dict = {}
        with open(file=relative_to_account('google.csv'), mode='r', newline='') as self.google:
            reader = csv.reader(self.google, delimiter=',')
            for row in reader:
                self.name_list.append(row[0])
                self.account_list.append(row[1])
                self.password_list.append(row[2])
                self.info_dict[row[0]] = [row[1], row[2]]

            self.google.close()

        if not name:
            match login_info:
                case 'NAME':
                    if pos == -1:
                        return self.name_list
                    else:
                        return self.name_list[pos]
                
                case 'ACCOUNT':
                    return self.account_list[pos]

                case 'PASSWORD':
                    return self.password_list[pos]
        else:
            return self.info_dict['name']

    def WRITE_GOOGLE(self, name, account, password):
        """name, account, password"""
        self.name = name
        self.account = account
        self.password = password

        with open(file=relative_to_account('google.csv'), mode='a+', newline='') as self.google:
            writer = csv.writer(self.google, delimiter=',')
            writer.writerow([self.name, self.account, self.password])

            # self.google_confirm = pwinput.pwinput('confirm password: ')

        self.google.close()

    def READ_MYACG(self, login_info = '', pos = -1, name = ''):
        """login_info: 'NAME', 'ACCOUNT', 'PASSWORD', pos: position
            name: return a list, [0]: Account, [1]: Password"""
        self.name_list = []
        self.account_list = []
        self.password_list = []
        self.info_dict = {}
        with open(file=relative_to_account('myacg.csv'), mode='r', newline='') as self.myacg:
            reader = csv.reader(self.myacg, delimiter=',')
            for row in reader:
                self.name_list.append(row[0])
                self.account_list.append(row[1])
                self.password_list.append(row[2])
                self.info_dict[row[0]] = [row[1], row[2]]

            self.myacg.close()
        
        if not name:
            match login_info:
                case 'NAME':
                    if pos == -1:
                        return self.name_list
                    else:
                        return self.name_list[pos]
                
                case 'ACCOUNT':
                    return self.account_list[pos]

                case 'PASSWORD':
                    return self.password_list[pos]
        else:
            return self.info_dict[name]

    def WRITE_MYACG(self, name, account, password):
        """name, account, password"""
        self.name = name
        self.account = account
        self.password = password

        with open(file=relative_to_account('myacg.csv'), mode='a+', newline='') as self.myacg:
            writer = csv.writer(self.myacg, delimiter=',')
            writer.writerow([self.name, self.account, self.password])

            # self.google_confirm = pwinput.pwinput('confirm password: ')

        self.myacg.close()

