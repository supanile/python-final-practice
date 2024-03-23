class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def __str__(self):
        return f"Person[name= {self.name}, address= {self.address}]"


class Student(Person):
    def __init__(self, name, address, program, fee):
        super().__init__(name, address)
        self.program = program
        self.fee = max(fee, 0)  # ตรวจสอบค่า fee ให้ไม่ต่ำกว่า 0

    def getProgram(self):
        return self.program

    def setProgram(self, program):
        self.program = program

    def getFee(self):
        return self.fee

    def setFee(self, fee):
        self.fee = max(fee, 0)  # ตรวจสอบค่า fee ให้ไม่ต่ำกว่า 0

    def __str__(self):
        return f"Student[{super().__str__()}, program= {self.program}, fee= {self.fee}]"

s1 = Student("Titipong Keawkhum", "KMITL", "MATH", 19000)

s1.setName("Titipong pond Keawkhum")
s1.setAddress("Saimai")

print(s1)
print("Name:", s1.getName())
print("Address:", s1.getAddress())
print("Program:", s1.getProgram())
print("Fee:", s1.getFee())
