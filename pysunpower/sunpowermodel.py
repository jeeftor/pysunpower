"""Define pydantic models for components."""
from __future__ import annotations

from pydantic import BaseModel


class SupervisorModel(BaseModel):
    """Supervisor model definition."""

    DETAIL: str
    STATE: str
    STATEDESCR: str
    SERIAL: str
    MODEL: str
    HWVER: str
    SWVER: str
    DEVICE_TYPE: str
    DATATIME: str
    dl_err_count: int
    dl_comm_err: int
    dl_skipped_scans: int
    dl_scan_time: int
    dl_untransmitted: int
    dl_uptime: int
    dl_cpu_load: float
    dl_mem_used: int
    dl_flash_avail: int
    panid: int
    CURTIME: str


class ProductionModel(BaseModel):
    """Production model definition."""

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
    ct_scl_fctr: float
    net_ltea_3phsum_kwh: float
    p_3phsum_kw: float
    q_3phsum_kvar: float
    s_3phsum_kva: float
    tot_pf_rto: float
    freq_hz: float
    CAL0: str
    origin: str
    OPERATION: str
    CURTIME: str


class ConsumptionModel(BaseModel):
    """Define a consumption model (power meter)."""

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
    ct_scl_fctr: float
    net_ltea_3phsum_kwh: float
    p_3phsum_kw: float
    q_3phsum_kvar: float
    s_3phsum_kva: float
    tot_pf_rto: float
    freq_hz: float
    i1_a: float
    i2_a: float
    v1n_v: float
    v2n_v: float
    v12_v: float
    p1_kw: float
    p2_kw: float
    neg_ltea_3phsum_kwh: float
    pos_ltea_3phsum_kwh: float
    CAL0: str
    origin: str
    OPERATION: str
    CURTIME: str


class TypeGInverterModel(BaseModel):
    """Type G Inverter model - different models have slightly different charateristics."""

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
    ltea_3phsum_kwh: float
    p_3phsum_kw: float
    vln_3phavg_v: float
    i_3phsum_a: float
    p_mppt1_kw: float
    v_mppt1_v: float
    i_mppt1_a: float
    t_htsnk_degc: float
    freq_hz: float
    stat_ind: str
    origin: str
    OPERATION: str
    CURTIME: str


class SunPowerModel(BaseModel):
    """The Base SunPower Device List REST Api definition."""

    # pydantic will attempt to match list items according to the order shown in the Union
    # listing the items in this order ensures correct JSON conversion as ConsumptionModel
    # is more specific than ProductionModel
    devices: list[
        SupervisorModel | ConsumptionModel | ProductionModel | TypeGInverterModel
    ]
    result: str

    @property
    def consumption(self) -> ConsumptionModel:
        """Return consumption device."""
        return self.devices[2]  # type: ignore

    @property
    def production(self) -> ProductionModel:
        """Return production device."""
        return self.devices[1]  # type: ignore

    @property
    def supervisor(self) -> SupervisorModel:
        """Return Supervisor Device."""
        return self.devices[0]  # type: ignore

    @property
    def inverters(self) -> list[TypeGInverterModel]:
        """Return inverters."""
        return self.devices[3:]  # type: ignore
