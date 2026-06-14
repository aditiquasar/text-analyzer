text = input ("Enter the text: ")


print ("First 5 chars: ", text[:5]) #It takes characters from index 0 up to(but not including)index 5


print("Last 5 chars: ", text[-5:])  #-5 means start from the 5th character from the end.

print ("Reversed: ", text[::-1]) #[::-1] means move through the string backward with a step of -1

print ("Word count: ", len(text.split())) 

print("Charcter count: ", len(text))

if text == text[::-1]:  #Compares the original string with its reversed version, If it is same the text is a palindrome.
    
    print("Palindrome")
    
else:
    print("Not Palindrome")   
