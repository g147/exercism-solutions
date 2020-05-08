class Luhn:
    num=""
    def __init__(self, card_num):
        self.num=card_num.replace(" ","")

    def valid(self):
        num = self.num[::-1]
        try:
            int(num)
        except:
            return False
        mod = 0
        if(num=='0'):
            return False
        for i in num[1::2]:
            sum=int(i)*2
            if(sum>9):
                sum=sum-9
            mod+=sum
        for i in num[::2]:
            mod+=int(i)
            
        return mod%10==0