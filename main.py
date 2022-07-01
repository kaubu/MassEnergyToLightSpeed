import decimal
import math

# test1 = "2.7x10^24"
# test2 = "3.404788e-001" # Scientific notation

# dec = decimal.Decimal(test2) # Works with test2, but not test1
# print(dec)
# #dec = float(test1)
# dec = float(2.7e+24)
# print(dec)
# print("{:.3f}".format(dec))

print("Mass and Energy to Percentage of Light Speed converter")

DEBUG = False
SPEED_OF_LIGHT = 299792458

print("If your tons of TNT is in the format 2.7x10^24, convert it to 2.7e+24")
tons_of_tnt = input("Tons of TNT: ")
# tons_of_tnt = "7e+14" # TEMP
tons_of_tnt = decimal.Decimal(tons_of_tnt)

mass = int(input("Mass (in kg): "))
# mass = 72 # TEMP

if DEBUG: print("[DEBUG] Tons of TNT: {:.0f}".format(tons_of_tnt))

joules = tons_of_tnt * decimal.Decimal(4.184)
megajoules = tons_of_tnt * 4184

if DEBUG: print("[DEBUG] Joules: {:.0f}".format(joules))
if DEBUG: print("[DEBUG] Megajoules: {:.0f}".format(megajoules))

# >>> import numpy as np
# >>> import sympy
# >>> m, j = sympy.symbols('m j')
# >>> v = sympy.symbols('v')
# >>> ke = sympy.symbols('ke')
# >>> keexpr = 0.5 * m * v^2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for ^: 'Mul' and 'int'
# >>> keexpr = 0.5 * m * v**2 
# >>> keeq = sympy.Eq(ke, keexpr)
# >>> sympy.pprint(keeq)
#             2
# ke = 0.5⋅m⋅v
# >>> vexpr = sympy.solve(keeq, v)
# >>> vexpr
# [-1.4142135623731*sqrt(ke/m), 1.4142135623731*sqrt(ke/m)]

# Anything less than 3,000,000 m/s
# KE = 0.5 * m * v²
# V = 1.4142135623731*sqrt(KE/m)
# THIS WORKS
def get_speed(mass, joules):
    # velocity_squared = decimal.Decimal(0.5) * mass / joules
    # return math.sqrt(velocity_squared)
    return 1.4142135623731 * math.sqrt(joules / mass)

# KE = m₀c² * [√(1 - v²/c²) -1]
# or
# KE = m * c**2 * (math.sqrt(1 - v ** 2 / c ** 2) - 1)
# Symbols ke, m, c, v | c = 299792458 so Symbols ke, m, v
# m₀ is mass at rest
# c is the Speed of Light constant, 299,792,458 m/s

# >>> import math, sympy
# >>> import numpy as np
# >>> ke, m, v = sympy.symbols("ke m v")
# >>> ke_expr = m * 299792458 ** 2 * (sympy.sqrt(1 - v ** 2 / 299792458 ** 2) - 1) 
# >>> ke_eq = sympy.Eq(ke, ke_expr)
# >>> sympy.pprint(ke_eq)
#                          ⎛     _______________________    ⎞
#                          ⎜    ╱              2            ⎟
#                          ⎜   ╱              v             ⎟
# ke = 89875517873681764⋅m⋅⎜  ╱   1 - ─────────────────  - 1⎟
#                          ⎝╲╱        89875517873681764     ⎠
# >>> v_expr = sympy.solve(ke_eq, v)
# >>> v_expr
# [sqrt(ke*(-ke - 179751035747363528*m)/m**2)/299792458, -sqrt(-ke*(ke + 179751035747363528*m)/m**2)/299792458]
# >>>

# sqrt(ke*(-ke - 179751035747363528*m)/m**2)/29979245

def get_relativistic_speed(mass, megajoules):
    # if DEBUG: print("To sqrt: {}".format(megajoules * (-megajoules - 179751035747363528 * mass) / mass**2))
    # if DEBUG: print("To divide by C: {}".format(math.sqrt(megajoules * (-megajoules - 179751035747363528 * mass) / mass**2)))
    # print(megajoules * (-megajoules - 179751035747363528 * mass))
    # return -math.sqrt(-megajoules * (megajoules - 179751035747363528 * mass) / (mass**2)) / 299792458
    # print("mass: {}, megajoules: {}".format(mass, megajoules))
    # print(-megajoules*(megajoules + 179751035747363528*mass)/mass**2)
    should_be_answer = math.sqrt(abs(-megajoules*(megajoules + 179751035747363528*mass)/mass**2))/299792458
    return should_be_answer * 1000

# print(get_speed(mass, joules))

velocity = get_speed(mass, joules)
print("[KIN] Speed: {:,.0f} m/s".format(velocity))

velocity = get_relativistic_speed(mass, megajoules)
print("[REL] Speed: {:,.0f} m/s".format(velocity))

# 2204748
# 2204792.7592354044

def get_percent_of_c(velocity):
    return velocity / 296794533.42 * 100

print("[REL] Speed of Light: {:.1f}%".format(get_percent_of_c(velocity)))
