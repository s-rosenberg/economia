from datetime import datetime
import pandas as pd
import gspread
import os

class ExcelReader:
    
    @staticmethod
    def excel_to_dataframe(sheet_id:str, sheet_name:str) -> pd.DataFrame:

        gc = gspread.service_account('credentials.json')
        spreadsheet = gc.open_by_key(sheet_id)
        worksheet = spreadsheet.worksheet(sheet_name)
        rows = worksheet.get_all_records()
        df = pd.DataFrame(rows)

        return df
    
    @staticmethod
    def parse_date(date: str) -> datetime:
        day, month, year = date.split('/')
        return datetime(int(year),int(month), int(day))

if __name__ == '__main__':
    SHEET_ID = os.getenv('SPREADSHEET_ID')
    SHEET_NAME = os.getenv('WORKSHEET_NAME')

    data_frame = ExcelReader.excel_to_dataframe(SHEET_ID, SHEET_NAME)