# The Bird class gives two attributes to each bird
# It has  _init_functions that set each birds name, species and age.
# The script runs three times and each time the user is prompted to give the names, species and age of each bird
# The attributes of each bird from the user is displayed

class Bird:

    def __init__(self, name, species, age):
        self.__name = name
        self.__species = species
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_species(self, species):
        self.__species = species

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age


def main():

    birdCount = int(0)

    while birdCount < 3:
        bird_name = input("Please enter a name for your bird:  ")
        bird_species = input("Please enter the species of the bird:  ")
        bird_age = float(input("Please enter the age of this bird:  "))

        bird_stats = Bird(bird_name, bird_species, bird_age)

        print("This Bird's name is: ", bird_stats.get_name())
        print("This bird is a: ", bird_stats.get_species())
        print("The birds age is: ", bird_stats.get_age())
        birdCount += 1

main()
