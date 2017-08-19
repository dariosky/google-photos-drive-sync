from __future__ import print_function

import httplib2
from apiclient import discovery

from api import settings
from api.gphoto import get_albums
from api.helpers import get_credentials


def try_drive(http):
    service = discovery.build('drive', 'v3', http=http)

    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))


def try_photos(http):
    # TODO: Looks like I should use something else to access Picasa Web API
    # https://developers.google.com/picasa-web/docs/3.0/developers_guide_protocol

    for album in get_albums(http):
        print(album)


def main():
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    credentials = get_credentials(settings.DRIVE_CREDENTIALS_PATH)
    http = credentials.authorize(httplib2.Http('.cache'))

    # try_drive(http)
    try_photos(http)


if __name__ == '__main__':
    main()
