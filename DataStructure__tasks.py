#TASKS
#question1
num1 = input("enter number1: ")
num2 = input("enter number2: ")
num3 = input("enter number3: ")
num4 = input("enter number4: ")
num5 = input("enter number5: ")
total = [int(num1)+int(num2)+int(num3)+int(num4)+int(num4)]
print(total)

#question2
my_books = ("Straight shooter","Lies that bind","Unforgiven","Healer","Power of faith")
for book in my_books:
    print(book)

#question3
name = input("enter name: ")
age = input("enter age: ")
fav_color = input("enter favourite color: ")

person = {
    "name": name,
    "age": age,
    "favourite color": fav_color
}

print(person)

#question4
n1 = input("enter number 1: ")
n2 = input("enter number2: ")

set1 = {n1,n2}
print(set1)

n3 = input("enter number 3: ")
n4 = input("enter number4: ")
set2 = {n3,n4}
print(set2)

common_elements = set1.intersection(set2)
if common_elements:
    print(f"common elements: {common_elements}")
else:
    print("No common elements")


#question5
words = input("Enter words: ").split()
odd_length_words = [word for word in words if len(word) % 2 != 0]

print(f"Original list of words: {words}")
print(f"Words with an odd number of characters: {odd_length_words}")














#list
#numbers = [1,2,3]
#mix = [1,"red",4.5]
#add
#mix.append(2)
#print(mix)
#print(numbers)

#players = ["ronaldo","messi","salah"]
#for player in players:
#    print(player)

#var1= "hello",
#print(type(var1))

#dictionary
#capital_city = {"Kenya":"Nairobi", "Tanzania":"dar", "Italy":"Rome"}
#print(capital_city)

#Sets
#student_ID = {23,63,25,84,23}
#student_name = {"dan","mark"}
#print(student_ID|student_name)