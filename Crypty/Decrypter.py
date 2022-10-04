from cryptography.fernet import Fernet


encrypted_file = 'C:/Users/Austi/OneDrive/Desktop/Stuff/Private_Encrypted.txt'

sensitive = {}

with open(encrypted_file, 'r') as file:
    for line in file.readlines():
        try:
            name, value = line.split(':', 1)
            sensitive[name.strip()] = value.strip()
        except:
            break

for name in sensitive.keys():
    print(name)

encryption_key = input('\nEnter Encryption Key: ')
key = encryption_key.encode()
f = Fernet(key)

sensitive_keys = []

for name in sensitive.keys():
    sensitive_keys.append(str(name).lower())


def ask_input():
        user_input = input('\nWhat data are you looking for: ')
        return user_input
        

def generate_value() -> str:
    user_input = ask_input()
    while user_input.lower() not in sensitive_keys:
        print("\nData doesn't exist, try again: ")
        user_input = ask_input()
    for name in sensitive.keys():
        if user_input.lower() == str(name).lower():
            value = sensitive[name]
            return value


def unencrypt_value(value: str) -> bytes:
    unencrypted_value = f.decrypt(str(value).encode())
    return unencrypted_value


def run_decrypter():
    generated_value = generate_value()
    unencrypted_value = unencrypt_value(generated_value)

    print(f'\nValue: {unencrypted_value.decode()}')

    user_input = ''
    while user_input.lower() not in ('y', 'n'):
        user_input = input('\nWould you like to find another value? Y or N: ')

    if user_input.lower() == 'y':
        run_decrypter()
    else:
        quit()


run_decrypter()


