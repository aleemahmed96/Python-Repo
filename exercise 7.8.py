sandwich_orders = ['chicken', 'jalepino', 'fajita']
finished_sandwiches = []
prompt = 'what would you like to eat??'
message =input(prompt)
while sandwich_orders:
    if 'fajita' in message:
        index = sandwich_orders.index('fajita')
        sandwitch = sandwich_orders.pop(index)
        finished_sandwiches.append(sandwitch)
        print('making ' + str(sandwitch))
        print('sandwiches made: ', finished_sandwiches)
    elif 'jalepino' in message:
        index = sandwich_orders.index('jalepino')
        sandwitch = sandwich_orders.pop(index)
        finished_sandwiches.append(sandwitch)
        print('making ' + str(sandwitch))
        print('sandwiches made: ', finished_sandwiches)
    elif 'chicken' in message:
        index = sandwich_orders.index('chicken')
        sandwitch = sandwich_orders.pop(index)
        finished_sandwiches.append(sandwitch)
        print('making ' ,sandwitch)
        print('sandwiches made: ', finished_sandwiches)
    signal = '\n anything else you like in our menu???'
    signal += '\n if yes then request your order'
    message = input(signal)

    new_sandwich_orders = sandwich_orders.copy()
    if sandwich_orders == new_sandwich_orders:
        comma ='\n Here are all sandwitches that have been made: '
        print(comma, new_sandwich_orders)
    break
