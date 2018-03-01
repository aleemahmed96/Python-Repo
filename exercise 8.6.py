def city_country(city, country):
    city_country = "\"" + city + ", " + country + "\"" 
    return city_country.title() 

count=0
for count in range(3):

    print("enter your city name")
    city1 = input("City Name: ")
    print("enter your country name")
    country1 = input("Country Name: ")
    boundry = city_country(city1, country1)
    print(boundry)