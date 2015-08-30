#!/usr/bin/python


import midpoint
import fun_plots
import calculus_plotter

def plot_easy_fun():
    calculus_plotter._plot(fun_plots.easy)

def plot_exp_saturation():
    calculus_plotter._plot(fun_plots.exp_saturation)

def plot_exp_growth():
    calculus_plotter._plot(fun_plots.exp_growth)

def plot_sine_and_cos():
    calculus_plotter._plot(fun_plots.sine_and_cos)

def plot_sine_sq():
    calculus_plotter._plot(fun_plots.sine_sq)


if __name__ == "__main__":
	plot_easy_fun()
	plot_exp_saturation()
	plot_exp_growth()
        plot_sine_and_cos()
        plot_sine_sq()
