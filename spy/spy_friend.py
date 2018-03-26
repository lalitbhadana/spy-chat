import validation
friend_name=[]
friend_salutation=[]
friend_age=[]
friend_rating=[]
def add_friend():

	print(" U want to update new profile")
	
	validation.check()

	friend_name.append(validation.new_spy_name)
	friend_salutation.append(validation.new_spy_salutation)
	friend_age.append(validation.new_spy_age)
	friend_rating.append(validation.new_spy_rating)
#print(frien)
