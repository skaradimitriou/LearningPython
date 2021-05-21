from objects.models.Animal import Animal
from objects.models.Cat import Cat
from objects.models.User import User

person = User('Stathis', 25)

print('{0} is {1} years old'.format(person.name, person.age))

cat = Cat('Tom', 'Cat', 4, True)

print('{0} is a {1} and has {2} legs'.format(cat.name, cat.category, cat.legs))
cat.makeSound()
