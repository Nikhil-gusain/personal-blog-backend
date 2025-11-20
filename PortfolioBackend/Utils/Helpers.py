from django_quill.fields import QuillField
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from PortfolioBackend.models import Tokens
import json

class cred():
    project_id = "fast-api-test-474705"
    private_key_id="e814c1f006c2688d584cd335305b1af612c01a8e"
    private_key="-----BEGIN PRIVATE KEY-----\nMIIEugIBADANBgkqhkiG9w0BAQEFAASCBKQwggSgAgEAAoIBAQCP8bVDfwqiOt4y\nwCzXZoirE0BEK4Mk39IPuJlGPVHLfR8vpIwDvQ0yWE5/qKtw5os9K7AGA9Qaha+4\nOUTfms1be57HQ85IItJXnNyLNYwY+w9wvV4rwutvmavWhfRCtbON9CwJCmZve9iC\nIYMAsVUJxyd00tkcjdG/N2l2YgSy0kF/lZ6rtWK+z3SfFXF6Q/+mSeZPYE2tsOpM\nQ5oXRjqBSeoVMygOzDaTJFPw+4IaaOF4WZhrm6qW19Q/C+WZiOJzbL/gPQypKYQZ\n7G/vg8yIBIOfW1WEwOfroujbv8NdN6znYEngk9qObtB3qram3Y2MqwuB/WzQGG9O\npzHNpMeXAgMBAAECgf8mph3qbVptkw/7MiUOAb03JHrZnQstmBOLg2OJQpzOqA0w\n2JHNENrLFYyE8D4li4trgvEerFRHAKunATLAUGSCYaFotwHvhONGNyjKbecVA+hJ\n1ljQ+2o7tT0QC78eKk0ZLqxTVU8eTxT7cAQNieCOv4wpZiLKenInvQnybnn854mX\nVMzTW/1ody1NS8NLsG3o/M8RN2qlpOvYjB8sQm15WEhAr1lBrA0YlmERf7HlDZt9\ngmsNElMtCTAH9yhv+mcuDaGCJwLMo+dZAYmTRVbA7TP1u+z3KODW875mg6H6kv+3\nisuU6CanAFmw/2dGJveiXTMFoG3aJaQ7MAuHTRECgYEAwfzLWIIFnGD2XC3KFACD\n/kPovSVpBb/0qD8IaENbZ4WjPxj/rvnh+4AzOQgVSK+cfeUchW9drTsoa8tlFIg0\nurrYyOFgymZ0dIv9m7x9TD8gvJZ+E/kt61EajDwbYHI5GDaRQeFskK3dqZyLGxmN\nnmxrZdRce7NaXxrcAaithqMCgYEAvfWOy6e4f6+n30mBa7zebq/ShqgbgaygdoX/\nVV50WUSiFlWC+RqFtBjL2x0aREz2OyGzaxD106oe9exquAuHhKIZxBhdqCx78vsP\nNTg/eFpTq21DnKL5f4vf9yUma0ZaNFdekbp7AQgu774wTuCCyLe2d1ovVdi8B1hN\nGXuwbn0CgYAqtlyXqllN61OTTEm4SbzGWXF/ZCNRrshR2z8gpeQUUSp2lCyH/GEz\nnTCqGAuHq5MLbUzwXGsF34aw5WHmOW9Sxh1Bbc6AAjsWBlTa24/DIAs3OvObtjvU\nGlF8Gyfz/nJv0GP/W4EqAf5SgDNoziGOhlTHYRDT89OsKR/UBa3ffQKBgHS8unN3\ncA+wEDdNQebG298j1/n+x2CqiLYt5Ns+v7u4TO/yvxl87hvefTD7so+0yEFQlaU/\neAMK8hnpny/Zjf+5aqIy4yOdqtKI7TCkj4TT5cVc0YcqNK/ocsu8Hd8hDgBKjQh7\nlGnu8IFO3PssR9M36z9vwdU861iMMF1vwN41AoGAbKWWim65IRDDh+RLmRrBi5h+\nUbxscDjQqKtdYMTERfKDlsIiyC0cSvpILoMcdCnIkPMB9WICb3dlIkTnUagqw2yM\nxQwLhDJrtAjmNOQxQJmbVQqTapca6e+f8+nWoWMpVdCX2P04pdpW3T41DqnL+z/m\nE+H9B1u372SESMChsks=\n-----END PRIVATE KEY-----\n"
    client_email="personal-portfolio@fast-api-test-474705.iam.gserviceaccount.com"
    client_id = "108869390288615649188"
    auth_uri = "https://accounts.google.com/o/oauth2/auth"
    token_uri = "https://oauth2.googleapis.com/token"
    auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
    client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/personal-portfolio%40fast-api-test-474705.iam.gserviceaccount.com"
    universe_domain = "googleapis.com"

class Helpers():
    
    @staticmethod
    def CalculateReadingTime(text:QuillField)->int:
        words = text.split()
        readingTime = len(words) / 200
        return readingTime
    
    @classmethod
    def loadCreds(self):
        t = Tokens.objects.first()
        data = {
            "token": t.token,
            "refresh_token": t.refreshToken,
            "token_uri": t.tokenUri,
            "client_id": t.clientId,
            "client_secret": t.clientSecret,
            "scopes": json.loads(t.scopes),
            "expiry": t.expiry
        }
        creds = Credentials.from_authorized_user_info(data, data["scopes"])
        return creds, t


    @classmethod
    def refreshCreds(self,creds, token_row):
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
            token_row.token = creds.token
            token_row.expiry = creds.expiry.isoformat()
            token_row.save(update_fields=["token", "expiry"])
        return creds


    @classmethod
    def uploadToDrive(self,file_path, file_name, folder_id=None):
        creds, token_row = self.loadCreds()
        creds = self.refreshCreds(creds, token_row)

        drive = build("drive", "v3", credentials=creds)

        meta = {"name": file_name}
        if folder_id:
            meta["parents"] = [folder_id]

        media = MediaFileUpload(file_path, resumable=True)
        f = drive.files().create(body=meta, media_body=media, fields="id").execute()

        drive.permissions().create(
            fileId=f["id"],
            body={"type": "anyone", "role": "reader"}
        ).execute()

        info= drive.files().get(
            fileId=f["id"],
            fields="id, webViewLink, webContentLink"
        ).execute()

        return f"https://drive.google.com/thumbnail?id={info['id']}"