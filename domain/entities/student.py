
class Student:
    def __init__(self, id: int, name: str, grade: int):
        self.id = id
        self.name = name
        self.grade = grade

    @staticmethod
    def validate_name(name: str):
        if not name or name.strip() == "":
            raise ValueError("Name cannot be empty")
        return name.strip()

    @staticmethod
    def validate_grade(grade: int):
        if not isinstance(grade, int) or grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")
        return grade