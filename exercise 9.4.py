class Restaurant():
    """making class restaurant that defines restaurant name and cuisine type
    """
    def __init__(self,name,cuisine):
        """ making method for exercise 9.4 """
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0
    
    def set_number_served(self, set1):
        """ changing value of customers served by using method """
        self.number_served = set1
        print("Number of customers served: " + str(self.number_served))
    
    def increment_number_served(self, inc):
        self.number_served += inc
        print("The maximum number of customers served are: " + str(self.number_served))

restaurant = Restaurant("xyz","abc")
restaurant.number_served = 23
print(restaurant.number_served)

restaurant.set_number_served(25)
restaurant.increment_number_served(28)


