requests_data_schemes
=====================

:author: Ian Cordasco
:version: 0.1
:license: Apache

This is a small module meant to offer a simpler way for requests users to
encode their data in a slightly more sensible way. So far this package only
contains ``multipart_formdata`` which will not encode anything as a file for
``multipart/form-data``. It comes with a test for the one function which will
pass.

Examples
--------

.. code-block:: python

    from requests_data_schemes import multipart_formdata
    import requests


    url = 'https://api.example.com/endpoint'
    r1 = requests.post(url, data=multipart_formdata(
        [('key1', 'value1'), ('key2', 'value2')]), headers={
        'Content-Type': 'multipart/form-data'})
    r2 = requests.post(url, data=multipart_formdata(
        {'key1': 'value1', 'key2': 'value2'}), headers={
        'Content-Type': 'multipart/form-data'})
