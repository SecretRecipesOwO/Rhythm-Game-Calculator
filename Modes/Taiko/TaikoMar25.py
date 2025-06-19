import tkinter as tk
from tkinter import ttk
import math
import matplotlib
from scipy.special import erf, erfinv

def OD_Multi(EZ_HR_var_t, DT_HT_var_t):
    mod_combo = (EZ_HR_var_t.get(), DT_HT_var_t.get())

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
    mod_sel = (DT_HT_var_t.get())

    mapping = {
        ("Off"): 1,
        ("DT_t"): 1.5,
        ("HT_t"): 0.75
    }
    return mapping.get(mod_sel, 1.0)

def OD_base(DT_HT_var_t):
    mod_sel2 = (DT_HT_var_t.get())

    mapping = {
        ("Off"): 49,
        ("DT_t"): 33,
        ("HT_t"): 66
    }
    return mapping.get(mod_sel2, 1.0)

def ODt_calc_25t(OD_var_t, EZ_HR_var_t, DT_HT_var_t):
    try:
        OD = float(OD_var_t.get())
        rounded_OD = math.ceil(OD / (1/3)) * (1/3)  # Round OD to nearest 1/3
        multiplier = OD_Multi(EZ_HR_var_t, DT_HT_var_t)
        multi2 = OD_multi2(DT_HT_var_t)
        Base = OD_base(DT_HT_var_t)

        # Calculate ms_t with correct operator precedence
        ms_t = (Base - (3 * rounded_OD / multiplier)) + (0.5 / multi2)

        # Clamp min/max depending on mod combo
        mod_combo = (EZ_HR_var_t.get(), DT_HT_var_t.get())
        if mod_combo == ("HR_t", "Off"):
            ms_t = max(ms_t, 20)
        elif mod_combo == ("HR_t", "DT_t"):
            ms_t = max(ms_t, 40 / 3)
        elif mod_combo == ("Off", "DT_t"):
            ms_t = max(ms_t, 40 / 3)

        return round(ms_t, 3)
    except (ValueError, TypeError) as e:
        return f"Invalid OD: {e}"

def PP_Calc_2025_03(star_var_t, com_var_t, miss_var_t, EZ_mul, HD_mul, FL_mul, acc_var_t, ms, HDFL_mul):
    def inner_calc(Mono_var_t):
        Base_Diff = 5 * max(1, star_var_t / 0.11) - 4
        Length_Bonus_Diff = 1 + (min(1, com_var_t / 1500) / 10)
        n = com_var_t
        great = n - (miss_var_t + acc_var_t)
        p = great / n
        z = 2.32634787404
        p_lower = (n * p + z**2 / 2) / (n + z**2) - z / (n + z**2) * math.sqrt(n * p * (1 - p) + z**2 / 4)
        EUR = 10 * (ms / (1.414213562 * erfinv(p_lower)))
        EMF = max(1, 1000 / (great + acc_var_t)) * miss_var_t

        Diff = min((Base_Diff**3 / 69052.51), (Base_Diff**2.25 / 1250)) \
               * (1 + max(0, star_var_t - 10) / 10) * Length_Bonus_Diff * pow(0.986, EMF)
        Diff *= EZ_mul * HD_mul * FL_mul

        Acc_scale_exp = 2 + Mono_var_t
        Acc_scale_shift = 500 - 100 * Mono_var_t * 3
        Diff *= pow(erf(Acc_scale_shift / (1.414213562 * EUR)), Acc_scale_exp)

        AccBonus = min(1.15, pow(com_var_t / 1500, 0.3))
        Acc = pow(70 / EUR, 1.1) * pow(star_var_t, 0.4) * 100 * AccBonus * HDFL_mul

        def FINMUL(EZ_mul, HD_mul):
            if EZ_mul == 1 and HD_mul == 1:
                return 1
            elif EZ_mul == 0.9 and HD_mul == 1:
                return 0.95
            elif EZ_mul == 1 and HD_mul == 1.025:
                return 1.075
            elif EZ_mul == 0.9 and HD_mul == 1.025:
                return 0.95 * 1.075
            else:
                return 1

        PP = pow(pow(Diff, 1.1) + pow(Acc, 1.1), 1 / 1.1) * (1.13 * FINMUL(EZ_mul, HD_mul))
        return round(PP, 3)

    pp_low_mono = inner_calc(2 / 9)
    pp_high_mono = inner_calc(23 / 32)
    return f"{pp_high_mono} to {pp_low_mono}"
