from typing import List
def grayCode(n: int, start: int) -> List[int]:
    res = [0] * (2 ** n)
    res[0] = start
    for i in range(1, 2 ** n):
        res[i] = (res[i - 1] ^ (i))
    return res