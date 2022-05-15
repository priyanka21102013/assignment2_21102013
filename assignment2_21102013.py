# Question1
string = "python is a case sensitive language"
# (a) To find length of string
length = len(string)
print("The length of string is ", length)

# (b) Reverse order of string
reverse = string[::-1]
print("The reverse order of the string in one line code is", reverse)

# (c) Slice function
sliced_string = string[10:26]
print("The new sliced string is", sliced_string)

# (d) Replace Function
replaced_string = string.replace("a case sensitive", "object oriented")
print("The new replaced string is",replaced_string)
# (e) Index of substring
indexed = string.index("a")
print("The index of substring a is", indexed)


# Question2
Name = "Priyanka"
SID = 21102013
Department_Name = "Civil"
CGPA =9.8
Line1 = "Hey, {} Here!".format(Name)
Line2 = "My SID is {}".format(SID)
Line3 = "I am from {} department_Name my CGPA is {}".format(Department_Name,CGPA)

print(Line1)
print(Line2)
print(Line3)

# Question3
a = 56
b = 10
A = a&b
B = a|b
C = a^b
D = a<<2, b<<2
E = a>>2, b>>4
print("output of a&b is", A)
print("output of a|b is ", B)
print("output of a^b is ", C)
print("Left shift both a and b with 2 bits is", D)
print("Right shift a with 2 bits and b with 4 bits is", E)
print("\n")

# Question4
String = input("Enter the string")
if 'name' in String:
        print("Yes")
else:
        print("No")
print("\n")

# Question5
s1 = int(input("Enter the first side of triangle"))
s2 = int(input("Enter the second side of triangle"))
s3 = int(input("Enter the third side of triangle"))
while(s1+s2>s3) and (s1+s3>s2) and (s2+s3>s1):
     print("Triangle is valid")
     break
print("\n")

# Question6
a = int(input("Enter the number"))
b = int(input("Enter the number"))
num = a ^ b
count_flipped_bit = 0
while (num != 0):
    num = num & (num - 1)
count_flipped_bit += 1
print("Number of bits needed to be flipped to convert a to b is", count_flipped_bit)
