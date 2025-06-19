import math
import matplotlib
import numpy
import tkinter
from tkinter import ttk


def Acc_perc(com_var_t, acc_var_t, miss_var_t):
    A1 = (com_var_t - acc_var_t - miss_var_t) * 100
    A2 = acc_var_t * 50
    A3 = (A1 + A2) / com_var_t
    return round(A3,2)  # Just return the float

def OD_Multi(EZ_HR_var_t, DT_HT_var_t):
    mod_combo = (EZ_HR_var_t, DT_HT_var_t)

    mapping = {
        ("EZ_t", "Off"): 2,
        ("HR_t", "Off"): 1 / 1.4,
        ("Off", "DT_t"): 3 / 2,
        ("Off", "HT_t"): 3 / 4,
        ("EZ_t", "HT_t"): 3 / 2,
        ("HR_t", "HT_t"): 3 / 5.6,
        ("EZ_t", "DT_t"): 3,
        ("HR_t", "DT_t"): 3 / 2.8
    }

    return mapping.get(mod_combo, 1.0)  # Default multiplier is 1.0

def OD_multi2(DT_HT_var_t):
    mod_sel = (DT_HT_var_t)

    mapping = {
        ("Off"): 1,
        ("DT_t"): 1.5,
        ("HT_t"): 0.75
    }
    return mapping.get(mod_sel, 1.0)

def OD_base(DT_HT_var_t):
    mod_sel2 = (DT_HT_var_t)

    mapping = {
        ("Off"): 50,
        ("DT_t"): 33,
        ("HT_t"): 66
    }
    return mapping.get(mod_sel2, 1.0)

def ODt_calc_22t(OD_var_t, EZ_HR_var_t, DT_HT_var_t):
    try:
        OD = float(OD_var_t)
        rounded_OD = math.ceil(OD / (1/3)) * (1/3)  # Round OD to nearest 1/3
        multiplier = OD_Multi(EZ_HR_var_t, DT_HT_var_t)
        Base = OD_base(DT_HT_var_t)

        # Calculate ms_t with correct operator precedence
        ms_t = (Base - (3 * rounded_OD / multiplier))

        # Clamp min/max depending on mod combo
        mod_combo = (EZ_HR_var_t, DT_HT_var_t)
        if mod_combo == ("HR_t", "Off"):
            ms_t = max(ms_t, 20)
        elif mod_combo == ("HR_t", "DT_t"):
            ms_t = max(ms_t, 40 / 3)
        elif mod_combo == ("Off", "DT_t"):
            ms_t = max(ms_t, 40 / 3)

        return round(ms_t, 3)
    except (ValueError, TypeError) as e:
        return f"Invalid OD: {e}"
    
def PP_calc_2022_09(star_var_t, com_var_t, miss_var_t, Acc_perc, EZ_mul, HD_mul, FL_mul, OD_var_t, EZ_HR_var_t, DT_HT_var_t, FL_var_t, HD_var_t):
    ms = ODt_calc_22t(OD_var_t, EZ_HR_var_t, DT_HT_var_t)

    Diff = pow(5 * max(star_var_t / 0.115, 1) - 4, 2.25) / 1150
    DiffLength = 1 + (min(com_var_t / 1500, 1) / 10)
    Diff *= DiffLength
    Diff *= pow(0.986, miss_var_t)
    Diff *= pow(Acc_perc / 100, 2)
    def Mod_multi(EZ_HR_var_t, HD_var_t, FL_var_t):
        Mult = 1
        if EZ_HR_var_t == "HR_t":
            Mult *= 1.05
        if EZ_HR_var_t == "EZ_t":
            Mult *= 0.985
        if HD_var_t == True:
            Mult *= 1.025
        if FL_var_t == True:
            Mult *= 1.05 * DiffLength
        return Mult
    Diff *= Mod_multi(EZ_HR_var_t, HD_var_t, FL_var_t)

    Acc = pow(60 / ms, 1.1) * pow(Acc_perc / 100, 8) * pow(star_var_t, 0.4) * 27
    AccLength = min(1.15, pow(com_var_t / 1500, 0.3))
    Acc *= AccLength

    def Mod_Multi2(HD_var_t, FL_var_t):
        Mult = 1
        if HD_var_t == True and FL_var_t == True:
            Mult *= max(1, 1.1 * AccLength)
        return Mult
    Acc *= Mod_Multi2(HD_var_t, FL_var_t)

    def Mod_Multi3(EZ_HR_var_t, HD_var_t):
        Mult = 1.13
        if EZ_HR_var_t == "EZ_t":
            Mult *= 0.975
        if HD_var_t == True:
            Mult *= 1.075
        return Mult
    
    PP = pow(pow(Diff, 1.1) + pow(Acc, 1.1), 1 / 1.1) * Mod_Multi3(EZ_HR_var_t, HD_var_t)
    return PP

    
