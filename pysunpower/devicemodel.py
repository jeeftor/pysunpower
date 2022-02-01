from __future__ import annotations

from typing import List, Union

from pydantic import BaseModel

class SupervisorModel(BaseModel):
    DETAIL: str
    STATE: str
    STATEDESCR: str
    SERIAL: str
    MODEL: str
    HWVER: str
    SWVER: str
    DEVICE_TYPE: str
    DATATIME: str
    dl_err_count: str
    dl_comm_err: str
    dl_skipped_scans: str
    dl_scan_time: str
    dl_untransmitted: str
    dl_uptime: str
    dl_cpu_load: str
    dl_mem_used: str
    dl_flash_avail: str
    panid: int
    CURTIME: str

class ProductionModel(BaseModel):
    ISDETAIL: bool
    SERIAL: str
    TYPE: str
    STATE: str
    STATEDESCR: str
    MODEL: str
    DESCR: str
    DEVICE_TYPE: str
    interface: str
    subtype: str
    SWVER: str
    PORT: str
    DATATIME: str
    ct_scl_fctr: str
    net_ltea_3phsum_kwh: str
    p_3phsum_kw: str
    q_3phsum_kvar: str
    s_3phsum_kva: str
    tot_pf_rto: str
    freq_hz: str
    CAL0: str
    origin: str
    OPERATION: str
    CURTIME: str

class ConsumptionModel(BaseModel):
    ISDETAIL: bool
    SERIAL: str
    TYPE: str
    STATE: str
    STATEDESCR: str
    MODEL: str
    DESCR: str
    DEVICE_TYPE: str
    interface: str
    subtype: str
    SWVER: str
    PORT: str
    DATATIME: str
    ct_scl_fctr: str
    net_ltea_3phsum_kwh: str
    p_3phsum_kw: str
    q_3phsum_kvar: str
    s_3phsum_kva: str
    tot_pf_rto: str
    freq_hz: str
    i1_a: str
    i2_a: str
    v1n_v: str
    v2n_v: str
    v12_v: str
    p1_kw: str
    p2_kw: str
    neg_ltea_3phsum_kwh: str
    pos_ltea_3phsum_kwh: str
    CAL0: str
    origin: str
    OPERATION: str
    CURTIME: str

class TypeGInverterModel(BaseModel):
    ISDETAIL: bool
    SERIAL: str
    TYPE: str
    STATE: str
    STATEDESCR: str
    MODEL: str
    DESCR: str
    DEVICE_TYPE: str
    hw_version: str
    interface: str
    module_serial: str
    PANEL: str
    slave: int
    SWVER: str
    PORT: str
    MOD_SN: str
    NMPLT_SKU: str
    DATATIME: str
    ltea_3phsum_kwh: str
    p_3phsum_kw: str
    vln_3phavg_v: str
    i_3phsum_a: str
    p_mppt1_kw: str
    v_mppt1_v: str
    i_mppt1_a: str
    t_htsnk_degc: str
    freq_hz: str
    stat_ind: str
    origin: str
    OPERATION: str
    CURTIME: str



class DeviceModel(BaseModel):
    devices: List[Union[SupervisorModel, ProductionModel, ConsumptionModel, TypeGInverterModel]]
    result: str