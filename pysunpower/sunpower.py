"""Sunpower module def."""
from __future__ import annotations

import asyncio
import logging

import aiohttp
from aiohttp import ClientConnectionError

from pysunpower.sunpowermodel import SunPowerModel

LOGGER = logging.getLogger("__name__")


class InvalidEndpointException(Exception):
    """A valid connection made to an invalid Endpoint."""


class ConnectionException(Exception):
    """Any failure to connect to sunpower PVS."""


class UnknownException(Exception):
    """An unknown exception occurred."""


class SunPower:
    """Async SunPower REST Api Interface Class."""

    def __init__(self, ip: str, port: str = "80") -> None:
        """Initialize Sunpower class."""
        self.command_url = f"http://{ip}:{port}/cgi-bin/dl_cgi?Command="
        self.device_data: SunPowerModel | None = None

    async def get_device_list(self) -> SunPowerModel:
        """Make a query to /cgi-bin/dl_cgi?Command=DeviceList which is really the only endpoint that matters."""
        async with aiohttp.ClientSession() as session:
            url = f"{self.command_url}DeviceList"

            try:
                async with session.get(url) as response:
                    if response.status == 404:
                        # Valid address but wrong endpoint
                        LOGGER.debug("Valid SunPower Endpoint not found at: %s", url)
                        raise InvalidEndpointException(f"Invalid URL: {url}")

                    json_data = await response.json(content_type=None)
                    self.device_data = SunPowerModel(**json_data)
                    return self.device_data

            except ClientConnectionError as e:
                raise ConnectionException(e)
            except Exception as e:
                LOGGER.error("Unhandled Exception: __line__")
                raise UnknownException(e)


async def main() -> None:
    """Define main function."""
    sp = SunPower(ip="192.168.1.62", port="81")

    data = await sp.get_device_list()
    print(data)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
