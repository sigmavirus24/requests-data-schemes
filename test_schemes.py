import unittest
from requests_data_schemes import multipart_formdata

return_value = ('--{0}\r\nContent-Disposition: form-data; name="key1"\r\n\r\n'
                'value1\r\n--{0}\r\nContent-Disposition: form-data; name='
                '"key2"\r\n\r\nvalue2\r\n--{0}--\r\n')

class SchemesTests(unittest.TestCase):
    def test_multipart_formdata(self):
        m = multipart_formdata([('key1', 'value1'), ('key2', 'value2')])
        i = m.find('\r\n')
        token = m[2:i]
        self.assertEqual(m, return_value.format(token))


if __name__ == '__main__':
    unittest.main()
