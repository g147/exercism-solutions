def is_armstrong_number(number):
    sum=0
    for i in str(number):
        sum+=pow(int(i),len(str(number)))
    return sum==number