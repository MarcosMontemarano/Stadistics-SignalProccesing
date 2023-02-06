#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:13:56 2020

@author: guillem
"""
import numpy as np

def circular_convolve(in1, in2, period):
    """
    Circular convolution of two 1-dimensional arrays.
    Circular convolve `in1` and `in2` with given `period`.
    Parameters
    ----------
    in1 : array_like, 1-D
        First input.
    in2 : array_like, 1-D
        Second input. Should have the same number of dimensions as `in1`.
  period : int
        Period of the circular convolution.
    Returns
    -------
    result : array, 1-D
        A 1-dimensional array containing the result of the circular
        convolution of `in1` with `in2`.
    See Also
    --------
    convolve
    Notes
    -----
    The (modulo-M) circular/cyclic/periodic convolution of period :math:`M`
    of the two signals :math:`x[k]` and :math:`h[k]` is defined as
    .. math::
        y[k] = \sum_{\kappa=0}^{M-1} \tilde{x}[k - \kappa] \; \tilde{h}[\kappa]
    where the periodic summations :math:`\tilde{x}[k]` and `\tilde{h}[\kappa]`
    of :math:`x[k]` and :math:`x[k]` are defined as
    .. math::
        \tilde{x}[k] &= \sum_{m = -\infty}^{\infty} x[m \cdot M + k] \\
        \tilde{h}[k] &= \sum_{m = -\infty}^{\infty} h[m \cdot M + k]
    Examples
    --------
    Equivalence of circular and linear convolution:
    >>> from scipy import signal
    >>> a = np.ones(5)
    >>> b = np.ones(5)
    >>> circular_convolve(a, b, 5)
    array([ 5.,  5.,  5.,  5.,  5.])
    >>> np.convolve(a, b, mode='full')
    array([ 1.,  2.,  3.,  4.,  5.,  4.,  3.,  2.,  1.])
    >>> circular_convolve(a, b, 9)
    array([ 1.,  2.,  3.,  4.,  5.,  4.,  3.,  2.,  1.])
    """
    in1 = _periodic_summation(in1, period)
    in2 = _periodic_summation(in2, period)

    return np.fromiter([np.dot(np.roll(in1[::-1], k+1), in2)
                        for k in np.arange(period)], float)


def _periodic_summation(x, period):
    """
    Periodic summation of 1-dimensional array or zero-padding.
    If the length of the array is longer or equal to the given `period`
    a periodic summation of `x` is perfomed, otherwise zero-padding to length
    `period`.
    """
    len_x = len(x)
    rows = int(np.ceil(len_x/period))

    if (len_x < int(period*rows)):
        x = np.pad(x, (0, int(period*rows-len_x)), 'constant')

    x = np.reshape(x, (rows, period))

    return np.sum(x, axis=0)

