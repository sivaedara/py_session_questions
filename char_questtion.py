# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '@', except the first char itself. 
# Sample String : 'restart', output : 'resta@t'


def take_input():
    input_string = str(input("Enter new string to update : ") or "qwertyqw")
    validate_input(input_string)
    do_magic(input_string)
    

def validate_input(input_string):
    
    if len(input_string) <=2:
        print ("Entered input is Not valid, please try again ")
        new_choise = str(input("Do you want to try again ? (yes/no) : "))
        
        if new_choise.upper() == "YES":
            take_input()
        else:
            exit(0)

def do_magic(input_string):
    """ Twhere all occurrences of its first char have been changed to '@'"""
    input_string = list(result for result in input_string)
    first_char = input_string[0]
    for j in range(1,len(input_string)):
        if input_string[j] == first_char:
            input_string[j]="@"
            
    input_string = str("".join(input_string))
    print (input_string)    

def do_magic1(input_string):
    """ This will chnage all 2nd occurances of any char"""
    input_string = list(result for result in input_string)
    print(input_string)
    for i in range(0,len(input_string)):
        for j in range(i+1,len(input_string)):
            if input_string[i] == input_string[j]:
                input_string[j]="@"
            
    input_string = str("".join(input_string))
    print (input_string)
          


if __name__ == "__main__":
    take_input()