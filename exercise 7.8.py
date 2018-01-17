sandwich_orders = ['chicken', 'jalepino', 'fajita']
finished_sandwiches = []
prompt = 'what would you like to eat??'
message =input(prompt)
while sandwich_orders:
    if 'fajita' in message:
        index1 = sandwich_orders.index('fajita')
        sandwitch = sandwich_orders.pop(index1)
        finished_sandwiches.append(sandwitch)
        print('making ' ,sandwitch)
        print('sandwiches made: ', finished_sandwiches)
    elif 'jalepino' in message:
        index2 = sandwich_orders.index('jalepino')
        sandwitch = sandwich_orders.pop(index2)
        finished_sandwiches.append(sandwitch)
        print('making ' ,sandwitch)
        print('sandwiches made: ', finished_sandwiches)
    elif 'chicken' in message:
        index3 = sandwich_orders.index('chicken')
        sandwitch = sandwich_orders.pop(index3)
        finished_sandwiches.append(sandwitch)
        print('making ' ,sandwitch)
        print('sandwiches made: ', finished_sandwiches)
    signal = '\n anything else you like in our menu???'
    signal += '\n if yes then request your order'
    message = input(signal)

if message == 'quit':
        comma ='\n Here are all sandwitches that have been made: '
        print(comma, finished_sandwiches)
