import itertools


prices = []
print('Enter "x" to stop.')
while True:
    num = input("Please enter the next price: ")
    if str(num) == 'x'.lower():
        break
    else:
        num = float(num)
        prices.append(num)
        print(f"${num:,.2f}")
        run_tot = list(itertools.accumulate(prices))[-1]
        print(f"\tTotal: ${run_tot:,.2f}")
        c = len(prices)

print(f"\nThe Grand Total of {c} items is: ${sum(prices):,.2f}")
