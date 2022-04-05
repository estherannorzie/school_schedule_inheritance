from school_schedule.student import Student
from school_schedule.high_school_student import HighSchoolStudent
from school_schedule.middle_school_student import MiddleSchoolStudent

#first instance
quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )
# print(quinn)
# print(dir(quinn))
# print(vars(quinn))

# quinn.add_class("Painting")
# quinn.get_num_classes()
# quinn.summary()

# second instance
claire = MiddleSchoolStudent(
                "Claire", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ],
                "Hogwarts"
            )

# claire.get_num_classes()
# print(claire.summary())
print(claire.school_name)

# # Extra:
# # - create a function that will return the student with more classes
# # - create a test for that function