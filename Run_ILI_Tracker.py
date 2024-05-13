#!/usr/bin/env python3

# Copyright 2024 University of Pittsburgh
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
#
# Authors:  John Aronis

from Data import Data
from Misc import *
from ILI_Tracker import ili_tracker
from math import nan
import numpy as np
import matplotlib.pyplot as plt
from brokenaxes import brokenaxes

# ----------------------------------------------------------------------

diseases  = [      'FLU',        'RSV',     'OTHER']
priors    = [       0.10,        0.10,        0.90]
ll_fields = ['log10_FLU', 'log10_RSV', 'log10_OTHER'] 

data_file = 'data_flu500_rsv500_other500.csv'
data_file = 'data_temp.csv'

equivalent_sample_size = 10
base = 10.0
modeled_diseases = [dx for dx in diseases if dx!='OTHER']
empirical_p_window = 21
min_empirical_p_window = 10
window = 7

start = '20140601'
end   = '20150531'

# ----------------------------------------------------------------------

data = Data(data_file, start, end)
dates = data.dates

ili_tracker_results = ili_tracker(diseases, priors, ll_fields, equivalent_sample_size, base, data)
daily_log_probability = ili_tracker_results['daily_log_probability']
daily_empirical_p = empirical_p(empirical_p_window,min_empirical_p_window,daily_log_probability)

# ----------------------------------------------------------------------

xticks =      [    0,    30,    61,    92,    122,    153,    183,   214,   245,   273,   304,   334,    364]
xticklabels = ['6/1', '7/1', '8/1', '9/1', '10/1', '11/1', '12/1', '1/1', '2/1', '3/1', '4/1', '5/1', '5/31']

yticklabels0 = ['p=1', 'p=0.1', 'p=0.01', 'p=0.001']

# ----------------------------------------------------------------------

fig, axes = plt.subplots(3)
fig.tight_layout(pad=2.0)
fig.set_size_inches(12,8)

axes[0].plot(moving_average(window,ili_tracker_results['FLU']))
axes[0].set_ylabel('Influenza')
axes[0].set_xticks(xticks)
axes[0].set_xticklabels(xticklabels)
axes[0].secondary_xaxis("top")
    
axes[1].plot(moving_average(window,ili_tracker_results['RSV']))
axes[1].set_ylabel('RSV')
axes[1].set_xticks(xticks)
axes[1].set_xticklabels(xticklabels)
axes[1].secondary_xaxis("top")

#axes[2].set_yscale('symlog')
axes[2].plot(daily_empirical_p)
axes[2].set_ylabel('Empirical p')
axes[2].set_xticks(xticks)
axes[2].set_xticklabels(xticklabels)
axes[2].secondary_xaxis("top")

axes[2].axhline(0.1,color='red')
axes[2].axhline(0.001,color='red')
    
plt.show()

# ----------------------------------------------------------------------

quit()

# ----------------------------------------------------------------------

