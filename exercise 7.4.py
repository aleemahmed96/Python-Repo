prompt = 'add pizza toppings'
pizza_topping = []
active = True
while active:
    message = input(prompt)
    pizza_topping.append(message)
    if message == 'quit':
        active = False
        pizza_topping.remove('quit')
        print(pizza_topping)
    else:
        print(message)