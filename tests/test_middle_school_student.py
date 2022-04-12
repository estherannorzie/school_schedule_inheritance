import pytest
from school_schedule.middle_school_student import MiddleSchoolStudent

# @pytest.mark.skip()
def test_new_valid_middle_school_student_gets_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.gets_transportation

# @pytest.mark.skip()
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
def test_new_valid_middle_school_student_displays_transportation():
    # act
    name = "Mink"
    grade = "freshman"
    classes = [
        "Cooking",
    ]

    # arrange
    mink = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)
    result = mink.display_transporation()

    # assert
    assert result
    assert result == "Mink has transportation"

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

    # arrange
    tyler = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)
    summary = tyler.summary()

    # assert
    assert summary == "Tyler is a freshman enrolled in 6 classes: Japanese, Psychology, Economics, Physics, Geometry, English\nTyler has transportation"

# @pytest.mark.skip()
def test_middle_school_student_summary_without_transportation():
    # act
    name = "Mona"
    grade = "senior"
    classes = [
        "ACT Prep",
        "Creative Writing",
        "Sociology",
        "Environmental Science",
        "Psychology",
        "Geology"
    ]

    # arrange
    mona = MiddleSchoolStudent(name, grade, classes)
    summary = mona.summary()

    # assert
    assert summary == "Mona is a senior enrolled in 6 classes: ACT Prep, Creative Writing, Sociology, Environmental Science, Psychology, Geology\nMona doesn't have transportation"