import math

'''
16인 레이드 추가될 시 주석 해제
'''
def auctioncalc(price: int):
    fair = []
    fair4 = math.floor(price * 0.95 * 3/4)
    fair8 = math.floor(price * 0.95 * 7/8)
    # fair16 = math.floor(price * 0.95 * 3/4)
    fairfield = math.floor(price * 0.95 * 10/11)

    fair.append(fair4)
    fair.append(fair8)
    fair.append(fairfield)
    # fair.append(fair16)
    
    return fair