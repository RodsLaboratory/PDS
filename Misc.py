# Copyright 2024 University of Pittsburgh
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
#
# Authors:  John Aronis

from Data import Data
from Patient import Patient
from math import nan

def empirical_p(window_size, min_window_size, daily_log_probability):
    result = []
    for day in range(len(daily_log_probability)):
        if day<=min_window_size:
            result.append(nan)
            continue
        day_log_p = daily_log_probability[day]
        window = daily_log_probability[max(0,day-window_size):day]
        larger = 0
        for x in window:
            if (x<day_log_p): larger+=1
        result.append(larger/len(window))
    return result

def moving_average(window_size,list_of_numbers):
    result = []
    length = len(list_of_numbers)
    for i in range(len(list_of_numbers)):
        window = list_of_numbers[int(max(0,i-window_size/2)):int(min(length-1,i+window_size+2))]
        average = sum(window)/len(window)
        result.append(average)
    return result

# End-of-File

