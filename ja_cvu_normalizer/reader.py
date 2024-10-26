# coding: utf-8
# Date:
# Filename:

import csv


def decomment(csvfile):
    for row in csvfile:
        raw = row.split("#")[0].strip()
        if raw:
            yield raw


def to_char(unicodes: list):
    return "".join(map(lambda u: chr(int(u, 16)), unicodes))


def cvuj_reader(filepath):
    mapping_table = dict()
    with open(filepath, encoding="utf-8") as f:
        for row in csv.reader(decomment(f), delimiter="\t"):
            mapper = (to_char([row[0]]), to_char(row[1].split(" ")))
            mapping_table[mapper[0]] = mapper[1]

    return mapping_table
