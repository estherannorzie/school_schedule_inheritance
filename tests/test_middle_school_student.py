import pytest
# from school_schedule.middle_school_student import MiddleSchoolStudent

# def test_new_valid_middle_school_student_gets_transportation():
#     # Arrange
#     name = "Ellis"
#     grade = "junior"
#     classes = ["Painting"]

#     # Act
#     ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

#     assert ellis.name == name
#     assert ellis.grade == grade
#     assert ellis.classes == classes
#     assert len(ellis.classes) == 1
#     assert ellis.gets_transportation

from school_schedule.middle_school_student import MiddleSchoolStudent


def test_new_valid_middle_school_student_with_defaults():
    # act
    name = "Clara"
    grade = "junior"
    classes = [
        "Art",
        "Spanish II",
        "Geography",
        "World History",
        "Precalculus",
        "Chemistry"
    ]

    # arrange
    clara = MiddleSchoolStudent(name, grade, classes)

    # assert
    assert clara.name == name
    assert clara.grade == grade
    assert clara.classes == classes

# @pytest.mark.skip()
def test_middle_school_student_summary_with_transportation():
    # act
    name = "Tyler"
    grade = "freshman"
    classes = [
        "Japanese",
        "Psychology",
        "Economics",
        "Physics",
        "Geometry",
        "English"
    ]
    gets_transportation = True

    # arrange
    tyler = MiddleSchoolStudent(name, grade, classes, gets_transportation)
    summary = tyler.summary()

    # assert
    assert summary == "Tyler is a freshman enrolled in 6 classes: Japanese, Psychology, Economics, Physics, Geometry, English\nTyler has transportation"

@pytest.mark.skip()
def test_middle_school_student_summary_without_transportation():
    # act


    # arrange


    # assert
    pass