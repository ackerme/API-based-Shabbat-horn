import os
import time
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
key= "8sxwHsnaouSFbfFLgK0ShK_BlIESC7M"
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MP3_PATH_1 = r"C:\Users\שיר\Downloads\‏‏צפירה למקוה - עותק.mp4"  # שנה לנתיב הקובץ שלך
MP3_PATH_2 = r"C:\Users\שיר\Downloads\song.mp3"
MP3_PATH_3 = r"C:\Users\שיר\Downloads\song.mp3"
MP3_PATH_4 = r"C:\Users\שיר\Downloads\song.mp3"

def get_calendar_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('calendar', 'v3', credentials=creds)

def check_events_and_play(service):
    now = datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=1, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    if events:
        event = events[0]
        start = event['start'].get('dateTime', event['start'].get('date'))
        event_time = datetime.fromisoformat(start.replace('Z', '+00:00'))
        # בדוק אם האירוע מתחיל תוך דקה
        if 0 <= (event_time - datetime.utcnow()).total_seconds() < 60:
            os.startfile(MP3_PATH_1)
            
 
if __name__ == '__main__':
    service = get_calendar_service()
    while True:
        check_events_and_play(service)
        time.sleep(60)