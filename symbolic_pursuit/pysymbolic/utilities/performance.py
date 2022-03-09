# Copyright (c) 2019, Ahmed M. Alaa
# Licensed under the BSD 3-clause license (see LICENSE.txt)

from __future__ import absolute_import, division, print_function

import itertools
import os
import sys
import time
import warnings

import numpy as np
import pandas as pd
import scipy as sc
from mpmath import *
from sympy import *

warnings.filterwarnings("ignore")
if not sys.warnoptions:
    warnings.simplefilter("ignore")

from pysymbolic.models.special_functions import MeijerG


def compute_Rsquared(f_true, f_est):

    R2 = 1 - (np.mean((f_true - f_est) ** 2) / np.mean((f_true - np.mean(f_true)) ** 2))

    return R2


def mean_confidence_interval(data, confidence=0.95):

    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), sc.stats.sem(a)
    h = se * sc.stats.t.ppf((1 + confidence) / 2.0, n - 1)

    return m, h


def scrambled(orig):

    dest = orig[:]
    np.random.shuffle(dest)

    return dest


def partition_(lst, n):

    division = len(lst) / float(n)

    return [
        lst[int(round(division * i)) : int(round(division * (i + 1)))] for i in range(n)
    ]
