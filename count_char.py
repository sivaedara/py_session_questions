#Write a Python program to count the number of characters in a string. Sample String : 'google.com'

import re

def take_input():
    input_string = str(input("Enter new string to update : ") or "qwertyqw-!@qwe")
    do_magic(input_string)
    
def do_magic(input_string):
    str_length = len(re.findall(r"\w", input_string))
    special_chars=len(input_string) - int(str_length)
    
    print(str_length)
    print(special_chars)


  
if __name__ == "__main__":
    take_input()