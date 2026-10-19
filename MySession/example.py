from MySession.OOP_2 import User

ali = User('Ali','Safari')
mehdi = User('Mehdi','moradi', 18 , 'mehdi0123@gmail.com', "kkg1256")
saber = User('Saber', 'Galedar', 21 , 'Saber65456@gmail.com', "123456789" )

print(saber.showInfo())
print(ali.showInfo())
print(mehdi.showInfo())

print(saber.buyCourses())
print(ali.buyCourses())
print(mehdi.buyCourses())
