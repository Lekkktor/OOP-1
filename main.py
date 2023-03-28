class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress \
                and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        average = []
        total = self.grades.values()
        for i in total:
            for b in i:
                average.append(b)
        return (sum(average) / len(average))

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} ' \
               f'\nСредняя оценка за домашние задания: {self.average_grade()} '\
               f'\nКурсы в процессе изучения: {self.courses_in_progress} ' \
               f'\nЗавершенные курсы: {self.finished_courses}'

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Не подходит'
        return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Не подходит'
        return self.average_grade() > other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Не подходит'
        return self.average_grade() < other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name} ' \
               f'\nФамилия: {self.surname} ' \
               f'\nСредняя оценка за лекции: {self.average_rate()}'

    def average_rate(self):
        average = []
        total = self.grades.values()
        for i in total:
            for b in i:
                average.append(b)
        return (sum(average) / len(average))

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Не подходит'
        return self.average_rate() == other.average_rate()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Не подходит'
        return self.average_rate() > other.average_rate()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Не подходит'
        return self.average_rate() < other.average_rate()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress \
                and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

lec_2 = Lecturer('Валерий', 'Равдин')
studentik = Student('Иван', 'Иванов', 'мужской')
studentik.courses_in_progress.append('Python')
studentik.courses_in_progress.append('OOP')
best_student = Student('Геннадий', "Петров", 'мужской')
best_student.courses_in_progress.append('Git')
best_student.courses_in_progress.append('Python')
lec_2.courses_attached.append('Python')
studentik.rate_hw(lec_2, 'Python', 7)
studentik.rate_hw(lec_2, 'Python', 7)
studentik.rate_hw(lec_2, 'Python', 7)
r = Reviewer('MARAT', 'MANSUROVICH')
r.courses_attached.append('Python')
r.rate_hw(studentik, 'Python', 8)
r.rate_hw(studentik, 'Python', 8)
r.rate_hw(studentik, 'Python', 8)
r.rate_hw(best_student, 'Python', 6)
r.rate_hw(best_student, 'Python', 8)
r.rate_hw(best_student, 'Python', 6)
lec_1 = Lecturer('Василий', 'Лекторов')
lec_1.courses_attached.append('OOP')
lec_1.courses_attached.append('Python')
studentik.rate_hw(lec_1, 'Python', 7)
studentik.rate_hw(lec_1, 'Python', 7)
studentik.rate_hw(lec_1, 'Python', 7)
studentik.rate_hw(lec_1, 'OOP', 4)
studentik.rate_hw(lec_1, 'OOP', 4)
studentik.rate_hw(lec_1, 'OOP', 4)
studentik.finished_courses.append('Введение в программирование')
best_student.finished_courses.append('Введение в программирование')
r.rate_hw(best_student, 'Python', 9)
r.rate_hw(best_student, 'Python', 8)
r.rate_hw(best_student, 'Python', 6)
print(lec_1)
print(r)
print(lec_2)
print(best_student)
print(studentik)
print(studentik.average_grade() > best_student.average_grade())
students = [best_student, studentik]
lectors = [lec_1, lec_2]


def average_grade_on_the_course(students, course):
    if not isinstance(students, list):
        return "Not list"
    all_average_grade = []
    for person in students:
        all_average_grade.extend(person.grades.get(course, []))
    if not all_average_grade:
        return "По такому курсу ни у кого нет оценок"
    return round(sum(all_average_grade) / len(all_average_grade), 2)

def average_grade_on_the_course(lectors, course):
    if not isinstance(lectors, list):
        return "Not list"
    all_average_grade = []
    for person in lectors:
        all_average_grade.extend(person.grades.get(course, []))
    if not all_average_grade:
        return "По такому курсу ни у кого нет оценок"
    return round(sum(all_average_grade) / len(all_average_grade), 2)

print(average_grade_on_the_course(students, 'Python'))
print(average_grade_on_the_course(lectors, 'Python'))