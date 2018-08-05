#python program to print the longest word in a string and if there are more than 1 longest word then print the first occurence
def largeword():
  str=input("Enter the string ")
  str2=str.split()
  print(max(str2))
