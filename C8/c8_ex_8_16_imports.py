#8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:


#import c8_ex_8_16_User_Profile_repository

#import module_name - DONE
#import module_name as mn - DONE
#from module_name import function_name - DONE
#from module_name import function_name as fn - DONE
#from module_name import * - DONE

from c8_ex_8_16_User_Profile_repository import *

user_profile = build_profile('gustavo', 'aguilar',
                             location = 'CR',
                             future_location = 'US',
                             field = 'engineering')

print_profile(user_profile)




