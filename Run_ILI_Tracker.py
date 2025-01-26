#!/usr/bin/env python3
import os

from Data import Data
from Misc import *
from datetime import date
from ILI_Tracker import ili_tracker
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------------------

data_directory = './data'
data_file = 'Sample_Data.csv'
diseases = ['INFLUENZA','RSV','HMPV','PARAINFLUENZA','OTHER']
ll_fields = [disease+'_loglikelihood_T' for disease in diseases]
priors = normalize([(0.1/(len(diseases)-1)) if dx!='OTHER' else 0.9 for dx in diseases],1.0)
admission_date_field, delimiter, file_missing_value, data_missing_value, base = 'Admit_date_time', ',', 'M', 'M', 10.0
equivalent_sample_size, moving_average_window = 10, 7

# ------------------------------------------------------------------------

data = Data(admission_date_field, delimiter, file_missing_value, data_missing_value, data_directory + os.sep + data_file)
ili_tracker_results = ili_tracker(diseases, priors, ll_fields, equivalent_sample_size, base, data)
daily_log_probability = ili_tracker_results['daily_log_probability']

# ----------------------------------------------------------------------

dates = data.dates()
xticks = [dates.index(date) for date in dates if date.day==1]
xticklabels = [str(dates[d].month)+'/'+str(dates[d].year) for d in xticks]

# ----------------------------------------------------------------------

fig, axes = plt.subplots(len(diseases))
fig.tight_layout(pad=2.0)
fig.set_size_inches(16,10)

for i in range(len(diseases)):
    axes[i].set_title(diseases[i])
    axes[i].plot(moving_average(moving_average_window,ili_tracker_results[diseases[i]]), color='blue')
    axes[i].set_ylabel('ILI Tracker', color='blue')
    axes[i].set_xticks(xticks)
    axes[i].set_xticklabels(xticklabels)
    axes[i].secondary_xaxis("top")

output_png_file = data_directory + os.sep + data_file + '.png'
plt.savefig(output_png_file)

print("The Output of ILI Tracker saved to: ", output_png_file)

# ------------------------------------------------------------------------

quit()

# ------------------------------------------------------------------------

