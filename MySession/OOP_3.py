class User:
    def __init__(self, name):
        self.name = name
        self._email = "test@test.com"
        self.__password = 123456
    def login(self, userPassword):
        if self.__password == userPassword :
            return 'login success'
        else:
            return 'login fail'

me = User("Saber")
print(me.login(123456))

print(me._User__password)