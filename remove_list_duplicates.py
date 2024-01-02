#Write a Python program to remove duplicates from a list.

def take_input():
    my_list = "aba xyz aabb xyz aba"
    input_string = input('Enter elements of a list separated by space \n') or my_list
    user_list = input_string.split()
    print('string list: ', user_list)
    remove_duplicats(user_list)

def remove_duplicats(input_list):
    input_list = set(input_list)
    input_list = list(input_list)
    
    print (f"output result with no duplicats is {input_list}")
    
if __name__ == "__main__":
    take_input()