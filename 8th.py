class ParentClass(object):
    i = 1
    j = 2
    k = 3

    def __init__(self, message):
        print message
        print "This is the constructor"

    def display_func(self):
        print ParentClass.i
        print ParentClass.j
        print ParentClass.k
        print ChildClass.r
        print ChildClass.s
        print ChildClass.t


class ChildClass(ParentClass):
    r = 4
    s = 5
    t = 6

    def __init__(self, message):
        self.message = message
        print "This is the initializer"
        ParentClass.__init__(self, message)

if __name__ == '__main__':
    message = "Calling the constructor now"
    child = ChildClass(message)
    child.display_func()
