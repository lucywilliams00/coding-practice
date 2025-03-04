#this can be written directly into the command line
print('Hello World!') #prints 'Hello World!'

a = 1
b = 2
A = 3 #does not overwrite variable a
if a < b:
    print('a is smaller than b')
elif a == b:
    print('a equals b')
else:
    print('a is bigger than b')

string = 'I am a string.'

numString = str(5) #'5'
numInteger = int(5) #5
numFloat = float(5) #5.0
print(type(numFloat)) #prints 'float'

flavour1, flavour2, flavour3 = 'apple', 'banana', 'strawberry' #three variables with unique values
person1, person2, person3 = 'Mary' #three variables with the same value
print(flavour1, flavour2, flavour3) #prints 'apple banana strawberry'
print(flavour1 + flavour2 + flavour3) #prints 'applebananastrawberry'
print(a + b) #prints 3

shoppingList = ['chicken', 'rice', 'beans']
item1, item2, item3 = shoppingList

def myFunction():
    print('I am number ' + str(a))

myFunction() #calls the function myFunction

stringArray = 'I am an array'
print(stringArray[0]) #prints 'I'
for character in stringArray:
    print(character) #prints each character of stringArray on separate lines
print(len(stringArray)) #prints 13
print('array' in stringArray) #prints true
print('list' not in stringArray) #prints true
print(stringArray[5:13]) #prints 'an array' 
print(stringArray[:4]) #prints 'I am'
print(stringArray[5:]) #prints 'an array'

stringWhitespace = ' whitespace string '
print(stringWhitespace.strip()) #prints 'whitespace string'
print(stringWhitespace.replace('t', 'p')) #prints 'whipespace spring'

stringOne = 'Dog, Cat, Hamster'
stringSplit = stringOne.split(',') #['Dog', 'Cat', 'Hamster']

product = 'EasyStep'
price = 39.99
ad1 = 'Buy the new {} today for just £{}!'
print(ad1.format(product, price)) #prints 'Buy the new EasyStep today for just £39.99!'

product1 = 'ShakerMaker'
product2 = 'SeatTreat'
ad2 = 'On offer today: the {1} and the {0}.'
print(ad2.format(product1, product2)) #prints 'On offer today: the SeatTreat and the ShakerMaker'

stringEscapeQuote = 'I saw the movie \"Oppenheimer\" yesterday'
stringNewLine = 'First line\nSecond line\nThird line'

#other string methods https://www.w3schools.com/python/python_strings_methods.asp

x = 1
y = 2

equationSum = x + y #3
equationSub = y - x #1
equationMul = x * y #2
equationDiv = y / x #2
equationMod = y % x #0

if x < y and x != y:
    print('true')

nameList = ['Lucy', 'James', 'Ted']
nameList.pop() #removes the last item
nameList.insert(2, 'Liv') #insert 'Liv' as the third item in nameList
nameList.append('Liv') #appends 'Liv' to the end of nameList

countries = ['France', 'Brazil', 'New Zealand']
asia = ['Russia', 'China', 'Japan']
countries.extend(asia) #adds the contents of asia to countries
asia.remove('Russia')
del asia[0] #removes the first item
asia.clear() #clears the contents of the list
del asia #deletes the list 

for i in range(5):
    print(i) #prints numbers 1 to 5

counter = 0
while counter < 5:
    print('counter too low')
    counter += 1 

letters = ['f', 'b', 'q', 'e']
letters.sort() #sort ascending
letters.sort(reverse == True) #sort descending
letters.reverse() #reverse the order of the list

#list vs tuple vs set
#list = [item, item]
#changeable
#tuple = (item, item)
#unchangeable
#set = {item, item}
#unordered

#vs dictionary
characterCreation = {
    'name': 'Merueum',
    'species': 'Chimera Ant'
}
print(characterCreation['name']) #prints 'Merueum'

#nested dictionary
hunterxhunter = {
    'Gon': {
        'lastName': 'Freecss',
        'age': 12
    },
    'Killua': {
        'lastName': 'Zoldyck',
        'age': 12
    }
}

#note: self can be renamed to anything
#the first parameter always refers to the current instance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, age: {self.age}'

    def greeting(self):
        print('Hello. My name is ' + self.name + '.')

newPerson = Person('Aaron Johnson', 33)
print(newPerson) #prints 'Name: Aaron Johnson, age: 33'
print(newPerson.greeting) #prints 'Hello. My name is Aaron Johnson.'

#parent class Person, child class Student
class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age) #inherit initialisation from parent
        self.year = year