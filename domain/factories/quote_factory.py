from domain.dtos.quote_dto import QuoteDTO

class QuoteFactory:
    @staticmethod
    def create_quote(quote_data: dict):
        if not quote_data.get("content") or not quote_data.get("author"):
            raise ValueError("Invalid quote data")
        return QuoteDTO(content=quote_data["content"], author=quote_data["author"])