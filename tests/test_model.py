#from unittest import TestCase
import pytest
from pysunpower.devicemodel import DeviceModel
import json

def test_type_g():
    f = open('type_g.json')
    json_data = f.read()
    data = DeviceModel.parse_raw(json_data)

    assert (data.devices[0].DEVICE_TYPE == "PVS")
    assert (len(data.devices) == 21) # 3 control devices and 18 inverters

