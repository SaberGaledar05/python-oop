class User:
    active_count = 0
    logged_users = list()
    allowed_users = ["Ali", "Saber", "Mohammad"]

    def __init__(self, user_name, user_family):
        if user_name in User.allowed_users:
            self.name = user_name
            self.family = user_family
            User.logged_users.append(user_name)
            User.active_count += 1
            print(f"{user_name} logged in")
        else:
            raise ValueError(f"User {user_name} has blocked")

    def log_out(self):
        if self.name in User.logged_users:
            User.logged_users.remove(self.name)
            print(f"{self.name} logged out")
            User.active_count -= 1
        else:
            print(f"{self.name} has logged out before")

    @classmethod
    def info(cls):
        print(User.logged_users)
        print(User.active_count)
        print(Saber.allowed_users)

    @classmethod
    def from_string(cls, string_data):
        data = string_data.split(",")
        return cls(data[0], data[1])


print(f'Active users: {User.active_count}')

Saber = User("Saber", "Galedar")

Ali = User("Ali", "Golpoor")

print(f'Active users: {User.active_count}')

Saber.log_out()
Saber.log_out()

print(User.logged_users)
print(f'Active users: {User.active_count}')

print(Saber.allowed_users)
User.allowed_users = ["   ", "Saber", "Mohammad"]
print(Saber.allowed_users)
Saber.allowed_users = ["   ", "     ", "Mohammad"]
print(User.allowed_users)
print(Saber.allowed_users)

User.info()

# print(dict.fromkeys([1,2,3],["unknown"]))

new_user = User("Mohammad", "Golpoor")
print(new_user.name, new_user.family)
