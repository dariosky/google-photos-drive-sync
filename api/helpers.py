import os

from oauth2client import client, tools
from oauth2client.file import Storage

from .settings import LOCAL_CREDENTIALS, CLIENT_SECRET_FILE, SCOPES, APPLICATION_NAME, flags


def get_credentials(flags=flags):
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    credential_path = os.path.expanduser(LOCAL_CREDENTIALS)
    credential_folder = os.path.dirname(credential_path)
    if not os.path.isdir(credential_folder):
        os.makedirs(credential_folder)

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials
