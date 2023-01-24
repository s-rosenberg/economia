import gspread
import pandas as pd
import os

SHEET_ID = os.getenv('SPREADSHEET_ID')
SHEET_NAME = os.getenv('WORKSHEET_NAME')

gc = gspread.service_account('credentials.json')
spreadsheet = gc.open_by_key(SHEET_ID)
worksheet = spreadsheet.worksheet(SHEET_NAME)
rows = worksheet.get_all_records()
print(rows[:5])

print('==============================')
df = pd.DataFrame(rows)
print(df.head())