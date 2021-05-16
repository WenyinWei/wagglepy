from sympy import sin, sinh, pi, symbols
a = symbols("a", positive=True)
b, t = symbols("b, t", real=True)
find_all_trig_period(sin((b**2)*t)+sin(b*t), t)