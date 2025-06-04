from domain.factories.student_factory import StudentFactory
from domain.dtos.student_dto import StudentDTO

class StudentService:
    def __init__(self, repository):
        self.repository = repository

    def add_student(self, student_dto: StudentDTO):
        student = StudentFactory.create_student(student_dto)
        self.repository.add(student)
        return student

    def edit_student(self, student_id: int, student_dto: StudentDTO):
        student = StudentFactory.create_student(student_dto)
        self.repository.update(student_id, student)
        return student

    def get_all_students(self):
        return self.repository.get_all()