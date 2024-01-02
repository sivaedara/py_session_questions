# Write a Python function that takes a list of words and returns the length of the longest one.


def take_input():
    my_list = "aba xyz aabb"
    input_string = input('Enter elements of a list separated by space \n') or my_list
    user_list = input_string.split()
    print('string list: ', user_list)
    validate_input(user_list)

def validate_input(input_list):
    
    for item in input_list:
        if len(item) <=2:
            print ("Entered input is Not valid, please try again ")
            new_choise = str(input("Do you want to try again ? (yes/no) : "))
        
            if new_choise.upper() == "YES":
                take_input()
            else:
                exit(0)
    
    max_len_item (input_list)

def max_len_item(input_list):
    print (max(input_list, key=len))
    
    
if __name__ == "__main__":
    take_input()