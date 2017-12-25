def shoppingOffers(price, special, needs):
    """
    :type price: List[int]
    :type special: List[List[int]]
    :type needs: List[int]
    :rtype: int
    """
    max_price = 0
    for i in range(len(price)):
        max_price += price[i] * needs[i]

    print max_price
    selected_offer = []
    for offer in special:
        tmp_price = 0
        flag = 0
        for i in range(len(offer) - 1):
            if offer[i] > needs[i]:
                flag = 1
                break
            else:
                tmp_price += (needs[i] - offer[i]) * price[i]

        if flag == 1:
            break

        tmp_price = tmp_price + offer[-1]
        print tmp_price


        if tmp_price < max_price:
            max_price = tmp_price
            selected_offer = list(offer)

    print max_price
    print selected_offer

    return max_price


price = [9,9]
special = [[1,1,1]]
needs = [2,2]
print shoppingOffers(price, special, needs)