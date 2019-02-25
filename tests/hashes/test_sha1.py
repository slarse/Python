import hashlib
import unittest

from hashes.sha1 import SHA1Hash

class SHA1HashTest(unittest.TestCase):
    """
    Test class for the SHA1Hash class. Inherits the TestCase class from unittest
    """
    def testMatchHashes(self):
        msg = bytes('Test String', 'utf-8')
        self.assertEqual(SHA1Hash(msg).final_hash(), hashlib.sha1(msg).hexdigest())
