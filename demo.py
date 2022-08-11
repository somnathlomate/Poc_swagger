import random

ans = {random.randint(1,200) for item in range(10)}
print(ans,len(ans))

import sys
sys.exit(0)

class MyArray:
    pass        # array --> mera ka --

class NdArray:
    pass


#Array --> java/python/donnet/php -->
    #conti -- hom --> update/read ---> cannot grow -- cannot shrink up


def print_star(funref):
    def inner(*args):
        print(funref)
        if len(args)==0:
            print('Invalid Function Params')
        else:
            funref(*args)
    return inner


def sample_code_one(*args):
    x = args[0]*args[1]
    while x:
        print('one_code',x)
        x = x - 1

def sample_code_two(*args):
    x = args[0]
    while x:
        print('one_two', x)
        x = x - 1

@print_star
def sample_code_three(*args):
    x = args[0]*args[1]*args[2]
    while x:
        print('one_three', x)
        x = x - 1


sample_code_three(2,3,4)



import sys
sys.exit(0)
#higher order function --> which accepts function ref as param -- return funref

def type_check(funref):
    def business_calling(x,n1,n2):
        if type(n1) == int and type(n2) == int:
            result = funref(x,n1,n2)
            return result
        else:
            print('Invalid Params...!')
    return business_calling




class Calculator:
    @type_check
    def addition(self,num1,num2):
        #if type(num1) == int and type(num2) == int:
            return num1 + num2
       # else:
        #    print('Invalid Numbers...')

    @type_check
    def substraction(self,num1,num2):
        return num1 - num2

    @type_check
    def multiplication(self, num1, num2):
        return num1 * num2



cal = Calculator()
ans1  = cal.addition(1002,"A")
ans2 = cal.substraction(203,3)

print(ans1)
print(ans2)

import sys
sys.exit(0)







'''
        property --> 
        decorators -->
        
'''


# values =[random.randint(1,1000) for item in range(100)]
# print(values)
# print(max(values))
# print(min(values))
# print(sum(values))
# print(map)
# print(filter)




class Employee:
    count = 0                                       #class Variable
    EMP_ROLE = ["SE", "LEAD", "MANAGER", "SSE"]     #class Variable
    EMP_GEN = ["M", "F"]                            #class Variable         #EMP_GEN[random.randomint(0,1)]

    def __init__(self,eid,efnm,elastnm,erol,esal,egen):      #constructor
        self.empId = eid
        self.firstName = efnm
        self.lastName = elastnm
        self.empRole = erol
        self.empSalary = esal
        self.empGender = egen
        #self.empEmail = self.firstName+"."+self.lastName+"@gmail.com"

    @property
    def empFullName(self):
        if self.empGender == "M":
            return "Mr." + self.firstName + " " + self.lastName
        else:
            return "Miss" + self.firstName + " " + self.lastName

    @property
    def empEmail(self):     # no need to explicitly give a call to the this --> ya method --> as a property...
        return self.firstName + "." + self.lastName + "@gmail.com"

    def __str__(self):                              #obj repr
        return f'''\n {self.__dict__}'''

    def __repr__(self):                             #obj iterable of
        return str(self)

    @classmethod
    def get_employee_instance(cls):                     #class Method
        Employee.count = Employee.count + 1
        emp = cls(eid=Employee.count,efnm=f"AAAA{Employee.count}",elastnm = f'''XXXYYY{Employee.count}''',
                  erol=Employee.EMP_ROLE[random.randint(0,len(Employee.EMP_ROLE)-1)],
                  esal=random.randint(10000,50000),
                  egen=Employee.EMP_GEN[random.randint(0,1)])

        return emp


e1 = Employee.get_employee_instance()
e2 = Employee.get_employee_instance()


print(e1)
print(e2)

print(e1.empEmail)
print(e2.empEmail)

e1.firstName = "Yogesh"
e1.lastName = "Chame"
e1.empGender = "M"
print(e1.empEmail)
print(e1.empFullName)



import sys
sys.exit(0)


employees = [Employee.get_employee_instance() for item in range(10)]
print(employees)

e1 = employees[0]    # first employee -->
# print(e1.lastName)
# print(e1.firstName)
# print(e1.empEmail)  # Access  ???
# print(e1.empFullName)   # Emp --> full --> name --> runtime cal -->

print('This is normal approach...!------------')
sumOfSalaries = 0.0
for emp in employees:
    sumOfSalaries = sumOfSalaries + emp.empSalary
    print(emp.firstName,emp.lastName,emp.empFullName,emp.empEmail)  # for all emps

print('Sum --',sumOfSalaries)
print("Avg salary : ",sumOfSalaries/len(employees))
print('------------------------------')


print('using lambda --')

from functools import reduce

result =reduce(lambda x1,x2 :  x1.empSalary+x2.empSalary if type(x1) == Employee else x1 + x2.empSalary,employees)/len(employees)
print('AVG --> ',result)
#print('USing lambda Sum --',result)
#print("Using Lambda Avg salary : ",result/len(employees))
#print('------------------------------')



emplist = list(map(lambda emp : emp.empSalary*1.10 if emp.empRole=='MANAGER' else emp.empSalary,employees))
print(emplist)


#e1 = Employee.get_employee_instance()
#e2 = Employee.get_employee_instance()
#print(e1)
#print(e2)

import sys
sys.exit(0)

values = [12,30,4,5,5,6,62,3,56,6]  # what is the n here..

n = len(values)
print('original leg --> ',n)

finalList = list(map(lambda x : "B" if x%3==0 else "A",values))

print('-------------')
#finalList = list(filter(lambda x : x if x%3==0 else "B",values))
#print(finalList)

n = len(finalList)
print('finallist leg --> ',n)
