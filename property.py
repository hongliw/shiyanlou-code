class Account(object):
    def __init__(self, rate):
        self.__amount = 0
        self.rate = rate

    @property
    def amount(self):
        return self.__amount

    @property
    def cny(self):
        return self.__amount * self.rate
    
    @amount.setter
    def amount(self, value):
        if value < 0:
            print('Sorry, no negative amount in the account.')
            return
        self.__amount = value

if __name__ == '__main__':
    acc = Account(rate=6.6)
    acc.amount = 20
    print('Dollar amount:', acc.amount)
    print('In CNY:', acc.cny)
    acc.amount = -100
    print('Dollar amount:', acc.amount)
