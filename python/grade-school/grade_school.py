class School:
    students={}
    def __init__(self):
        self.students={}

    def add_student(self, name, grade):
        if grade not in self.students.keys():
            self.students[grade]=[]
        self.students[grade].append(name)

    def roster(self):
        list=[]
        for key in sorted(self.students.keys()):
            list.extend(sorted(self.students[key]))
        return list

    def grade(self, grade_number):
        if grade_number not in self.students.keys():
            return []
        return [items for items in sorted(self.students.get(grade_number))]