weight = float(input("enter the weight of the package: "))

if 0 < weight <= 2:
    prin("shipping cost: $2.5")
    elif weight <= 4:
        print("shipping cost: $4.5")
        elif weight <= 10:
            print("shipping cost: $7.5")
            elif weight <= 20:
                print("shipping cost: $10.5")
                else:
                    print("the package cannot be shipped.")
