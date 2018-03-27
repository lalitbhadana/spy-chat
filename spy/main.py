import sys
#import valiadation
import default
import spy_status
import spy_chat
import spy_friend

print("Welcome to spychat program")
spy={
    'name' : " ",
    'salutation' : " ",
    'age' : 0,
    'rating' : 0.0
}

choice=input("Enter your choice to print default settings (Y or N)")

if(choice.upper() =='Y'):
    print("U have choosen default settings")
    spy['name']=default.spy1['name']
    spy['salutaion']=default.spy1['salutation']
    spy['age']=default.spy1['age']
    spy['rating']=default.spy1['rating']
    print("Hello" + " "+spy['salutaion'] + spy['name'])
    print("Your age is " , spy['age'])
    print("Your rating is " ,spy['rating'])
    if choice.upper()=='Y':
        print(default.spy1['rating_star'])
    #sys.exit(0)

else:
    print("U wnat to take input from the user")
    spy['name']=input("Enter a name")
    if spy['name'].isalpha() == False:
        print("U have given wrong name")
        sys.exit(0)


        #validation For salutation (Mr. or Mrs.)
    spy['salutaion']=input("Enter a salutation(Mr. or Mrs.)")
    if spy['salutaion'] != 'Mr.' and spy['salutaion'] != 'Mrs.':
        print("U have given wrong salutation")
        sys.exit(0)


        #validation for age:
    #if dict1['age'].isdigit() == False:
        #print("U have given wrong input")
        #sys.exit(0)
    spy['age'] = int(input("Enter your age"))
    if spy['age'] < 12 and spy['age'] > 50:
        print("U are not eleigible")
        sys.exit(0)


        # validation for rating:
    spy['rating'] = float(input("Enter your rating( 0 to 5)"))
    print("Hello" +spy['salutaion'] + spy['name'] )
    print("Your age is " , spy['age'])
    print("Your rating is " ,spy['rating'])

    if spy['rating'] > 4 and spy['rating'] < 5:
        print("U are 3 star of spy")
    elif spy['rating']> 3 and spy['rating'] <4:

        print("U are 2 star of spy")

    elif spy['rating'] > 2 and spy['rating'] <3:

        print("U are 1 star of spy")
    else:
        print("U are 0 star spy")
        sys.exit(0)
        # validation for name


#result=valiadation.validate_chat(spy_name,spy_salutaion,spy_age)
spy_chat.start_chat('mikku',25,4.5)

