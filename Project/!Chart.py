import random
import matplotlib.pyplot as plt

Student = ['Amir','Hosein','Reza','Ali']
Counter = Student
for i in range(0,4):
    Score = random.randrange(1,21)
    print(Student[0],Score)
    Score = random.randrange(1,21)
    print(Student[1],Score)
    Score = random.randrange(1,21)
    print(Student[2],Score)
    Score = random.randrange(1,21)
    print(Student[3],Score)

# matplotlib inline
plt.bar(range(0,5),Student)

