#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import array_calculus as a
import numpy as np

def test_gradient():
    """
    Tests that the gradient returns what I want it to
    """
    x = np.arange(0, 10, 1)
    test1 = a.gradient(x)
    test1 = test1[:5]
    assert np.array_equal(test1, np.array([[-1.,1.,0.,0.,0.,0.,0.,0.,0.,0.],[-0.5,0.,0.5,0.,0.,0.,0.,0.,0.,0.], [0.,-0.5,0.,0.5,0.,0.,0.,0.,0.,0.], [0.,0.,-0.5,0.,0.5,0.,0.,0.,0.,0.], [0.,0.,0.,-0.5,0.,0.5,0.,0.,0.,0.]]))

