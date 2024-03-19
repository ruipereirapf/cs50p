def main():
    mass_input = int(input("Insert mass in kilograms: "))

    print("E =", einstein(mass_input))

def einstein(mass_input):
    m = mass_input
    c = int(300000000)
    e = m * c ** 2
    return e

main()