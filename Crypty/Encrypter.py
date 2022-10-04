from cryptography.fernet import Fernet
import getpass

username = getpass.getuser()

encrypted_file = f'C:/Users/{username}/OneDrive/Desktop/Private_Encrypted.txt'

def ask_input():
    user_input = input('Do you want to Encrypt a new File or add a new Element, F or E: ')
    return user_input

user_input = ''
while user_input.lower() not in ('f', 'e'):
    user_input = ask_input()


def populate_dict(a_file: str) -> dict:
    sensitive = {}

    with open(a_file, 'r') as file:
        for line in file.readlines():
            try:
                name, value = line.split(':', 1)
                sensitive[name.strip()] = value.strip()
            except:
                break
        
    
    return sensitive


def generate_fernet_object() -> Fernet:
    encryption_key = input("Enter path to store your Encryption Key, file must be empty: ")
    with open(encryption_key, 'r+') as file:
        if file.readline() == '':
            key = Fernet.generate_key()
            file.write(key.decode())
        else:
            print('File needs to be empty')

    f = Fernet(key)
    return f


def create_new_element():
    encryption_key = input('Enter your Encryption key: ')
    encryption_key = encryption_key.encode()
    f = Fernet(encryption_key)

    name = input('Enter name of value: ')
    value = input('Enter value to encrypt: ')

    token = f.encrypt(value.encode())

    sensitive = populate_dict(encrypted_file)

    with open (encrypted_file, 'w+') as file:
        sensitive.update({name:token.decode()})
        for name, value in sensitive.items():
            file.write(f'{name} : {value}\n')


def create_new_file():
    raw_file = input('Enter path to Raw File: ')

    sensitive = populate_dict(raw_file)

    f = generate_fernet_object()

    for name in sensitive.keys():
        token = f.encrypt(bytes(sensitive[name], encoding='utf8'))
        sensitive[name] = token.decode()

    with open(encrypted_file, 'w+') as file:
        for name, value in sensitive.items():
            file.write(f'{name} : {value}\n')


if user_input == 'f':
    create_new_file()
else:
    create_new_element()
