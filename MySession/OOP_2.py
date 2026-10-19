class User:
    def __init__(self, name=None, family=None, age=None, email=None, password=None):
        self.userName = name
        self.userFamily = family
        self.userAge = age
        self.userEmail = email
        self.userPass = password
    def buyCourses(self):
         if None in (self.userName , self.userFamily , self.userAge , self.userEmail , self.userPass) :
            return f'{self.userName} can not buy all courses , please complete your account information'
         else :
             return f'{self.userName} can buy all courses'
    def showInfo(self):
        age = self.userAge
        if age is None :
            age = "unknown"
        return f'{self.userName} {self.userFamily} is {age} years old , Email : {self.userEmail} and Password : {self.userPass}'
