from domain.entities.student import Student
from domain.dtos.student_dto import StudentDTO
import uuid

class StudentFactory:
    @staticmethod
    def create_student(student_dto: StudentDTO):
        name = Student.validate_name(student_dto.name)
        grade = Student.validate_grade(student_dto.grade)
        return Student(id=int(uuid.uuid4().int & (1<<31)-1), name=name, grade=grade)