import unittest
import asyncio
import logging
from unittest.mock import AsyncMock
from application.services.quote_service import QuoteService
from data_access.adapters.quote_api_adapter import QuoteApiAdapter
from domain.factories.quote_factory import QuoteFactory
from domain.dtos.quote_dto import QuoteDTO

# Настройка логирования
logging.basicConfig(filename='test_logs.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class TestQuoteService(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.mock_adapter = AsyncMock(spec=QuoteApiAdapter)
        self.quote_factory = QuoteFactory()
        self.quote_service = QuoteService(self.mock_adapter, self.quote_factory)
        logging.info("Setting up TestQuoteService")

    async def test_get_random_quote_zenquotes_format(self):
        logging.info("Running test_get_random_quote_zenquotes_format")
        self.mock_adapter.get_random_quote.return_value = [
            {"q": "Stay positive, work hard, make it happen.", "a": "Unknown"}
        ]
        quote = await self.quote_service.get_random_quote()
        self.assertIsInstance(quote, QuoteDTO)
        self.assertEqual(quote.content, "Stay positive, work hard, make it happen.")
        self.assertEqual(quote.author, "Unknown")
        logging.info("test_get_random_quote_zenquotes_format passed")

    async def test_get_random_quote_standard_format(self):
        logging.info("Running test_get_random_quote_standard_format")
        self.mock_adapter.get_random_quote.return_value = {
            "content": "Stay positive, work hard, make it happen.",
            "author": "Unknown"
        }
        quote = await self.quote_service.get_random_quote()
        self.assertIsInstance(quote, QuoteDTO)
        self.assertEqual(quote.content, "Stay positive, work hard, make it happen.")
        self.assertEqual(quote.author, "Unknown")
        logging.info("test_get_random_quote_standard_format passed")

    async def test_invalid_quote_data(self):
        logging.info("Running test_invalid_quote_data")
        self.mock_adapter.get_random_quote.return_value = {"content": "", "author": ""}
        quote = await self.quote_service.get_random_quote()
        self.assertIsInstance(quote, QuoteDTO)
        self.assertEqual(quote.content, "Keep going!")
        self.assertEqual(quote.author, "Default")
        logging.info("test_invalid_quote_data passed")

    async def test_api_failure(self):
        logging.info("Running test_api_failure")
        self.mock_adapter.get_random_quote.side_effect = ValueError("Failed to fetch quote")
        quote = await self.quote_service.get_random_quote()
        self.assertIsInstance(quote, QuoteDTO)
        self.assertEqual(quote.content, "Keep going!")
        self.assertEqual(quote.author, "Default")
        logging.info("test_api_failure passed")

if __name__ == "__main__":
    unittest.main()