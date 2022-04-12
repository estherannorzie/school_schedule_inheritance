from .student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation
    
    def summary(self):
        student_summary = super().summary()
        transporation_message = self.display_transporation()
        return "\n".join((student_summary, transporation_message))
    
    def display_transporation(self):
        has_message = "has" if self.gets_transportation else "doesn't have"
        return f"{self.name} {has_message} transportation"