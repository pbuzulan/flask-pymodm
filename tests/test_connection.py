import unittest

from flask_pymodm.connection import connect


class ConnectionTest(unittest.TestCase):

    def test_connection_without_config_raises(self):
        config = None
        with self.assertRaises(TypeError):
            connect(config)


if __name__ == '__main__':
    unittest.main()
