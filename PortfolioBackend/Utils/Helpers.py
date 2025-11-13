from django_quill.fields import QuillField
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


class Helpers:
    @staticmethod
    def CalculateReadingTime(text:QuillField)->int:
        words = text.split()
        readingTime = len(words) / 200
        return readingTime
    
    @staticmethod
    def upload_file_to_gdrive(file_path, file_name, folder_id=None):
        SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), 'service_account.json')
        SCOPES = ['https://www.googleapis.com/auth/drive.file']
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )

        drive_service = build('drive', 'v3', credentials=credentials)
        file_metadata = {'name': file_name}
        if folder_id:
            file_metadata['parents'] = [folder_id]

        media = MediaFileUpload(file_path, resumable=True)
        file = drive_service.files().create(body=file_metadata, media_body=media, fields='id, webViewLink').execute()

        # Make the file public (optional)
        drive_service.permissions().create(
            fileId=file['id'],
            body={'role': 'reader', 'type': 'anyone'}
        ).execute()

        # Return public URL
        return f"https://drive.google.com/uc?id={file['id']}"