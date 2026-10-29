class Person:
    status = "True"
    def __init__(self,name,family,age):
        self.name = name
        self.family = family
        self.age = age
    def show_full_name(self):
        return f"{self.name} {self.family} is {self.age} years old "

    @classmethod
    def show(cls):
        return Person.status

class User(Person):
    pass


me = Person("Saber","Galedar",21)
you = User("Arash","Galedar", 31)

print(me.name)
print(you.show_full_name())

print(User.show())
print(User.status)

