#Accept string from a user and display only those characters which are present at an even index number.
string=str(input("Enter a word:"))
def finding_index(string):
    for i in range(len(string)):
        if i%2==0:
            return string[i]
        i=i+1

print(finding_index(string))


