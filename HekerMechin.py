import random
def Rand():
    lin=209487370
    tal=316261353
    yuval=207059544
    ids=[tal,lin,yuval]
    a=4
    return int((random.choice(ids))%a)+1
print(Rand())