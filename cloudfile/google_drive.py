import pickle
import os.path
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/drive"]


def get_service():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "cloudfile_api_credentials.json", SCOPES
            )
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build("drive", "v3", credentials=creds)  # service


def upload_file(drive_service, file):
    # TODO add zip functionality
    file_metadata = {"name": "cloudfile_" + file.split(os.sep)[-1]}  # TODO parent
    media = MediaFileUpload(file, mimetype="application/plain")
    file = drive_service.files().create(body=file_metadata, media_body=media).execute()
    file_id = file.get("id")
    add_link_permision(drive_service, file_id)
    url = (
        drive_service.files()
        .get(fileId=file_id, fields="webContentLink")
        .execute()["webContentLink"]
    )
    print(f"File ID: {file_id}, link:{url}")

    return url, file_id


def add_link_permision(drive_service, file_id):
    def callback(request_id, response, exception):
        if exception:
            # Handle error
            print(exception)
        else:
            print(f"Permission Id: {response.get('id')}")

    batch = drive_service.new_batch_http_request(callback=callback)
    user_permission = {
        "type": "anyone",
        "role": "reader",
        "Value": "",
        "WithLink": True,
    }
    batch.add(
        drive_service.permissions().create(
            fileId=file_id, body=user_permission, fields="id"
        )
    )
    batch.execute()


def delete_google_file(drive_service, file_id):
    drive_service.files().delete(fileId=file_id).execute()


"""
    # Call the Drive v3 API
    results = (
        service.files()
        .list(pageSize=10, fields="nextPageToken, files(id, name)")
        .execute()
    )
    items = results.get("files", [])

    if not items:
        print("No files found.")
    else:
        print("Files:")
        for item in items:
            print(u"{0} ({1})".format(item["name"], item["id"]))
"""
if __name__ == "__main__":
    get_service()
