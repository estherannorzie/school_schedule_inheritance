from .student import Student

class HighSchoolStudent(Student):
    """
    attr: has_parking_privileges=False, clubs
    parent attr:
        self.name = name
        self.grade_level = grade_level
        self.class_list = class_list
        self.school_name = school_name

    methods: join_club, summary
    """
    def __init__(self, name, grade_level, class_list,
                clubs=None, has_parking_privileges=False):
        super().__init__(name, grade_level, class_list,)
        self.has_parking_privileges = has_parking_privileges
        self.clubs = clubs 

    def join_club(self, club_name):
        self.club.append(club_name)

    #method overriding
    def summary(self):
        """
        Update the summary method to include information 
        about the student's parking abilities and club memberships
        """
        student_summary = super().summary()

        print(f"{student_summary}\n Can park? {self.has_parking_privileges} \nClubs: {self.clubs}")
