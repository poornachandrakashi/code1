#Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string
string=str(input("Enter the string:"))
n=int(input("ENter an integer number"))
new=[]
def remove(string,n):
    for i in range(0,n):
        new.append(string[-i])
        i=i+1

    return new

print(remove(string,n))
