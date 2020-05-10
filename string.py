#Accept string from a user and display only those characters which are present at an even index number.
string=str(input("Enter a word:"))
def finding_index(string):
    for i in range(len(string)):
        if i%2==0:
            print(string[i])
        i=i+1

finding_index(string)