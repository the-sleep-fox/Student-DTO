import aiohttp
import certifi
import ssl

class QuoteApiAdapter:
    def __init__(self, api_url: str, ssl_verify: bool = True):
        self.api_url = api_url
        self.ssl_verify = ssl_verify

    async def get_random_quote(self):
        ssl_context = ssl.create_default_context(cafile=certifi.where()) if self.ssl_verify else False
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url, ssl=ssl_context) as response:
                if response.status != 200:
                    raise ValueError(f"Failed to fetch quote: HTTP {response.status}")
                return await response.json()