from unittest import TestCase
from python.scripts.which_are_in import in_array


class Test(TestCase):
    def test_in_array(self):
        self.assertEqual(in_array(["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]),
                           ['arp', 'live', 'strong'])
        self.assertEqual(in_array(["arp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]),
                           ['arp'])
