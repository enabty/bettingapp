from auth import pd
from auth import gspread
from auth import sh


val = sh.acell('C4').value

if __name__ == '__main__':
    print(sh.get('C4'))  # [['16.32kr']]
    print(val)  # 16.32kr


