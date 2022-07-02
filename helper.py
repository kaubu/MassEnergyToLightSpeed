import decimal

def get_percent_of_c(velocity):
    return velocity / 299792458.0 * 100.0

while True:
    tons_of_tnt = decimal.Decimal(input("Tons of TNT: "))
    # mass = decimal.Decimal(input("Mass (in kg): "))

    joules = tons_of_tnt * decimal.Decimal(4.184)
    megajoules = tons_of_tnt * 4184

    print("Joules: {}".format(joules))
    print("Megajoules: {}".format(megajoules))

    unformatted_result = float(input("Unformatted result: "))

    print("Formatted result:\n{:,.0f} m/s".format(unformatted_result))

    print("Speed of Light: {}%".format(get_percent_of_c(unformatted_result)))
    print()
