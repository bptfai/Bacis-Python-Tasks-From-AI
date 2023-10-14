# TASK1: Check number if is palindromic or not

# ==============================================================================================

# defining colors
cyan = "\033[36m"
red = "\033[31m"
white = "\033[37m"
green = "\033[32m"

# ==============================================================================================

# error messages
error_message_1 = red + "Please enter a valid number ..."
error_message_2 = red + "Float numbers can not be palindromic ..."

# output messages
output_message_1 = cyan + "Your number is palindromic !"
output_message_2 = cyan + "Your number is not palindromic !"

# system messages
system_message_1 = white + ">>> Please enter a number: "
system_message_2 = white + "Goodbye !"

# ==============================================================================================

running = True
while running:
    number = input('\n' + system_message_1 + green)

    try:
        if number == str(int(float(number))):
            """
            EXPLANATION
            [case1] user input ('1') --> 1.0 --> 1 --> '1' (same with first input) 
            [case2] user input ('1.0') --> 1.0 --> 1 --> '1' (not same with first input)
            [case3] user input ('sometext') --> error_message_1
            """
            
            # reverse the number
            reverse_list = []
            reversed_number = ""

            for figure in number:
                reverse_list.insert(0, figure)
    
            for reversed_figure in reverse_list:
                reversed_number += reversed_figure

            # disable minus sign
            if '-' in number:
                number = number.strip('-')
                reversed_number = reversed_number.strip('-')

            # check if they are same           
            if number == reversed_number:
                print('\n' + output_message_1)
            else:
                print('\n' + output_message_2)

        else:
            print('\n' + error_message_2)
    except:
        # setting up the exit
        if number == 'q' or number == 'Q':
            print('\n' + system_message_2 + '\n')
            running = False
        else:
            print('\n' + error_message_1)
