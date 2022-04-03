import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('../bettingapp-346110-9e1235526163.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('LIVE')

# get the fourth sheet of the Spreadsheet
sh = sheet.get_worksheet(0)


if __name__ == '__main__':
    print(sheet.worksheets())



