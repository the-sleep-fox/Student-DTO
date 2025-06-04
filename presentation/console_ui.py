from application.commands.add_student_command import AddStudentCommand
from application.commands.edit_student_command import EditStudentCommand
from application.commands.view_students_command import ViewStudentsCommand
from domain.dtos.student_dto import StudentDTO

class ConsoleUI:
    def __init__(self, student_service, quote_service):
        self.student_service = student_service
        self.quote_service = quote_service
        self.commands = {
            "add": AddStudentCommand(student_service, quote_service),
            "edit": EditStudentCommand(student_service),
            "view": ViewStudentsCommand(student_service),
            "exit": None
        }

    async def run(self):
        while True:
            print("\nCommands: add, edit, view, exit")
            command = input("Enter command: ").lower()
            if command == "exit":
                break
            if command in self.commands:
                await self.commands[command].execute()
            else:
                print("Invalid command")