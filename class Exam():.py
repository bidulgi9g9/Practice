class Exam():
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result
          
print(Exam.add(2))
print(Exam.add(3))
