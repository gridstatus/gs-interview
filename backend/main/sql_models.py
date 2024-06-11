from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


# details on why we use AsyncAttrs
# to make relationships work with async
# https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html#asyncio-orm-avoid-lazyloads
class Base(AsyncAttrs, DeclarativeBase):
    pass


class ErcotLoadForecast(Base):
    __tablename__ = "ercot_load_forecast"

    load_forecast = Column("load_forecast", Integer)
    interval_end_utc = Column("interval_end_utc", DateTime)
    publish_time_utc = Column("publish_time_utc", DateTime)
    interval_start_utc = Column("interval_start_utc", DateTime, primary_key=True)


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
