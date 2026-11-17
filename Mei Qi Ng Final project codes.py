# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 19:38:06 2026

@author: Maggie
"""
# Research Q: 
   #Can automated Python analysis of POC middleware exports support both 
   #resource and quality decisions? 
   #Specifically: 
   #(1) which units could have devices 
   #consolidated based on testing volume and QC burden, and
   #(2) is the newly installed ROTEM Sigma at Labor & Delivery producing consistent, 
   #in-range results ready for clinical use?”




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
RALS  = REPO + "RAL%20Workload%20summary%20year%20to%20date.xlsx"
ROTEM = REPO + "GEMWEB%20Rotem%20Sigma%20Validation.csv"

# Load and view raw file

rals = pd.read_excel(RALS, header=None)

print(rals.head(10))


# clean column names and drop irrelevant/empty rows
rals.columns = ['Drop', 'Location', 'Test Type', 'Patient Results', 'QC Results', 'Proficiency', 'Other', 'Total Results']

# record device row before rows are dropped
device_row  = rals['Drop'].astype(str).str.startswith('Device Type :')
rals['Device'] = rals['Location'].where(device_row).ffill() 
rals['Device'] = rals['Device'].str.replace('®', '', regex=False).str.strip()


rals = rals.drop(columns=['Drop', 'Proficiency']).dropna(subset=['Location', 'Total Results']) #keep 'Other'

rals = rals[rals['Location'] != 'Location'] # remove duplicate header


# Convert column values to numeric (for stat calculation)

for col in ['Patient Results', 'QC Results', 'Other', 'Total Results']: 
    rals[col] = pd.to_numeric(rals[col], errors='coerce'). fillna(0)
    
rals['Test Type'] = rals['Test Type'].fillna('Other(no test)') # create label for blank test types

print(rals.head(5))
print(rals.groupby('Device')[['Patient Results', 'QC Results', 'Other', 'Total Results']].sum())