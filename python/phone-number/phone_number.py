import re
class PhoneNumber:
    number =  ""
    area_code =""
    def __init__(self, number):
        number=re.sub('[^0-9]+', '', number)
        if(len(number)<10 or len(number)>11):
            raise ValueError("Invalid")
        elif(len(number)==10):
            if(number[0]=='1'):
                raise ValueError("Invalid")
        else:
            if(number[0]!='1'):
                raise ValueError("Invalid")
            number=number[1:]
        if(number[0]=='0' or number[0]=='1' or number[3]=='0' or number[3]=='1' ):
            raise ValueError("Invalid")
        self.number=number
        self.area_code=number[0:3]

    def pretty(self):
        return "(%s) %s-%s"%(self.number[0:3],self.number[3:6],self.number[6:])