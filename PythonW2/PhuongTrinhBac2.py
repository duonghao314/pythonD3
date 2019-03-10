import math


def giai_pt_bac_2(a, b, c):
    """
    giải phương trình bậc 2: ax^2 + bx + c = 0
    """

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        x1 = None
        x2 = None
    elif delta == 0:
        x1 = -b / (2 * a)
        x2 = x1
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2


r1, r2 = giai_pt_bac_2(1, 2, 1)
print(str(r1) + " " + str(r2))
