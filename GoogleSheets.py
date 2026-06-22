import os.path
from ctypes import HRESULT

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SPREADSHEET_ID = "1wALF3JSAUKt-m8P8DTKonHvBS45ycQyCGKp_sxPW-uA"
RANGE_NAME = "Sheet1!A:Z"


def authenticate_google(): #Google authentication - holds user's active authorization
    credentials = None

    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file(
            "token.json",
            SCOPES
        )

    if not credentials or not credentials.valid:

        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_1046939115832-d4521ui78tla2t1e2ksss5qivsllnkut.apps.googleusercontent.com.json',
                SCOPES
            )

            credentials = flow.run_local_server(port=0)

    with open('token.json', 'w') as token:
        token.write(credentials.to_json())

    return credentials


def connect_to_google_sheets():
    credentials = authenticate_google()

    service = build(
        "sheets",
        "v4",
        credentials=credentials
    )

    return service

inscriptions = []

def read_sheet_data():
    import Database

    service = connect_to_google_sheets()

    result = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME
    ).execute()

    values = result.get("values", [])

    for all in values[1:]:

        participant = {
            "name": f"{all[0]}{all[1]}".strip().lower(),
            "age": all[2],
            "phone": all[3],
            "medical": all[4],
            "transportation": all[5],
            "email": all[6],
            "accommodation": all[7].strip().lower(),
            "inscription": all[8].strip().lower(),
            "payment": float(all[9]),
            "food": all[10]
        }

        inscriptions.append(participant)
        Database.save_data(inscriptions)

    return inscriptions

read_sheet_data()
