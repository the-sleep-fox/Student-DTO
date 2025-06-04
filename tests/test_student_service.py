import unittest
from application.services.student_service import StudentService
from data_access.repositories.student_repository import StudentRepository
from domain.dtos.student_dto import StudentDTO

class TestStudentService(unittest.TestCase):
    def setUp(self):
        self.repository = StudentRepository("test_students.json")
        self.service = StudentService(self.repository)

    def test_add_student(self):
        student_dto = StudentDTO(name="John Doe", grade=85)
        student = self.service.add_student(student_dto)
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.grade, 85)

    def test_invalid_grade(self):
        student_dto = StudentDTO(name="Jane Doe", grade=101)
        with self.assertRaises(ValueError):
            self.service.add_student(student_dto)

if __name__ == "__main__":
    unittest.main()