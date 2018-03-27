import spy_status
import spy_friend
import spy_message
def start_chat(spy_name,spy_age,spy_rating):
    current_status_message = None
    show_menu = True


    while show_menu:

        menu_choice = int(input("1. Add a status \n 2. Add a Friend \n 3. Send a message \n 4. close application"))

        if menu_choice ==1:
            print("U have chosen to add a status")
            current_status_message=spy_status.add_status(current_status_message)
            #print("your current message is",current_status_message)
        elif menu_choice ==2:
            print("U have chosen add a Friend")
            current_new_user=spy_friend.add_friend()
            print(current_new_user)
        elif menu_choice ==3:
            print("U have chosen to send a message")
            
            msg=spy_message.chat1(spy_friend.friends,spy_friend.new_spy_profile)
            print(msg)

        elif menu_choice ==4:
            show_menu = False