import re
import xml.etree.ElementTree


def get_albums(http):
    GET_ALBUMS_URL = 'https://picasaweb.google.com/data/feed/api/user/default'
    (resp_headers, content) = http.request(GET_ALBUMS_URL,
                                           headers={
                                               'GData-Version': '3',
                                           })
    if resp_headers.status >= 400:
        raise Exception(content.decode('utf-8'))

    # Remove the default namespace definition (xmlns="http://some/namespace")
    # see: https://stackoverflow.com/questions/34009992/python-elementtree-default-namespace
    xmlstring = re.sub(r"""\s(xmlns="[^"]+"|xmlns='[^']+')""", '', content.decode('utf8'), count=1)
    e = xml.etree.ElementTree.fromstring(xmlstring)

    namespaces = {
        'gphoto': 'http://schemas.google.com/photos/2007',
    }
    for album in e.findall('entry'):
        yield dict(
            id=album.find('gphoto:id', namespaces).text,
            title=album.find('title', namespaces).text,
            numphotos=album.find('gphoto:numphotos', namespaces).text,
        )
