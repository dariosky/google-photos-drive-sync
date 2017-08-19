from oauth2client import tools

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = " ".join(['https://www.googleapis.com/auth/drive',
                   'https://picasaweb.google.com/data/'])
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Photos Drive Sync'

DRIVE_CREDENTIALS_PATH = '~/.credentials/gphotodrivesync'
