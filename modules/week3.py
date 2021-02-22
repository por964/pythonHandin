class Course():

    def __init__(self, name, class_room, teacher, etcs, grade=0):
        self.name = name
        self.class_room = class_room
        self.teacher = teacher
        self.etcs = etcs
        self.grade = grade

    def __repr__(self):
        return 'Course: (%r, %r, %r,%r,%r)' % (self.name, self.class_room, self.teacher,
                                               self.etcs, self.grade)

    def __str__(self):
        return 'Course: {name}, classroom: {cr}, teacher: {tc}, ETCS: {et}, grade: {grade} '.format(
            name=self.name, cr=self.class_room, tc=self.teacher, et=self.etcs, grade=self.grade
        )

class Student():

    def __init__(self,name,gender,image_url,data_sheet):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def __repr__(self):
        return 'Name: (%r,%r,%r,%r)' % (self.name, self.gender,self.data_sheet,self.image_url)

    def __str__(self):
        return '{name} is {gender} and has no of courses: {data} and the URL to image is: {img}'.format(
            name=self.name, gender=self.gender,data=self.data_sheet,img=self.image_url
        )

    def __iter__(self):
        self.n = 0
        return self

    def get_img(self):
        return str(self.image_url)

    def get_avg_grade(self):
        lst = self.data_sheet.get_grades_as_list()
        return sum(lst)/len(lst)

    def ects_status(self):
        max = 150
        actual = 0
        for course in self.data_sheet.courses:
            actual += course.etcs
        status = actual / max
        return round(status * 100, 2)


class DataSheet():

    def __init__(self, courses=[]):
        self.courses = courses


    def get_grades_as_list(self):
        grades = []
        for course in self.courses:
            grades.append(course.grade)
        return grades

    def __repr__(self):
        str1 = ''
        for course in self.courses:
            str1 += str(course)+'\n'
            return str1

    def __repr__(self):
        return str(len(self.courses))

    def __str__(self):
        return 'DataSheet {data_sheet}'.format(data_sheet=self.courses)