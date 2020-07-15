def calc_dollars(**coins):
    dollarAmount = 0
    for key, value in coins.items():
        if(key == 'pennies'):
          dollarAmount += value * .01
        elif(key == 'nickels'):
          dollarAmount += value * .05
        elif(key == 'dimes'):
          dollarAmount += value * .10
        elif(key == 'quarters'):
          dollarAmount += value * .25
    print(dollarAmount)
          


# Not a good way to do it. Will come back with error if all four params are not there.
# def calc_dollars(**coins):
#     quarters = coins["quarters"] if coins["quarters"] else 0
#     dimes = coins["dimes"] if coins["dimes"] else 0
#     nickels = coins["nickels"] if coins["nickels"] else 0
#     pennies = coins["pennies"] if coins["pennies"] else 0
#     dollars = ((quarters * 25) / 100) + ((dimes * 10) / 100) + ((nickels * 5) / 100) + (pennies / 100)
#     print(dollars)


calc_dollars(pennies=342, nickels=9, dimes=32, quarters=4)