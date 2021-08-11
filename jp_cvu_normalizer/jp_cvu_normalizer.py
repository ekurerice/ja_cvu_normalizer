# coding: utf-8
# Date:
# Filename:

import re
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


class JpCvuNormalizer(object):
    def __init__(self, mapping_table):
        self.mapping_table = mapping_table

    def normalize(self, text: str):
        _text = text
        for key in self.mapping_table:
            _text = re.sub(key, self.mapping_table[key], _text)
        return _text
