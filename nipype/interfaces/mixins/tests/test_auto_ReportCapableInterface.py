# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..reporting import ReportCapableInterface


def test_ReportCapableInterface_inputs():
    input_map = dict()
    inputs = ReportCapableInterface.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
