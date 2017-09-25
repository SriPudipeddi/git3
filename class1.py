class Student(object):
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def display_info(self):
        print "The name is %s and ssn is %d" % (self.name, self.ssn)


s1 = Student("Euler", 123456789)
s1.display_info()
