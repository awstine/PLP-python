def addSums():
    print(2 + 7)


addSums()


def multiply(a, b):
    return a * b


product = multiply(4, 2)
print("product: ", product)


#argments a * is added before parameter if the parameters are unknown
def subtract(*nums2):
    sub = 0
    for num in nums2:
        sub -= num
        return sub
    print("total: ", subtract(65, 76, 2))


def add_sums(a, b):
    def double_it():
        double = (a + b) * 2
        print(double)

    double_it()
    return a + b


print(add_sums(2, 3))

#Lambdas
snack = lambda: print("maharagwe")
snack()


def num_square(num):
    return num ** 2


#print("square is: ",num_square(2))

num_square1 = lambda num: print(num ** 2)
num_square1(3)

#check a palindrome
isPalindrome = lambda string: "palindrome" if string == string[::-1] else "not palindrome. "
string = input("enter string: ")
print(isPalindrome(string))
