import validation
friends = []
new_spy_profile = {
		'new_spy_name' : " ",
		'new_spy_salutation' : " ",
		'new_spy_age' : 0,
		'new_spy_rating' : 0.0,
		'chat' : []
	}

def add_friend():

	
	print(" U want to update new profile")
	new_spy_profile['new_spy_name']=input("Enter a name")
	new_spy_profile['new_spy_salutation']=input("Enter a salutation(Mr. or Mrs.)")
	new_spy_profile['new_spy_age']=int(input("Enter a age"))
	new_spy_profile['new_spy_rating']=float(input("Enter a rating(0 to 5)"))
	
	#validation.check()

	
#print(frien)


	if validation.check(new_spy_profile) == False:
		print("U entered wrong information")

	friends.append(new_spy_profile)

	return new_spy_profile
	
	
	
	

#for i in range(len(friend_name)):
#