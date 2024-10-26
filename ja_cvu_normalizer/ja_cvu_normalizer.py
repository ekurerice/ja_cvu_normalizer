from .reader import cvuj_reader
import os

import logging


class JaCvuNormalizer(object):
    def __init__(
        self,
        mapping_table=None,
        mapping_table_path=os.path.join(
            os.path.dirname(__file__), "resource/ISO-2022-JP.txt"
        ),
    ):
        if mapping_table_path:
            self.mapping_table = cvuj_reader(mapping_table_path)

        if mapping_table:
            self.mapping_table = mapping_table

        if self.mapping_table is None:
            logging.warning("mapping_table is not defined.")
            exit(-1)

    def normalize(self, text: str):
        _text = text
        for key in self.mapping_table:
            _text = _text.replace(key, self.mapping_table[key])
        return _text
