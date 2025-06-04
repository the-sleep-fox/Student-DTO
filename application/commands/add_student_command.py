from domain.dtos.student_dto import StudentDTO

class AddStudentCommand:
    def __init__(self, student_service, quote_service):
        self.student_service = student_service
        self.quote_service = quote_service

    async def execute(self):
        try:
            name = input("Enter student name: ")
            grade = input("Enter student grade (0-100): ")
            student_dto = StudentDTO(name=name, grade=int(grade))
            student = self.student_service.add_student(student_dto)
            print(f"Student {student.name} added successfully!")
            quote = await self.quote_service.get_random_quote()
            print(f"Motivational Quote: {quote.content} - {quote.author}")
        except ValueError as e:
            print(f"Error: {e}")