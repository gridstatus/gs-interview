from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    pass


class CaisoFuelMix(Base):
    __tablename__ = "caiso_fuel_mix"

    coal = Column("coal", Integer)

    wind = Column("wind", Integer)
    other = Column("other", Integer)
    solar = Column("solar", Integer)
    biogas = Column("biogas", Integer)
    biomass = Column("biomass", Integer)
    imports = Column("imports", Integer)
    nuclear = Column("nuclear", Integer)
    batteries = Column("batteries", Integer)
    geothermal = Column("geothermal", Integer)
    large_hydro = Column("large_hydro", Integer)
    natural_gas = Column("natural_gas", Integer)
    small_hydro = Column("small_hydro", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class CaisoLoad(Base):
    __tablename__ = "caiso_load"

    load = Column("load", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class CaisoLoadForecast(Base):
    __tablename__ = "caiso_load_forecast"

    load_forecast = Column("load_forecast", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    publish_time_utc = Column("publish_time_utc", DateTime, primary_key=True)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class ErcotFuelMix(Base):
    __tablename__ = "ercot_fuel_mix"

    wind = Column("wind", Integer)
    hydro = Column("hydro", Integer)
    other = Column("other", Integer)
    solar = Column("solar", Integer)
    nuclear = Column("nuclear", Integer)
    ab_cdc_lsn = Column("_ab_cdc_lsn", Integer)
    natural_gas = Column("natural_gas", Integer)
    power_storage = Column("power_storage", Integer)
    coal_and_lignite = Column("coal_and_lignite", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class ErcotLoad(Base):
    __tablename__ = "ercot_load"

    load = Column("load", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class ErcotLoadForecast(Base):
    __tablename__ = "ercot_load_forecast"

    load_forecast = Column("load_forecast", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    publish_time_utc = Column("publish_time_utc", DateTime, primary_key=True)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class IsoneFuelMix(Base):
    __tablename__ = "isone_fuel_mix"

    oil = Column("oil", Integer)
    coal = Column("coal", Integer)
    wind = Column("wind", Integer)
    wood = Column("wood", Integer)
    hydro = Column("hydro", Integer)
    other = Column("other", Integer)
    solar = Column("solar", Integer)
    refuse = Column("refuse", Integer)
    nuclear = Column("nuclear", Integer)
    natural_gas = Column("natural_gas", Integer)
    landfill_gas = Column("landfill_gas", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class IsoneLoad(Base):
    __tablename__ = "isone_load"

    load = Column("load", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class IsoneLoadForecast(Base):
    __tablename__ = "isone_load_forecast"

    load_forecast = Column("load_forecast", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    publish_time_utc = Column("publish_time_utc", DateTime, primary_key=True)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class MisoFuelMix(Base):
    __tablename__ = "miso_fuel_mix"

    coal = Column("coal", Integer)
    wind = Column("wind", Integer)
    other = Column("other", Integer)
    solar = Column("solar", Integer)
    imports = Column("imports", Integer)
    nuclear = Column("nuclear", Integer)
    natural_gas = Column("natural_gas", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class MisoLoad(Base):
    __tablename__ = "miso_load"

    load = Column("load", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class MisoLoadForecast(Base):
    __tablename__ = "miso_load_forecast"

    load_forecast = Column("load_forecast", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    publish_time_utc = Column("publish_time_utc", DateTime, primary_key=True)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class NyisoFuelMix(Base):
    __tablename__ = "nyiso_fuel_mix"

    wind = Column("wind", Integer)
    hydro = Column("hydro", Integer)
    nuclear = Column("nuclear", Integer)
    dual_fuel = Column("dual_fuel", Integer)
    natural_gas = Column("natural_gas", Integer)
    other_renewables = Column("other_renewables", Integer)
    other_fossil_fuels = Column("other_fossil_fuels", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class NyisoLoad(Base):
    __tablename__ = "nyiso_load"

    load = Column("load", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class NyisoLoadForecast(Base):
    __tablename__ = "nyiso_load_forecast"

    load_forecast = Column("load_forecast", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    publish_time_utc = Column("publish_time_utc", DateTime, primary_key=True)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class PjmFuelMix(Base):
    __tablename__ = "pjm_fuel_mix"

    gas = Column("gas", Integer)
    oil = Column("oil", Integer)
    coal = Column("coal", Integer)
    wind = Column("wind", Integer)
    hydro = Column("hydro", Integer)
    other = Column("other", Integer)
    solar = Column("solar", Integer)
    nuclear = Column("nuclear", Integer)
    storage = Column("storage", Integer)
    multiple_fuels = Column("multiple_fuels", Integer)
    other_renewables = Column("other_renewables", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class PjmLoad(Base):
    __tablename__ = "pjm_load"

    load = Column("load", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class PjmLoadForecast(Base):
    __tablename__ = "pjm_load_forecast"

    load_forecast = Column("load_forecast", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    publish_time_utc = Column("publish_time_utc", DateTime, primary_key=True)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class SppFuelMix(Base):
    __tablename__ = "spp_fuel_mix"

    coal = Column("coal", Integer)
    wind = Column("wind", Integer)
    hydro = Column("hydro", Integer)
    other = Column("other", Integer)
    solar = Column("solar", Integer)
    nuclear = Column("nuclear", Integer)
    waste_heat = Column("waste_heat", Integer)
    natural_gas = Column("natural_gas", Integer)
    diesel_fuel_oil = Column("diesel_fuel_oil", Integer)
    waste_disposal_services = Column("waste_disposal_services", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class SppLoad(Base):
    __tablename__ = "spp_load"

    load = Column("load", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


class SppLoadForecast(Base):
    __tablename__ = "spp_load_forecast"

    load_forecast = Column("load_forecast", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    publish_time_utc = Column("publish_time_utc", DateTime, primary_key=True)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


def table_name_to_model(table_name):
    table_mapping = {
        "caiso_fuel_mix": CaisoFuelMix,
        "caiso_load": CaisoLoad,
        "caiso_load_forecast": CaisoLoadForecast,
        "ercot_fuel_mix": ErcotFuelMix,
        "ercot_load": ErcotLoad,
        "ercot_load_forecast": ErcotLoadForecast,
        "isone_fuel_mix": IsoneFuelMix,
        "isone_load": IsoneLoad,
        "isone_load_forecast": IsoneLoadForecast,
        "miso_fuel_mix": MisoFuelMix,
        "miso_load": MisoLoad,
        "miso_load_forecast": MisoLoadForecast,
        "nyiso_fuel_mix": NyisoFuelMix,
        "nyiso_load": NyisoLoad,
        "nyiso_load_forecast": NyisoLoadForecast,
        "pjm_fuel_mix": PjmFuelMix,
        "pjm_load": PjmLoad,
        "pjm_load_forecast": PjmLoadForecast,
        "spp_fuel_mix": SppFuelMix,
        "spp_load": SppLoad,
        "spp_load_forecast": SppLoadForecast,
    }

    if table_name not in table_mapping:
        raise ValueError("Unable to find table")

    return table_mapping[table_name]
