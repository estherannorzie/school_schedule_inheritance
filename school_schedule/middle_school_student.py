from .student import Student

class MiddleSchoolStudent(Student):
    """
    Track whether the student receives school 
    transportation using the boolean attribute gets_transportation
    (can be set in the constructor, defaults to False)
    Update the summary method to include information about 
    the student's transportation status
    attr: transportation BOOL, summary
    """
    def __init__(self, name, grade_level, class_list, school_name, gets_transportation = False):
        super().__init__(name, grade_level, class_list, school_name)
        self.gets_transportation = gets_transportation

    def summary(self):
        student_summary = super().summary()
        middle_school_summary = f"{student_summary}\n Rides bus? {self.gets_transportation}"
        return "\n".join((student_summary, middle_school_summary))

