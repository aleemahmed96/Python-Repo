class Restaurant():
    """making class restaurant that defines restaurant name and cuisine type
    """
    def __init__(self,name,cuisine):
        """defining built-in method of python  (formerly called 'functions' before classes introduction) 
        
        Arguments:
            name {string} -- name of restaurant
            cuisine {string} -- type of food(cuisine)
        """
        self.restaurant_name = name
        self.cuisine_type = cuisine
    
    def describe_restaurant(self):
        print("This is " + self.restaurant_name.title() + " restaurant.")
        print("This restaurant has " + self.cuisine_type.title() + " cuisine.")
    
    def open_restaurant(self):
        print(self.restaurant_name.title() + " Restaurant is open.")

restaurant_obj = Restaurant('Chinatown','Chinese')
restaurant_obj.describe_restaurant()
restaurant_obj.open_restaurant()

    
