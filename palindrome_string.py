#check if a string is palindrome
def palstr():
  str=input("Enter String--> ")
  pal=str[::-1]
  if pal==str:
    print(str +"is palindrome")
  else:
    print("False")
palstr()
