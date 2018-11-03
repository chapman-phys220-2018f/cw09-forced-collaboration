#!/usr/bin/env python3
# -*- coding: utf-8 -*-


###
# Name: Morgan Holve
# Student ID: 2281337
# Email: holve100@mail.chapman.edu
# Course: MATH220 Fall 2018
# Assignment: Classwork 9
###

"""This module computes the derivative of a function at some x throught the techniques of matricies."""

import numpy as np
import matplotlib.pyplot as plt

def gradient(x):
    """Creates the gradient of some range of x values"""
    dx = x[1] - x[0]
    dim = len(x)
    gradient = (((np.tri(len(x), len(x), 1) - np.tri(len(x), len(x), 0))) + (np.tri(len(x), len(x), -2) - np.tri(len(x), len(x), -1))) / (2*dx)

    gradient[0][0] = -1 / dx
    gradient[0][1] = 1 / dx
    gradient[-1][-1] = 1 / dx
    gradient[-1][-2] = -1 / dx
    
    return gradient

def squared_plot():
    """Computes the derivative of x^2"""
    f = plt.figure(figsize = (16,12))
    cartesian = plt.axes()
    plt.ylim(0,10)
    
    x = np.arange(0, 10, .01)
    fx = x**2
    
    grad = gradient(x)
    deriv = grad @ fx

    cartesian.plot(x, fx, label="$f(x)$")
    cartesian.plot(x, deriv, color="Red")
    cartesian.legend()
    cartesian.set(xlabel="x", ylabel="y", title="$x^2$")
    plt.show()
                    
def squared_plot_compare():
    """Computes the derivative of x^2 using the numpy function"""
    x = np.arange(0, 10, .01)
    fx = x**2

    grad = np.gradient(x)
    deriv = grad @ fx
    print(deriv[:15])
def sine_plot():
    """Computes the derivative of sin(x)"""
    f = plt.figure(figsize = (16,12))
    cartesian = plt.axes()
    plt.ylim(-2,2)
    
    x = np.arange(0, 10, .1)
    fx = np.sin(x)
    
    grad = gradient(x)
    deriv = grad @ fx


    cartesian.plot(x, fx, label="$f(x)$")
    cartesian.plot(x, deriv, color="Red")
    cartesian.legend()
    cartesian.set(xlabel="x", ylabel="y", title="$\sin(x)$")
    plt.show()

def sine_plot_compare():
    """Computes the derivative of sin(x) through the numpy function"""
    x = np.arange(15, .01)
    fx = np.sine(x)
    fdx3 = np.gradient(fx)
    cartesian = plt.axes()
    cartesian.plot(x, fx, label="$f(x)$")
    cartesian.plot(x, fdx3, color="Red", label="Derivative of $f(x) with Numpy Function$")
    cartesian.legend()
    cartesian.set(xlabel="x", ylabel="y", title="$\sin(x)$")
    plt.show()
               
def exp_plot():
    """Computes the derivative of e^stuff"""
    f = plt.figure(figsize = (16,12))
    cartesian = plt.axes()
    plt.ylim(-1,1)
    
    x = np.arange(0, 10, .1)
    fx = np.exp(-x**2/2)/np.sqrt(2*np.pi)
    
    grad = gradient(x)
    deriv = grad @ fx


    cartesian.plot(x, fx, label="$f(x)$")
    cartesian.plot(x, deriv, color="Red", label = "Derivative of $f(x)$")
    cartesian.legend()
    cartesian.set(xlabel="x", ylabel="y", title="function")
    plt.show()
          
def exp_plot_compare():
    """Computes the derivative of e^stuff throught the numpy function"""
    x = np.arange(15, .01)
    fx = np.exp(-x**2/2)/np.sqrt(2*np.pi)
    fdx3 = np.gradient(fx)
    cartesian = plt.axes()
    cartesian.plot(x, fx, label="$f(x)$")
    cartesian.plot(x, fdx3, color="Red", label="Derivative of $f(x)$ with Numpy Function")
    cartesian.legend()
    cartesian.set(xlabel="x", ylabel="y", title="$\frac{e^{\frac{-x^2}{2}}}{\sqrt{2\pi}}$")
    plt.show()