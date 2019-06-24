import random
'''
实现52张牌的随机洗牌
'''
class PokerGame():
    # 定义两个类成员 类似java里用static修饰
    color = ['黑桃', '红桃', '梅花', '方块' ]
    poker = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] #牌面
    def __init__(self):
        self.__initPoker = {}  # 存放有序的原始没有洗过的牌
        self.__randomPoker = []  # 存放洗完之后的牌
        pass
    def initPoker(self):
        self.__initPoker = {'黑桃'： PokerGame.poker[:],
                            '红桃':  PokerGame.poker[:],
                            '梅花':  PokerGame.poker[:],
                            '方块':  PokerGame.poker[:]}
        pass
    def randomPoker(self):
        # 当随机出来的牌数少于52张，继续随机
        while len(self.__randomPoker) < 52:
            # 1、随机拍的颜色
            colorIndex = random.randint(0,3)
            colorValue = PokerGame.color[colorIndex]

            pokerColorList = self.__initPoker[colorValue]
            # 2、随机牌面
            if len(pokerColorList) <= 0:
                continue
                pass
            # 否则还有的情况，随即排面的索引
            pokerIndex = random.randint(0, len(pokerColorList)-1)
            # 通过索引得到排面值
            pokerValue = pokerColorList[pokerIndex]
            # 把颜色和排面连接后存入洗牌结束列表
            self.__randomPoker.append(colorValue +":" + pokerValue)
            # 从当前舒适化的牌面劣币哦啊中删除当前的牌面
            pokerColorList.remove(pokerValue)
            pass
        pass
    def getRandomPoker(self):
        return self.__randomPoker
        pass
    pass
if __name__ == "__main__":
    pokerGame = PokerGame()
    pokerGame.initPoker()
    pokerGame.randomPoker()
    print(pokerGame.getRandomPoker())

