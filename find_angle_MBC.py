import math
angle_AB = int(input())
angle_BC = int(input())
ans = f'{round(math.degrees(math.atan(angle_AB/angle_BC)))}{chr(176)}'
print(ans)
