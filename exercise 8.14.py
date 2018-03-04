def car(manufacturer,model_name,**details):

    '''details will be car year and car kind and car value'''

    car_info = {}
    car_info['Car Name'] = manufacturer
    car_info['Model Name'] = model_name
    for key, value in details.items():
        car_info[key] = value
    return car_info

car_information1 = car("honda","civic",Year=2016,Kind='hybrid',Value=30000000)
print("The car has the following information:")
print(car_information1)