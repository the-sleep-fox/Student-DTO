Description
The Student Record Management System is a simple console-based Python app for managing student records. It lets users add, edit, and view students, saving data in a JSON file (students.json). When a student is added, it fetches a motivational quote from an API (zenquotes.io) to show the user. The app is built with clear, organized code using a layered structure (UI, services, domain, and data).
Key features:

Add, edit, and view student records with checks for valid names (not empty) and grades (0–100).
Display random quotes from an API, with a default quote ("Keep going!" - Default) if the API fails.
Save student data in a JSON file.
Use aiohttp for fast API calls.
Log errors to test_logs.txt for easy debugging.
Test with unittest to ensure everything works, including error cases.

The app uses smart design ideas:

DTOs: StudentDTO and QuoteDTO make data easy to pass around.
Commands: Actions like adding or editing students are handled by separate command classes.
Adapter: QuoteApiAdapter connects to the API.
Factories: StudentFactory and QuoteFactory create and check data.
Clean Code: Business rules are separate from UI and API code, following SOLID principles.

Settings are stored in config.json (API URL and SSL options). If the file is missing, it uses defaults. The app is secure with certifi for HTTPS and flexible to add new features, like different APIs or storage, without changing the main code.
