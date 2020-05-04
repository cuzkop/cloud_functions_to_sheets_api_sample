import gspread
import google.auth

def main(event, context):

    credentials, _ = google.auth.default(scopes=['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'])

    gc = gspread.authorize(credentials)

    SPREADSHEET_KEY = '{your-spreadsheet-key}'

    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

    import_value = int(worksheet.acell('A1').value)

    export_value = import_value + 100
    worksheet.update_cell(1, 2, export_value)