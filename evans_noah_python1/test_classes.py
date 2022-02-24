from arthmetic import *;
'''
Classes can represent real-world objects or abstract ideas. After defining a class, you use it by making an instance, or object,of the class. You can make as many instances as you want from one class.
As an example, you might use a class to represent a website user. The class would have attributes associated with the user’s username, password, registration date, and more. Methods would define the actions the user could take, such as registering, authenticating, logging in, and logging out. You could then make one instance for each user who registers on the site.
Many external libraries are written as classes, so learn-ing to work with classes makes it easier to work with many existing projects.
'''

ar = Arithmetic()
print(ar.add())
print(ar.divide())
print(ar.remainder())
ar.print_self()
print('\n')
#TODO: create several more instance of the Arithmetic class and add different values
tenandfive = Arithmetic(10, 5)
print(tenandfive.add())
print(tenandfive.divide())
print(tenandfive.remainder())
print('\n')
fiveandten = Arithmetic(5, 10)
print(fiveandten.add())
print(fiveandten.divide())
print(fiveandten.remainder())
print('\n')
threemillionandsix = Arithmetic(3000000, 6)
print(threemillionandsix.add())
print(threemillionandsix.multiply())
print(threemillionandsix.divide())
print(threemillionandsix.subtract())
print(threemillionandsix.remainder())
print('\n')

thirteenandfourteen = Arithmetic(13, 14)
print(thirteenandfourteen.add())
print(thirteenandfourteen.multiply())
print(thirteenandfourteen.divide())
print(thirteenandfourteen.subtract())
print(thirteenandfourteen.remainder())
print('\n')

x = 2
threeandtwocubed = Arithmetic(3, x**3)
print(threeandtwocubed.add())
print(threeandtwocubed.multiply())
print(threeandtwocubed.divide())
print(threeandtwocubed.subtract())
print(threeandtwocubed.remainder())
print('\n')

estimateofpiand6billion = Arithmetic(3.14159265359, 6000000000)
print(estimateofpiand6billion.add())
print(estimateofpiand6billion.multiply())
print(estimateofpiand6billion.divide())
print(estimateofpiand6billion.subtract())
print(estimateofpiand6billion.remainder())