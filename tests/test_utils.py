import unittest

import flask_pymodm.util


class TestUtils(unittest.TestCase):
    host = "mongodb"
    port = "27017"
    db = "testDb"

    # noinspection PyTypeChecker
    def test_get_uri_without_auth(self):
        check_str = "mongodb://" + self.host + ":" + self.port + "/" + self.db
        self.assertEqual(flask_pymodm.util._get_uri(None, None, self.host, self.port, self.db), check_str)

    # noinspection PyTypeChecker
    def test_get_uri_with_int_port_fails(self):
        self.port = 27017

        with self.assertRaises(TypeError):
            flask_pymodm.util._get_uri(None, None, self.host, self.port, self.db)


if __name__ == '__main__':
    unittest.main()
