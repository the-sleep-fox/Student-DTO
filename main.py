import asyncio
import json
from presentation.console_ui import ConsoleUI
from application.services.student_service import StudentService
from application.services.quote_service import QuoteService
from data_access.repositories.student_repository import StudentRepository
from data_access.adapters.quote_api_adapter import QuoteApiAdapter
from domain.factories.quote_factory import QuoteFactory

async def main():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print("Error: config.json not found. Using default configuration.")
        config = {"quote_api_url": "https://zenquotes.io/api/random", "ssl_verify": True}
    except json.JSONDecodeError:
        print("Error: Invalid config.json format. Using default configuration.")
        config = {"quote_api_url": "https://zenquotes.io/api/random", "ssl_verify": True}

    repository = StudentRepository("students.json")
    quote_adapter = QuoteApiAdapter(config["quote_api_url"], config["ssl_verify"])
    quote_factory = QuoteFactory()
    student_service = StudentService(repository)
    quote_service = QuoteService(quote_adapter, quote_factory)
    ui = ConsoleUI(student_service, quote_service)
    await ui.run()

if __name__ == "__main__":
    asyncio.run(main())