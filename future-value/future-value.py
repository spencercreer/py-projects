print("This program calculates the future value of an investment")

pv = eval(input("Enter the principal: "))
interest = eval(input("Enter the annual intrest earned as a decimal: "))
yr = eval(input("Enter the number of years: "))


for i in range(yr):
    pv = pv * (1 + interest)

print("Future Value" + pv)
print("Annual Interest Rate" + interest)
print("Number of Years" + yr)