# use cookie clicking file to test run the code
# cookie clicker simulation
class cookieClicker:

    # value and amount are set
    def __init__(self):
        self._value = 0
        self._amount = 1

    # add to the value using self._amount
    def click(self):
        self._value += self._amount
    # return total value
    def total(self):
        return ("you have: $" + str(self._value))
    # increase amount if there is enough value, so more value can be gained in fewer clicks
    def increase(self):
        if self._value >= 5:
            self._value -= 5
            self._amount+= 1
        else:
            return ("Sorry you need at least 5 dollars to upgrade")
    # return how much you currently get per click
    def amount(self):
        return ("this is how much you currently get per click: $" + str(self._amount))

    
    

    
