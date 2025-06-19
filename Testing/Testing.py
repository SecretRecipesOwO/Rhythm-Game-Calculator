import math 
import numpy
from scipy.special import erf, erfinv
import tkinter as tk



def PP_Calc_2025_03(star_var_t, com_var_t, miss_var_t, Mono_var_t, EZ_mul, HD_mul, FL_mul, ODt_Calc_25t, acc_var_t):
    Base_Diff = 5 * max(1, star_var_t / 0.11) - 4
    Length_Bonus_Diff = 1 + (min(1,com_var_t / 1500 ) / 10)
    Diff = min((pow(Base_Diff,3) / 69052.51), (pow(Base_Diff, 2.25) / 1250)) * (1 + (max(0, star_var_t - 10)) / 10) * Length_Bonus_Diff * pow(0.986, miss_var_t) * pow(erf((500 - 300 * Mono_var_t) / (math.sqrt(2) * EUR_Calc)), 2 * Mono_var_t)
    Diff *= EZ_mul
    Diff *= HD_mul
    Diff *= FL_mul
    return Diff
