import aiohttp
import asyncio
import logging

from aiohttp import ClientConnectionError

from pysunpower.sunpowermodel import SunPowerModel

LOGGER = logging.getLogger("__name__")


class SunPowerAsync:
    """Async SunPower REST Api Interface Class."""

    def __init__(self, ip: str, port: str = "80") -> None:
        self.base_url = f"http://{ip}:{port}"

    async def get_device_list(self) -> SunPowerModel:
        """Makes a query to /cgi-bin/dl_cgi?Command=DeviceList which is really the only endpoint that matters."""

        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}/cgi-bin/dl_cgi?Command=DeviceList"

            try:
                async with session.get(url) as response:
                    if response.status == 404:
                        # Valid address but wrong endpoint
                        # LOGGER.log(msg = f"Valid SunPower Endpoint not found at: {url}")
                        raise ConnectionError("Invalid URL")

                    json_data = await response.json(content_type=None)
                    return SunPowerModel(**json_data)

            except ClientConnectionError as e:
                raise e
            except Exception as e:
                print(e)
                LOGGER.error("Unhandled Exception: __line__" )
                raise Exception("Unknown")


async def main():
    sunpower = SunPowerAsync(ip="192.168.1.62", port="81")

    data = await sunpower.get_device_list()
    print(data)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
