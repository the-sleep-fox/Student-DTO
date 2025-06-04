from domain.dtos.student_dto import StudentDTO

class EditStudentCommand:
    def __init__(self, student_service):
        self.student_service = student_service

    async def execute(self):
        try:
            student_id = input("Enter student ID to edit: ")
            name = input("Enter new student name: ")
            grade = input("Enter new student grade (0-100): ")
            student_dto = StudentDTO(name=name, grade=int(grade))
            student = self.student_service.edit_student(int(student_id), student_dto)
            print(f"Student ID {student.id} updated successfully! Name: {student.name}, Grade: {student.grade}")
        except ValueError as e:
            print(f"Error: {e}")