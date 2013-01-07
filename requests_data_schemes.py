__title__ = 'requests_data_schemes'
__author__ = 'Ian Cordasco'
__version__ = '0.1'
__copyright__ = '(C) 2013 Ian Cordasco'
__license__ = 'Apache'

from requests.packages.urllib3.filepost import encode_multipart_formdata


def multipart_formdata(data):
    """Takes a dictionary (or dictionary-like object), or list of two-tuples
    and return a string of multipart/form-data assuming no files.

    :param data: dictionary-like object or list of two-tuples, e.g.,
        ``{'key1': 'value1', 'key2': 'value2'}`` or ``[('key1', 'value1'),
        ('key2', 'value2')]``
    :returns: str
    """
    if data is None:
        return None

    dict(data)

    if isinstance(data, dict):
        data = data.items()

    return encode_multipart_formdata(data)[0].decode()
