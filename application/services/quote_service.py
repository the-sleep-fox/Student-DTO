class QuoteService:
    def __init__(self, quote_adapter, quote_factory):
        self.quote_adapter = quote_adapter
        self.quote_factory = quote_factory

    async def get_random_quote(self):
        try:
            quote_data = await self.quote_adapter.get_random_quote()
            if isinstance(quote_data, list) and len(quote_data) > 0:
                quote_data = {"content": quote_data[0]["q"], "author": quote_data[0]["a"]}
            return self.quote_factory.create_quote(quote_data)
        except Exception as e:
            print(f"Error fetching quote: {e}. Returning default quote.")
            return self.quote_factory.create_quote({"content": "Keep going!", "author": "Default"})