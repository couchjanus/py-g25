from datetime import datetime, date, time

choices = ('', 'All contacts', 'New contact', 'Show contact', 'Edit contact', 'Delete contact', 'Exit')

# Dick of contacts 
# contacts = {}

fields = ("name", "phone", "address", "note")

# dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).

# Initialize dictionary with None values
res = dict.fromkeys(range(10))

print("The dictionary with None values : " + str(res))

contacts = dict.fromkeys(fields)
print("The dictionary with None values : " + str(contacts))

# перебор словаря с использованием метода items(), который возвращает новый вид элементов словаря:
print(contacts)

d_items = contacts.items()
print(d_items) # Here d_items is a view of items

# Define a welcome function

def welcome():
    prompt = """
    Welcome to PhoneBook.
        At hand:\n"""
    tip = "Your choice("

    for (index, item) in enumerate(choices):
        if index == 0: continue 
        tip += f"{index},"
        prompt += f'{" "*8} {index}. {item}\n'
    return input(prompt + f"{' '*8} {tip[:-1]} 0r q): ")



def addContact():
    contact = []
    for item in fields:
        field = input(f'Enter {item}: ')
        contact.append(field)
        
    contact.append(datetime.today().strftime("%Y-%m-%d"))
    return contact

def findContact():
    name = input(f'Enter {fields[0]} for serach: ')
    for item in contacts:
        if name in item:
            return item
        else: return None

def editContact(i):
    contact = []
    for item in fields:
        field = input(f'Enter {item}: ')
        contact.append(field)
    contact.append(datetime.today().strftime("%Y-%m-%d"))
    contacts[i] = contact

# Define a main function
def main():
    
    while True:
        choice = welcome()
        if choice == 'q': break
        choice = int(choice if choice.isdigit() else 0)

        if choice == 0:
            continue
        elif choice == 1:
            print(contacts)
        elif choice == 2:
            contacts.append(addContact())
            print(contacts)
        elif choice == 3:
            res = findContact()
            contact = res if res else 'Nothing found'
            print(contact)
        elif choice == 4:
            res = findContact()
            index = contacts.index(res)
            editContact(index)
            print(contacts)            
        elif choice == 5:
            res = findContact()
            index = contacts.index(res)
            print(index)
            print(contacts[index]) 
            del contacts[index]
            print(contacts)
        elif choice == 6:
            print('Thanks for using FoneBook')
            break
        else:
            print('Incorrect Chice!')

main()
