## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## is-a object
class Dog(Animal):
	
	def __init__(self, name):
		## has-a object
		self.name = name
	
## is-a object
class Cat(Animal):

	def __init__(self, name):
		## has-a object
		self.name = name
	
## is-a object
class Person(object):

	def __init__(self, name):
		## has-a object
		
		self.name = name
		## Person has-a pet of some kind
		self.pet = None
		
## is-a object
class Employee(Person):
	
	def __init__(self, name, salary):
		## is-a object
		super(Employee, self).__init__(name)
		## has-a object
		self.salary = salary
		
## is-a object
class Fish(object):
	pass

## is-a object
class Salmon(Fish):
	pass
	
## is-a object
class Halibut(Fish):
	pass
	
## is-a Dog
rover = Dog("Rover")

## is-a Cat
satan = Cat("Satan")

## is-a Person
mary = Person("Mary")

## has-a pet
mary.pet = satan

## is-a Emplyee
frank = Employee("Frank", 120000)

## has-a pet
frank.pet = rover

## is-a fish
flipper = Fish()

## is-a Salmon
crouse = Salmon()

## is-a Halibut
harry = Halibut

print rover.name
print satan.name
print mary.name
print frank.name, " ", frank.salary