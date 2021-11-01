from graphics import *

# Introduction
print("This program calculates the future value of an investment")

# Get principal and interest rate
pv = float(input("Enter the principal: "))
interest = float(input("Enter the annual intrest earned as a decimal: "))
yr = 10

# Create graphics window with labels
win = GraphWin('Investment Growth Chart', 320, 240)
win.setBackground('white')
win.setCoords(-1.75, -200, 11.5, 10400)
Text(Point(-1, 0), '0.0K').draw(win)
Text(Point(-1, 2500), '2.5K').draw(win)
Text(Point(-1, 5000), '5.0K').draw(win)
Text(Point(-1, 7500), '7.5K').draw(win)
Text(Point(-1, 10000), '10.0K').draw(win)

# Draw bar for initial principal
bar = Rectangle(Point(0, 0), Point(1, pv))
bar.setFill('green')
bar.setWidth(2)
bar.draw(win)

for year in range(1, 11):
    pv = pv * (1 + interest)
    bar = Rectangle(Point(year, 0), Point(year+1, pv))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(win)

input("Press <Enter> to quit")
win.close()