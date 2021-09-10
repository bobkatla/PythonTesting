import datetime

now = datetime.datetime.now()


class Student:
    def __init__(self, year_of_birth, name):
        if type(year_of_birth) is not int or year_of_birth < 0 or year_of_birth > now.year:
            raise Exception("Invalid birth year")
        self.__year_of_birth = year_of_birth
        self.__name = name

    def get_name(self):
        return self.__name

    def get_age(self):
        return now.year - self.__year_of_birth


if __name__ == '__main__':
    student_1 = Student(2021, 'Huy')
    print(student_1.get_name())
    print(student_1.get_age())
