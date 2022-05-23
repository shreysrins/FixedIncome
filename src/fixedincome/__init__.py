"""
FixedIncome
===========
Provides tools for Fixed Income analytics

This package was developed for 15.438 Fixed Income Securities and Derivatives at the MIT Sloan School of Management. Its recommended usage is as
    >>> import fixedincome as fi
Documentation is available through the built-in ``help`` function.

Available subpackages
---------------------
    utils
        Basic functions useful for fixed income applications.
    bonds
        Functions useful for analyzing fixed rate bonds.
    yield_curve
        Functions useful for constructing yield curves.
"""

__all__ = ['utils', 'bonds', 'yield_curve']

from fixedincome import *
