# coding: utf-8
# Date:
# Filename:

from ja_cvu_normalizer.reader import cvuj_reader
import unittest
import os
import sys
import argparse
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


class TestReader (unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def test_reader_1(self):
        mapping_table = cvuj_reader(
            "ja_cvu_normalizer/resource/ISO-2022-JP.txt")
        self.assertTrue("髙" in mapping_table)
