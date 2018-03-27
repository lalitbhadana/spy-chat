status_list=[]
def add_status(current_status_message):
    print("Display current message")
    if current_status_message == None:
        print("U don't have any current status message yet")
        print("U have to insert a new status")
        new_status_message=input("Enter a new status ")
        if len(new_status_message) > 0:
            updated_status=new_status_message
        status_list.append(updated_status)
        return updated_status
            
            #sprint(status_list)
    else:
        print("Your current message is :" , current_status_message)
        update_choice=input("If u want to select older status then prnt 'y' or add a status then print 'n' :")
        
        if update_choice.upper()=='Y':
            for i in range(len(status_list)):
                print(str(i+1)+ " " + status_list[i])
            message_selection = int(input("Enter a number which u want to select"))
            updated_status=status_list[message_selection-1]
            return updated_status

        elif update_choice.upper() == 'N':
            print("U want to add a status")
            new_status_message=input("Enter a status")
            if len(new_status_message) > 0:
                updated_status=new_status_message
            status_list.append(updated_status)
            return updated_status
