import json
import os
from domain.entities.student import Student

class StudentRepository:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.students = self.load_students()

    def load_students(self):
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [Student(**student) for student in data]
        except:
            return []

    def save_students(self):
        with open(self.file_path, 'w') as file:
            json.dump([vars(student) for student in self.students], file, indent=4)

    def add(self, student: Student):
        self.students.append(student)
        self.save_students()

    def update(self, student_id: int, student: Student):
        for i, s in enumerate(self.students):
            if s.id == student_id:
                self.students[i] = student
                self.save_students()
                return
        raise ValueError("Student not found")

    def get_all(self):
        return self.students