import sys
def check():
	new_spy_name=input("Enter a name")
	if new_spy_name.isalpha() == False:
		print("U have given wrong name")
		sys.exit(0)
	return new_spy_name

	new_spy_salutation=input("Enter a salutation(Mr. or Mrs.)")
	if new_spy_salutation !='Mr.' and new_spy_salutation!='Mrs.' :

		print("U have given wrong salutation")
		sys.exit(0)
	return new_spy_salutation

	new_spy_age=int(input("Enter a age"))
	if new_spy_age < 12 and new_spy_age > 50:
	    print("U are not eleigible")
	    sys.exit(0)
	return new_spy_age

	
	new_spy_rating=float(input("Enter a rating(0 to 5)"))
	print("Hello" +new_spy_salutation + new_spy_name )
	print("Your age is " , new_spy_age)
	print("Your rating is " ,new_spy_rating)
	if new_spy_rating > 4 and new_spy_rating < 5:
	    print("U are 3 star of spy")
	elif new_spy_rating > 3 and new_spy_rating <4:

	    print("U are 2 star of spy")

	elif new_spy_rating > 2 and new_spy_rating <3:

	    print("U are 1 star of spy")
	else:
	    print("U are 0 star spy")
	    sys.exit(0)
	return new_spy_rating
