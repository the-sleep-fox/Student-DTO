class ViewStudentsCommand:
    def __init__(self, student_service):
        self.student_service = student_service

    async def execute(self):
        try:
            students = self.student_service.get_all_students()
            if not students:
                print("No students found.")
                return
            print("\nStudent Records:")
            for student in students:
                print(f"ID: {student.id}, Name: {student.name}, Grade: {student.grade}")
        except Exception as e:
            print(f"Error: {e}")