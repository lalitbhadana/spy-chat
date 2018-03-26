import sys
#import valiadation
import default
import spy_status
import spy_chat
import spy_friend

print("Welcome to spychat program")

choice=input("Enter your choice to print default settings (Y or N)")

if(choice.upper() =='Y'):
    print("U have choosen default settings")
    spy_name=default.spy_name
    spy_salutaion=default.spy_salutation
    spy_age=default.spy_age
    spy_rating=default.spy_rating
    print("Hello" + " "+spy_salutaion + spy_name )
    print("Your age is " , spy_age)
    print("Your rating is " ,spy_rating)
    if choice.upper()=='Y':
        print(default.spy_rating1)
    #sys.exit(0)

else:
    print("U wnat to take input from the user")
    spy_name=input("Enter a name")
    if spy_name.isalpha() == False:
        print("U have given wrong name")
        sys.exit(0)


        #validation For salutation (Mr. or Mrs.)
    spy_salutaion=input("Enter a salutation(Mr. or Mrs.)")
    if spy_salutaion != 'Mr.' and spy_salutaion != 'Mrs.':
        print("U have given wrong salutation")
        sys.exit(0)


        #validation for age:
    #if dict1['age'].isdigit() == False:
        #print("U have given wrong input")
        #sys.exit(0)
    spy_age = int(input("Enter your age"))
    if spy_age < 12 and spy_age > 50:
        print("U are not eleigible")
        sys.exit(0)


        # validation for rating:
    spy_rating = float(input("Enter your rating( 0 to 5)"))
    print("Hello" +spy_salutaion + spy_name )
    print("Your age is " , spy_age)
    print("Your rating is " ,spy_rating)

    if spy_rating > 4 and spy_rating < 5:
        print("U are 3 star of spy")
    elif spy_rating > 3 and spy_rating <4:

        print("U are 2 star of spy")

    elif spy_rating > 2 and spy_rating <3:

        print("U are 1 star of spy")
    else:
        print("U are 0 star spy")
        sys.exit(0)
        # validation for name


#result=valiadation.validate_chat(spy_name,spy_salutaion,spy_age)
spy_chat.start_chat('mikku',25,4.5)

