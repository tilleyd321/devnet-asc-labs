from simpleClass import *
#from fileName import className
#from file: simpleClass.py import all classes
def main():
    print("instancing SimpleClass")
    a = SimpleClass(100)
    b = SimpleClass(200)
    c = AnotherClass()
    a.SimpleClassReportMethod()
    b.SimpleClassReportMethod()
   

if __name__ == "__main__":
    main()