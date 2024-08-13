from Data import Data
from Patient import Patient
from math import nan

def daily_positive(test,data):
    result = []
    for day in range(data.number_of_days()):
        n = 0
        for patient in range(data.number_of_patients(day)):
            if (data.patient(day,patient).get_value(test+"LABRESULT")==test+"_POS"): n+=1
        result.append(n)
    return result

def daily_negative(test,data):
    result = []
    for day in range(data.number_of_days()):
        n = 0
        for patient in range(data.number_of_patients(day)):
            if (data.patient(day,patient).get_value(test+"LABRESULT")==test+"_NEG"): n+=1
        result.append(n)
    return result

def _safe_divide(x,y):
    if (y==0.0): return 0.0
    else: return x/y

def daily_positivity(test,data):
    positive = daily_positive(test,data)
    negative = daily_negative(test,data)
    return [_safe_divide(p,n) for (p,n) in zip(positive,negative)]

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

def find_max_index(L):
    max = L[0]
    max_i = 0
    for i in range(len(L)):
        if L[i]>L[max_i]:
            max_i=i
            max = L[i]
    return max_i

