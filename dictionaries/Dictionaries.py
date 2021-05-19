# Goal: Learn About Dictionaries in Python

myDictionary = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

print(myDictionary)
print()
print('The length of the dictionary is: {0}'.format(len(myDictionary)))

print('The brand of the car saved in the dictionary is: {0}'.format(myDictionary['brand']))

# Data Types in Dictionary
myDict = {
    'brand': 'Nissan',
    'model': 'Skyline',
    'manual': False,
    'year': 1964,
    'colors': ['red', 'black', 'blue']
}

print()
print('There are totally {0} colors available'.format(len(myDict['colors'])))
print('The available colors for {0} {1} are: {2}'.format(myDict['brand'], myDict['model'], myDict['colors']))