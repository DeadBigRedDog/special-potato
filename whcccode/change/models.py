from django.db import models
import math

# Create your models here.
class Coin(models.Model):
    COIN_VALUES = (
        (1, .01),
        (2, .05),
        (3, .1),
        (4,.25),
        (5,1)
    )
    change = models.ForeignKey('Change',on_delete=models.CASCADE)
    coin_type = models.SmallIntegerField(choices=COIN_VALUES)

    def get_coin_value_list(self):
        return list(dict(self.COIN_VALUES).values())

    def get_coin_type_value(self):
        return self.COIN_VALUES[self.coin_type-1][1]

class Change(models.Model):
    initial_value = models.FloatField()
    total_count = models.IntegerField(null=True)

    def __get_coin_type_id(self,coin_value):
        coin = Coin()
        for c in dict(coin.COIN_VALUES).items():
            if c[1] == coin_value:
                return c[0]

    def save_coins(self,coin_list):
        for c in coin_list:
            coin_type_id = self.__get_coin_type_id(c)
            coin = Coin()
            coin.change = self
            coin.coin_type = coin_type_id
            coin.save()

    def make_change_1(self):
        coin = Coin()
        coin_values = coin.get_coin_value_list()
        coinValueList = [int(i * 100) for i in coin_values]
        converted_initial_value = int(self.initial_value * 100)
        coinsUsed = [0]*(converted_initial_value+1)
        minCoins = [0]*(converted_initial_value+1)
        for cents in range(converted_initial_value+1):
            coinCount = cents
            newCoin = 1
            for j in [c for c in coinValueList if c <= cents]:
                    if minCoins[cents-j] + 1 < coinCount:
                        coinCount = minCoins[cents-j]+1
                        newCoin = j
            minCoins[cents] = coinCount
            coinsUsed[cents] = newCoin
        
        min_coins_used = minCoins[converted_initial_value]
        list_of_coins = self.__getCoins(coinsUsed,converted_initial_value)
        return min_coins_used,list_of_coins

    def __getCoins(self,coinsUsed,change):
        r_coins_used = list()
        coin = change
        while coin > 0:
            thisCoin = coinsUsed[coin]
            r_coins_used.append(thisCoin/100)
            coin = coin - thisCoin
        return r_coins_used




