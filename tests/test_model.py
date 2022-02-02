import pytest
from pysunpower.sunpowermodel import SunPowerModel, SupervisorModel, ProductionModel, ConsumptionModel, \
    TypeGInverterModel


def test_type_g():
    """Test TypeG Data Parsing"""
    f = open('type_g.json')
    json_data = f.read()
    data = SunPowerModel.parse_raw(json_data)

    assert (data.devices[0].DEVICE_TYPE == "PVS")
    assert (len(data.devices) == 21) # 3 control devices and 18 inverters

    assert type(data.devices[0]) is SupervisorModel
    assert type(data.devices[1]) is ProductionModel
    assert type(data.devices[2]) is ConsumptionModel
    assert type(data.devices[3]) is TypeGInverterModel
