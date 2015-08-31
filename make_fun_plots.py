
import calculus_plotter, fun_plots

from numpy import linspace

rangex = linspace(-5,15,50,endpoint=True)

for h in fun_plots.funclist:
    calculus_plotter.plot_all(h,rangex)
