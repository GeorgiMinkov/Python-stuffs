# encoding: utf-8
class MyException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
    
def foo():
    raise MyException("Some message")

def boo():
    try:
        foo()
    except MyException as e:
        print e
        raise
    except Exception as e:
        print e
        raise
    finally:
        print "This is finally block"
    
# def someFunc():
#     try:
#         import bira
#     except Import Error:
#         import json as bira


#     try:
#         import simplejson as json
#     except json as json

def printFile(file_name):
    f = open(file_name, 'r')
    for line in f:
        print line

    f.close()

def anotherFunction(a, b):
    if a > 10:
        return a + b
    else:
        # return anotherFunction # функциите са обекти
        return anotherFunction_some # няма компилатор, който още тук да ти каже, че е грешка, ще гръмне само ако влезе да търси променливата

def write_file(name):
    try:
        f = open(name, "w")
        for index in xrange(10):
            f.write("{}\n".format(index))
    except Exception as e:
        print e
    finally:
        f.close()

def read_file(name):
    f = None # по този начин махаме грешката, че f няма никаква стойност
    try:
        f = open(name, "r")
        for  line in f:
            print line 
    except Exception as e:
        print e
    finally:
        f.close()
# better versions
def write_file_better(name):
    with open(name, "w") as f:
        for index in xrange(10):
            f.write("{}\n".format(index))

def read_file_better(name):
    with open(name, "r") as f:
        for line in f:
            print line
if __name__ == '__main__':
    # printFile("file")
    # boo()
    # print anotherFunction(5, 3)

    # i = 10

    # try:
    #     i++
    # except SyntaxError as e:
    #     print e
    #     i += 10

    # print i
    
    # r = xrange(10)

    # while True:
    #     try:
    #         print r.next()
    #     except Exception as e:
    #         print e


    # r = iter(range(10))
    # while True:
    #     try: 
    #         print r.next()
    #     except Exception as e:
    #         print type(e), e
    #            break
    # write_file("someFile")
    # read_file("someBadFile")
    write_file_better("someGoodFile")
    read_file_better("someGoodFile")