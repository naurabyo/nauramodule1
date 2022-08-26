list_contact = {'atul dian' : '081234567891', 'budi septy' : '08678650984031', 'catha lina' : '087374368746736' }
def back():
    home = input('Enter to back home')

def add():
    add_name = input ('Insert name: ').lower()
    if add_name.lower() in list_contact.keys(): 
        print('Name already exist')
        back()
        start()
    else:
        add_number = int (input('Add number: '))
        list_contact[add_name] = str(add_number)
        print ('Saved successfuly')
        back()
        start()

def search():
    search_contact = input ('Insert name: ').lower()
    if search_contact in list_contact.keys():
        print('{} \n {}'.format(search_contact, list_contact[search_contact]))
        back()
        start()
    else:
        print ('Contact not found')
        back()
        start()

def edit():
    edit_contact = input ('Insert name: ').lower()
    if edit_contact in list_contact.keys():
        change_name = input('Change name?')
        if change_name == 'yes' or change_name == 'y':
            new_name = input ('Insert new name: ').lower()
            list_contact[new_name] = list_contact [edit_contact]
            del list_contact[edit_contact]
            print ('Name updated')
            change = input('change number?')
            if change == 'yes' or change == 'y':
                new_number = int(input('Insert new number: '))
                list_contact[new_name]= str(new_number)
                print('Contact updated')
                back()
                start()
            else:
                print ('There is no changes')
                back()
                start()
        elif change_name == 'no' or change_name == 'n':
            change = input('change number?')
            if change == 'yes' or change == 'y':
                new_number = int(input('Insert new number: '))
            else:
                print ('There is no changes')
            list_contact[edit_contact] = str(new_number)
            back()
            start()
        else:
            print ('Please answer correctly')
            back()
            start()
    else:
        print ('Contact not found')
        back()
        start()

def delete():
    delete = input ('Insert name: ').lower()
    if delete in list_contact.keys():
        sure = input ('Are you sure?')
        if sure == 'yes' or sure == 'y':
            del list_contact[delete]
            print('Contact has been deleted')
            back()
            start()
        elif sure == 'no' or sure == 'n':
            print ('No contact deleted')
            back()
            start()
        else:
            print ('Please answer correctly')
            back()
            start()
    else:
        print ("Contact not found")
        back()
        start()

def start() :
    welcome = int(input ("Welcome to Yellow Pages \n 1. Add contact \n 2. Search contact \n 3. Edit contact \n 4. Delete contact \n 5. View Contact \n 6. Exit \n Choose your action: "))
    if welcome == 1:
        add()        
    elif welcome == 2:
        search()
    elif welcome == 3:
        edit()
    elif welcome == 4:
        delete()
    elif welcome == 5:
        print(list_contact)
        back()
        start()
    elif welcome == 6:
        print('See you')
    else:
        print('Please Answer correctly')

start()
