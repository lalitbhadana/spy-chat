import spy_friend
def chat1(friends,new_spy_profile):
	for i in range(len(friends)):
		print(str(i+1), " ", friends[i])
	msg_selection=int(input("Enter your choice which friend do u want to select"))
	print(friends[msg_selection-1])
	chat_msg=input("Enter a msg")
	spy_friend.new_spy_profile['chat'].append(chat_msg)
	return new_spy_profile['chat']
