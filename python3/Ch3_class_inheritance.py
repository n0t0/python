""" A Garage Full of Glassy Vehicles """

class Vehicle: # Base Vehicle class

    def __init__(self, color, manuf):
        self.color = color
        self.manuf = manuf
        self.gas = 4 # a full tank of gas

    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print('The {} {} goes VROOOM!'.format(self.color, self. manuf))
        else:
            print('The {} {} sputters out of gas.'.format(self.color, self.manuf))

class Car(Vehicle): # Inherits from Vehicle class

    # turn the radio on
    def radio(self):
        print("Rockin' Tunes!")

    # open the window
    def window(self):
        print('Ahhh... freash air!')

class Motorycle(Vehicle): # Inherits from Vehicle class

    # put on motorcycle helmet
    def helmet(self): 
        print('Nice and Safe!')

class ECar(Car)

    def drive(self):
         print('The {} {} goes shhhh!'.format(self.color, self. manuf))
       
     
