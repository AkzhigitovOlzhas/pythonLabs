class Clothes:
    def __init__(self, name, quantity=0, number_of_pairs=0):
        self.__name = name
        self.__quantity = int(quantity)
        self.__number_of_pairs = int(number_of_pairs)

    def is_couple(self):
        if self.__quantity == 0 and self.__number_of_pairs > 0:
            return True
        else:
            return False

    def show(self):
        print('='*20)
        print(self.__name,end=' ')
        print(str(self.__number_of_pairs)+ " пар" if self.is_couple() else str(self.__quantity)+" шт.")
        print('='*20)

