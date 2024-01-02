#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'wbw', '0110']


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
    
    result_list = []
    for item in input_list:
        result_list.append(verify_list(item))

    print ("input list is : " + str(input_list))
    print ("first and last chart same matched ones are : " + str(result_list))
    
def verify_list(input_str):
    
    input_str = list(input_str)
    
    if (input_str[0]) == (input_str[-1]):
        return ("same")
    else:
        return ("not same")
        
if __name__ == "__main__":
    take_input()