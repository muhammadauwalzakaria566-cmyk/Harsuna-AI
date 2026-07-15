temp = float(input(f'enter the temprature: '))
is_raining = False
if temp > 35.0 or temp < 0.0 or is_raining:
    print('the outdoor is event is cancelled')
else:
    print('the outdoor is event is still schedule')