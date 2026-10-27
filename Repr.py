class User:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def __repr__(self):
        return f'{self.name}, {self.family}'


me = User("Saber", "Galedar")

print(me)  # Saber, Galedar
print(type(me))  # <class '__main__.User'>
