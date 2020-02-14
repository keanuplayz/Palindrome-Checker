# Palindrome-Checker - A project for IT class checks if your input is a palindrome or not.
# Started writing in 2020 by Keanu Timmermans.
# To the extent possible under law, the author(s) have dedicated all copyright and related and neighboring rights to this software to the public domain worldwide. This software is distributed without any warranty.
# You should have received a copy of the Apache License 2.0. If not, see <https://www.apache.org/licenses/LICENSE-2.0>.

def reverse(s):                                                # Functie die het omgekeerde van een string returnt.
    return s[::-1] 
  
def isPalindrome(s):                                           # Functie die checkt of het een Palindroom is.
    # Calling reverse function 
    rev = reverse(s)                                           # Reverse functie wordt hier aangeroepen.

    # Checking if both string are equal or not 
    if (s == rev):                                             # Checkt of alle twee de strings hetzelfde zijn ja of nee.
        return True
    return False
  
  
# Driver code                                                  # Code die uitgevoerd wordt.
s = input("Enter string:")
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No")


                                                               # Translation of comments in order of appearance:

                                                               # Function which returns the reverse of a string. 
                                                               # The reverse function is called here.
                                                               # Checks if both strings are equal or not. 
                                                               # Code that's executed.