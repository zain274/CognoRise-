import random
import string 

print("Welcome to our Random Password Generate ")
def main():
    length=int(input("Enter the Length of password you want:"))
    # print(length)
    lowerD=string.ascii_lowercase
    UpperD=string.ascii_uppercase
    digitalD=string.digits
    symbolD=string.punctuation
    combine=lowerD+UpperD+digitalD+symbolD
    x=random.sample(combine,length)
    password="".join(x)
    print(password)
    main()
main()