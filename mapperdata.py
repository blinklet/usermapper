#!/usr/bin/env python3
import yaml, secrets, string

def get_user_passwords(pass_value,length=8):
    if pass_value == "random":
        alphabet = string.ascii_letters + string.digits
        passwd = ''.join(secrets.choice(alphabet) for i in range(length))
    else:
        passwd = pass_value
    return passwd


if __name__ == "__main__":

    stream = open('config.yaml', 'r')
    configuration = yaml.safe_load(stream)

    for x in configuration['users']:
        print(x)
        for y in range(configuration['users'][x]["quantity"]):
            z = configuration['users'][x]["password"]
            print(z)
            print(get_user_passwords(z))
            print()
    
    

