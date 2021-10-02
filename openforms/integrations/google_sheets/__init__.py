import gspread
from oauth2client import client


class GoogleSheetIntegration:
    def __init__(self, sheet_id):
        self.client = gspread.service_account(
            filename="openforms/integrations/google_sheets/credentials.json"
        )
        self.spreadsheet = self.client.open_by_key(
            sheet_id
        )  # sheet access must be given to the gcloud service account
        self.worksheet = self.set_worksheet()

    def set_worksheet(self, wsheet_number=0):
        worksheet = self.spreadsheet.get_worksheet(wsheet_number)
        return worksheet

    def add_row(self, data):
        self.worksheet.append_row(data)

    def set_header(self, data):
        self.worksheet.insert_row(data, 1)
