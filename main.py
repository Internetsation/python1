# Project 5!
# This program asks for the user's name and greets them.
# If the user is "Obiwan", they are asked to fight the empire!
# Otherwise they are asked to deliver the droid to Obiwan.


# Get user name
name = input("Tell me your name:")


def my_function():
    # Print user greeting
    while name == "Obiwan":
        break
    else:
        print(f'Hello {name}')


def jedi_request(name):
    if name == "Obiwan":
        # If user is Obiwan help is requested
        print(f' {name}-Kenobi \n Do not forget to tell Luke that Leia is his sister \n and Vader is his '
              f'father!')
    else:
        # If user is not Obiwan help is requested
        print(f'{name} \n This is not the droid you are looking for! \n please return this droid to Obiwan-Kenobi!  ')


if __name__ == '__main__':
    # Run file
    my_function()
    jedi_request(name)
