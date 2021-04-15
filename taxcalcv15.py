def IfNegative(data):
    # validator for input data as to prevent negative inputs
    if data < 0:
        raise ValueError

def MPF(inc):
    # MPF calculation
    # 7100 is the minimum income level per month
    IfNegative(inc)
    if inc > (7100 * 12):
        mpf = inc * 0.05
    elif inc <= (7100 * 12):
        mpf = 0
    if mpf > 18000:
        mpf = 18000
    IfNegative(mpf)
    return mpf

def StandardTax(inc):
    IfNegative(inc)
    # calculation for standard tax
    Standard_tax = (inc - 18000) * 0.15
    if Standard_tax < 0:
        Standard_tax = 0

    IfNegative(Standard_tax)
    return Standard_tax

def SalaryTax(inc):
    if inc <= 2040023:
        if inc * 0.05 >= 18000:
            NetChargableIncome = inc - 18000 - 132000
            if NetChargableIncome < 0:
                NetChargableIncome = 0
            else:
                NetChargableIncome = NetChargableIncome

        elif inc * 0.05 <= 18000:
            NetChargableIncome = inc - (inc * 0.05) - 132000
            if NetChargableIncome < 0:
                NetChargableIncome = 0
            else:
                NetChargableIncome = NetChargableIncome

            # cal for the tax payable
        if NetChargableIncome <= 50000:
            SalaryTax = NetChargableIncome * 0.02
        elif 50000 < NetChargableIncome <= 100000:
            SalaryTax = (NetChargableIncome - 50000) * 0.06 + (50000 * 0.02)
        elif 100000 < NetChargableIncome <= 150000:
            SalaryTax = (NetChargableIncome - 50000 - 50000) * 0.1 + (50000 * 0.06) + (50000 * 0.02)
        elif 150000 < NetChargableIncome <= 200000:
            SalaryTax = (NetChargableIncome - 50000 - 50000 - 50000) * 0.14 + (50000 * 0.02) + (
                    50000 * 0.06) + (50000 * 0.1)
        elif NetChargableIncome > 200000:
            SalaryTax = (NetChargableIncome - 50000 - 50000 - 50000 - 50000) * 0.17 + (50000 * 0.02) + (
                    50000 * 0.06) + (50000 * 0.1) + (50000 * 0.14)
        if SalaryTax < 0:
            SalaryTax = 0
        else:
            SalaryTax = SalaryTax

        IfNegative(SalaryTax)
        return SalaryTax

    elif inc > 2040023:
        SalaryTax=StandardTax(inc)

    if SalaryTax < 0:
        SalaryTax = 0
    else:
        SalaryTax = SalaryTax
        IfNegative(SalaryTax)
        return SalaryTax

def TotalSalarytax(Husband_inc, Wife_inc):
    IfNegative(Husband_inc)
    IfNegative(Wife_inc)
    totalincome= Husband_inc + Wife_inc
    totalC= totalincome - 264000 - MPF(Husband_inc) - MPF(Wife_inc)

    if totalincome > 3167023:
        TotalSalarytax = (totalincome- MPF(Husband_inc)- MPF(Wife_inc))*0.15
        return TotalSalarytax
    elif totalincome <= 3167023:
        if totalC <= 50000:
            TotalSalarytax = totalC * 0.02
        elif 50000 < totalC <= 100000:
            TotalSalarytax = (totalC - 50000) * 0.06 + (50000 * 0.02)
        elif 100000 < totalC <= 150000:
            TotalSalarytax = (totalC - 100000) * 0.1 + (50000 * 0.06) + (50000 * 0.02)
        elif 150000 < totalC <= 200000:
            TotalSalarytax = (totalC - 150000) * 0.14 + (50000 * 0.02) + (
                    50000 * 0.06) + (50000 * 0.1)
        elif totalC > 200000:
            TotalSalarytax = (totalC - 200000) * 0.17 + (50000 * 0.02) + (
                    50000 * 0.06) + (50000 * 0.1) + (50000 * 0.14)

        return TotalSalarytax



def SeparateTotal(Husband_inc,Wife_inc):
    SeparateHusb = SalaryTax(Husband_inc)
    SeparateWife = SalaryTax(Wife_inc)
    Separate = SeparateHusb + SeparateWife
    return Separate

def Recommendation(Husband_inc, Wife_inc):
    separateTotal=SeparateTotal(Husband_inc,Wife_inc)
    jointTotal = TotalSalarytax(Husband_inc, Wife_inc)
    print("If separate assessment is used, need to pay for a total of", separateTotal, "HKD", "\n",
          "Husband needs to pay for", SalaryTax(Husband_inc), "HKD", "\n",
          "Wife needs to pay for", SalaryTax(Wife_inc), "HKD", "\n",
          "If joint assessment is used, need to pay for a total of", jointTotal, "HKD")
    if separateTotal < jointTotal:
        print("Joint assessment is not recommended, Separate assessment is better")
    elif separateTotal > jointTotal:
        print("Joint assessment is recommended")

def ContOrNot(answer):
    # continue the program for more calculations or not
    if answer == "Y" or answer == "y":
        main()
    elif answer =="N" or answer =="n":
        print("OK,bye")
    else:
        print("Invalid input! Please try again")

def main():
    while True:
        try:
                print(
                    "please type '0' in wife annual income if you only wants to calculate salary tax for 1 person")
                Husband_inc = int(input("Please enter husband annual income:"))
                Wife_inc = int(input("Please enter wife annual income:"))
                IfNegative(Husband_inc)
                IfNegative(Wife_inc)
                print("Annual MPF mandatory contribution based on personal income of Husband : ", MPF(Husband_inc), "\n",
                      "Annual MPF mandatory contribution based on personal income of Wife :", MPF(Wife_inc), "\n",
                      "Salaries Tax to be paid for husband if separate assessment :", SalaryTax(Husband_inc),"\n",
                      "Salaries Tax to be paid for wife if separate assessment : ", SalaryTax(Wife_inc), "\n",
                      "Total Salaries Tax to be paid in total:",SalaryTax(Husband_inc) + SalaryTax(Wife_inc),"\n",
                      "Salaries Tax to be paid if joint assessment :", TotalSalarytax(Husband_inc, Wife_inc), "\n")
                Recommendation(Husband_inc,Wife_inc)
                ContOrNot(input("Continue to use the program or Not, (Y/N)"))

        except ValueError:
            print("invalid value exist.")
if __name__ == '__main__':
    main()