# for matrix calculations 

def calc_det2(matrix): 
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
def solve2(A, B):
    n = 2
    det = calc_det2(A)
    det1 = calc_det2([[B[r], A[r][1]] for r in range(n)])
    det2 = calc_det2([[A[r][0], B[r]] for r in range(n)])
    x1 = det1 / det
    x2 = det2 / det
    return x1, x2

def calc_det3(A):
    pos = A[0][0] * A[1][1] * A[2][2] + \
          A[0][1] * A[1][2] * A[2][0] + \
          A[0][2] * A[1][0] * A[2][1]
    neg = A[0][2] * A[1][1] * A[2][0] + \
          A[0][1] * A[1][0] * A[2][2] + \
          A[0][0] * A[1][2] * A[2][1]
    return pos - neg

def calc_det5(A):
    n = 5
    sign = 1
    r = 0  
    res = 0
    for c in range(n):
        A_ = [[A[r_][c_] for c_ in range(n) if c_ != c]
              for r_ in range(n) if r_ != r]
        res += sign * A[r][c] * calc_det4(A_)
        sign *= -1
    return res

def calc_det6(A):
    n = 6
    sign = 1
    r = 0  
    res = 0
    for c in range(n):
        A_ = [[A[r_][c_] for c_ in range(n) if c_ != c]
              for r_ in range(n) if r_ != r]
        res += sign * A[r][c] * calc_det5(A_)
        sign *= -1
    return res

def solve3(A, B):
    n = 3
    det = calc_det3(A)
    det1 = calc_det3([[B[r], A[r][1], A[r][2]] for r in range(n)])
    det2 = calc_det3([[A[r][0], B[r], A[r][2]] for r in range(n)])
    det3 = calc_det3([[A[r][0], A[r][1], B[r]] for r in range(n)])
    x1 = det1 / det
    x2 = det2 / det
    x3 = det3 / det
    return x1, x2, x3


def calc_det4(A):
    n = 4
    sign = 1
    r = 0
    res = 0
    for c in range(n):
        A_ = [[A[r_][c_] for c_ in range(n) if c_ != c]
              for r_ in range(n) if r_ != r]
        res += sign * A[r][c] * calc_det3(A_)
        sign *= -1
    return res

def solve4(A, B):
    n = 4
    det = calc_det4(A)
    det1 = calc_det4([[B[r], A[r][1], A[r][2], A[r][3]] for r in range(n)])
    det2 = calc_det4([[A[r][0], B[r], A[r][2], A[r][3]] for r in range(n)])
    det3 = calc_det4([[A[r][0], A[r][1], B[r], A[r][3]] for r in range(n)])
    det4 = calc_det4([[A[r][0], A[r][1], A[r][2], B[r]] for r in range(n)])
    x1 = det1 / det
    x2 = det2 / det
    x3 = det3 / det
    x4 = det4 / det
    return x1, x2, x3, x4

def solve5(A, B):
    n = 5
    det = calc_det5(A)
    det1 = calc_det5([[B[r], A[r][1], A[r][2], A[r][3], A[r][4]] for r in range(n)])
    det2 = calc_det5([[A[r][0], B[r], A[r][2], A[r][3], A[r][4]] for r in range(n)])
    det3 = calc_det5([[A[r][0], A[r][1], B[r], A[r][3], A[r][4]] for r in range(n)])
    det4 = calc_det5([[A[r][0], A[r][1], A[r][2], B[r], A[r][4]] for r in range(n)])
    det5 = calc_det5([[A[r][0], A[r][1], A[r][2], A[r][3], B[r]] for r in range(n)])
    
    x1 = det1 / det
    x2 = det2 / det
    x3 = det3 / det
    x4 = det4 / det
    x5 = det5 / det
    return x1, x2, x3, x4, x5

def solve6(A, B):
    n = 6
    det = calc_det6(A)    
    det1 = calc_det6([
        [B[r] if c == 0 else A[r][c] for c in range(n)]
        for r in range(n)])
    det2 = calc_det6([
        [B[r] if c == 1 else A[r][c] for c in range(n)]
        for r in range(n)])
    det3 = calc_det6([
        [B[r] if c == 2 else A[r][c] for c in range(n)]
        for r in range(n)])
    det4 = calc_det6([
        [B[r] if c == 3 else A[r][c] for c in range(n)]
        for r in range(n)])
    det5 = calc_det6([
        [B[r] if c == 4 else A[r][c] for c in range(n)]
        for r in range(n)])
    det6 = calc_det6([
        [B[r] if c == 5 else A[r][c] for c in range(n)]
        for r in range(n)])
    
    x1 = det1 / det
    x2 = det2 / det
    x3 = det3 / det
    x4 = det4 / det
    x5 = det5 / det
    x6 = det6 / det
    return x1, x2, x3, x4, x5, x6

def solve_sle(A, B, n):
    if n == 2:
        return solve2(A, B)
    if n == 3:
        return solve3(A, B)
    if n == 4:
        return solve4(A, B)
    if n == 5: 
        return solve5(A, B)
    if n == 6: 
        return solve6(A, B)
    print(f"! n should be 2/3/4/5/6, {n} got")
    return None