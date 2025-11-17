def linear(m,x,b):
    return m*x+b

def slope_units(x_units,y_units):
    x_stripped = x_units.rstrip("s")
    y_stripped = y_units.rstrip("s")
    return str(y_stripped) + "/" + str(x_stripped)

def print_equation(m,b,x_units,y_units):
    m_units = slope_units(x_units, y_units)
    print("The equation of the line is: y = " + str(m) + " " + m_units + " x + " + str(b) + " cm")
    
