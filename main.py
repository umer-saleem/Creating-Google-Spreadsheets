from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1-y5n3o6Mh0F_QYkNgyTUcyk6gxEv3_w9vY5UYyR3HDQ'


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="CertProgramInfo!A1:E16").execute()
data_list = result["values"]
data = {}
for item in data_list[0]:
    data[item] = []
for item in data_list[1:]:
    for ind,val in enumerate(item):
        data[data_list[0][ind]].append(val)

df = pd.DataFrame(data)
print(df)


