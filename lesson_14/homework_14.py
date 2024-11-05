class Student:
    def __init__(self, first_name, surname, age, average_rating):

        self.first_name = first_name
        self.surname = surname
        self.age = age
        if average_rating < 0:
            self.average_rating = 0.1
            print('Average rating should be more than 0')
        else:
            self.average_rating = average_rating

    def change_average_rating(self, value):
        if value < 0:
            print('Average rating should be more than 0')
        else:
            print(f'For {self.first_name} change average rating from {self.average_rating} to {value}')
            self.average_rating = value

    def info(self):
        print(f'Name {self.first_name}, surname {self.surname},  age {self.age} average rating is {self.average_rating}')


student_1 = Student('Garry', 'Potter', 13, 34)
student_2 = Student('Hermione', 'Granger', 12, 99)
student_3 = Student('Ron', 'Weasley', 12, 41)
student_4 = Student(first_name='Dudley', surname='Dursley', age=13, average_rating=-13)
student_1.change_average_rating(99)
student_1.info()
student_4.change_average_rating(100)
student_4.info()

