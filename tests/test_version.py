import unittest

from culqi import __version__


class VersionTest(unittest.TestCase):
    @staticmethod
    def test_version():
        assert __version__ == "1.0.4"


if __name__ == "__main__":
    unittest.main()
