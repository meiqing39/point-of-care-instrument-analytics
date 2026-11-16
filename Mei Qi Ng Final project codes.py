# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 19:38:06 2026

@author: Maggie
"""

# Load packages and files, Inspect, and clean

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

pd.set_option("display.width", 140)    # shows more columns before pandas cuts display, use to inspect wide table
pd.set_option("display.max_columns", 40)

REPO      = "https://raw.githubusercontent.com/meiqing39/point-of-care-instrument-analytics/main/"
RALS_URL  = REPO + "RAL%20Workload%20summary%20year%20to%20date.xlsx"
ROTEM_URL = REPO + "GEMWEB%20Rotem%20Sigma%20Validation.csv"