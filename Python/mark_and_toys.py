# ***WARNING*** this did not pass all of its tests

# prices is an array of integers, k is an integer
def maximum_toys(prices, k):
    # remove the prices larger than the budget k
    for price in prices:
        if price > k:
            prices.remove(price)
    # sort the prices in ascending order
    prices.sort()
    final = 0
    # iterate through the prices except the last one
    for x in range(len(prices) - 2):
        # set total as the smallest price
        total = prices[x]
        count = 1
        y = x + 1
        # iterate through the prices + 1
        while y < len(prices) - 1:
            # add the next price to the total and check if it is less than the budget k
            if total + prices[y] < k:
                total += prices[y]
                count += 1
            y += 1
        if count > final:
            final = count
    return final
