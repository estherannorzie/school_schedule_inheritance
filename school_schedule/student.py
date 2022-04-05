class Student:
    """
    Attributes:
    # name
    # grade level
    # classes_list

    Methods:
    - add_class()
    - get_num_classes()
    - summary()
    """
    def __init__(self, name, grade_level, class_list, school_name = "Ada Developers Academy"):
        self.name = name
        self.grade_level = grade_level
        self.class_list = class_list
        self.school_name = school_name

    def add_class(self, class_name):
        self.class_list.append(class_name)
        return self.class_list

    def get_num_classes(self):
        return len(self.class_list)

    def summary(self):
        student_summary = f"{self.name} is a {self.grade_level}. \
        \n Class list: {self.class_list}"
        return student_summary

