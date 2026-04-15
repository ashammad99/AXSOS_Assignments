import sys
print("------------------------Q1-----------------")
x = [ [5,2,3], [10,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)
students[0]['last_name'] = 'Bryant'
print(students)
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
print("------------------------Q2-----------------")
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(dictionary):
    for i in range(len(dictionary)):
        for key,value in dictionary[i].items():
            sys.stdout.write(key + " - " + value + ",")
        print("")

iterateDictionary(students)
print("------------------------Q3-----------------")
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        for key,value in some_list[i].items():
            if key == key_name:
                print(some_list[i][key_name])

iterateDictionary2('first_name', students)
print("------------------------Q3-----------------")
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for key,value in some_dict.items():
        print(str(len(value)) + " " + key.upper())
        for i in range(len(value)):
            print(value[i])
        print("\n")
printInfo(dojo)