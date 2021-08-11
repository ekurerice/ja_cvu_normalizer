# coding: utf-8
# Date:
# Filename:

from ja_cvu_normalizer.ja_cvu_normalizer import JaCvuNormalizer
from ja_cvu_normalizer.reader import cvuj_reader
import unittest
import sys
from logging import Formatter, getLogger, StreamHandler, DEBUG, WARNING, FileHandler

__author__ = ""
__date__ = ""

""" variables """
formatter = Formatter('%(asctime)-15s - %(levelname)-8s - %(message)s')
logger = getLogger(__name__)
logger.setLevel(DEBUG)

# handler1
handler = StreamHandler(sys.stdout)
handler.setFormatter(formatter)

# handler2 (file)
# handler2 = FileHandler("test.log")
# handler2.setLevel(WARNING)
# handler2.setFormatter(formatter)

logger.addHandler(handler)
# logger.addHandler(handler2)


class TestJpCvuNormalzier (unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.jp_cvu_normalizer = JaCvuNormalizer()

    def test_normalize_1(self):
        actual = self.jp_cvu_normalizer.normalize("髙")
        expected = "高"
        self.assertEqual(expected, actual)
