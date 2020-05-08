class Garden:
    STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
    PLANTS = {'C': 'Clover', 'G': 'Grass', 'R': 'Radishes', 'V': 'Violets'}
    def __init__(self, diagram, students=None):
        if(students == None):
            self.students = self.STUDENTS
        else:
            self.students = students
        self.diagram = diagram.splitlines()
        self.students = sorted(self.students)

    def plants(self, name):
        planted = []
        index = self.students.index(name)
        for i in range(2):
            for j in range(index+index, index+index+2):
                planted.append(self.PLANTS[self.diagram[i][j]])   
        return planted