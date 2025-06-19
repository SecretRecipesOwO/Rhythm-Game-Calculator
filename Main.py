import tkinter as tk
import numpy as np
import matplotlib as mp
import math
from tkinter import ttk
from Modes.Taiko import TaikoMar25, TaikoOct24, TaikoSep22, TaikoSep20, TaikoMar14
from Visuals.Graphs.Taiko import GoodMissAccRatio
from PIL import Image, ImageTk
from tkinter import Canvas


Window = tk.Tk()
Window.geometry('1920x1080')
Window.title('Rhythm Game Calculator V1')
Window.configure(bg="#121212")
Window.minsize(width=1200, height=800)

# --- Custom styles for mod buttons ---
style = ttk.Style()
style.theme_use("default")

style.configure("EZ.TButton", background="#2CA82C", foreground="black")
style.map("EZ.TButton", background=[("active", "#279427")])
style.configure("HR.TButton", foreground="white", background="#ac0435")
style.map("HR.TButton", background=[("active", "#6d041e")])
style.configure("HD.TButton", background="#E6B625", foreground="black")
style.map("HD.TButton", background=[("active", "#c99e1f")])
style.configure("FL.TButton", background="#2B2B2B", foreground="white")
style.map("FL.TButton", background=[("active", "#222222")])
style.configure("DT.TButton", background="#30106B", foreground="white")
style.map("DT.TButton", background=[("active", "#522e92")])
style.configure("HT.TButton", background="#161627", foreground="White")
style.map("HT.TButton", background=[("active", "#1B1B30")])
style.configure("NF.TButton", background="#aab7b8", foreground="black")
style.map("NF.TButton", background=[("active", "#8b9d9e")])


ModeSelect=ttk.Notebook(Window)
ModeSelect.pack(expand=True)

frame1=ttk.Frame(ModeSelect, width=1920, height=1080)
frame2=ttk.Frame(ModeSelect, width=1920, height=1080)
frame3=ttk.Frame(ModeSelect, width=1920, height=1080)
frame4=ttk.Frame(ModeSelect, width=1920, height=1080)
frame5=ttk.Frame(ModeSelect,width=1920,height=1080)


frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)
frame5.pack(fill='both', expand=True)

ModeSelect.add(frame1, text='osu!Standard')

# --- Dropdown for Standard Reworks ---
standard_reworks = [
    "Select a Rework",
    "Mar 2025 - Now", 
    "Oct 2024 - Mar 2025", 
    "Sep 2022 - Oct 2024", 
    "Nov 2021 - Sep 2022", 
    "Jul 2021 - Nov 2021",
    "Jan 2021 - Jul 2021",
    "Feb 2019 - Jan 2021",
    "May 2018 - Feb 2019",
    "Apr 2015 - May 2018",
    "Feb 2015 - Apr 2015",
    "Jul 2014 - Feb 2015",
    "May 2014 - Jul 2014"
]

rework_label = ttk.Label(frame1, text="Select PP Rework:")
rework_label.pack(pady=(4, 0))

rework_dropdown_s = ttk.Combobox(
    frame1, 
    values=standard_reworks, 
    state="readonly"
)
rework_dropdown_s.current(0)  # default to first rework
rework_dropdown_s.pack(pady=(0, 4))
star_frame = ttk.Frame(frame1)
star_frame.pack(pady=(10, 5))

ttk.Label(star_frame, text="Star Rating:").pack(side="left", padx=(0, 5))

star_var = tk.DoubleVar(value=5.0)
star_entry = ttk.Entry(star_frame, textvariable=star_var, width=10)
star_entry.pack(side="left")
# --- Additional inputs ---
extra_inputs_frame = ttk.Frame(frame1)
extra_inputs_frame.pack(pady=(10, 5))

# Miss Count
ttk.Label(extra_inputs_frame, text="Misses:").grid(row=0, column=0, padx=5)
miss_var_s = tk.IntVar(value=0)
ttk.Entry(extra_inputs_frame, textvariable=miss_var_s, width=6).grid(row=0, column=1)

# Accuracy
ttk.Label(extra_inputs_frame, text="Accuracy (%):").grid(row=0, column=2, padx=5)
acc_var_s = tk.DoubleVar(value=100.0)
ttk.Entry(extra_inputs_frame, textvariable=acc_var_s, width=6).grid(row=0, column=3)

# Unstable Rate
ttk.Label(extra_inputs_frame, text="Unstable Rate:").grid(row=0, column=4, padx=5)
ur_var_s = tk.DoubleVar(value=150.0)
ttk.Entry(extra_inputs_frame, textvariable=ur_var_s, width=6).grid(row=0, column=5)

ttk.Label(extra_inputs_frame, text="Max Combo:").grid(row=1, column=0, padx=5, pady=5)
com_var_s = tk.IntVar(value=1250)
ttk.Entry(extra_inputs_frame, textvariable=com_var_s, width=6).grid(row=1, column=1)

# OD
ttk.Label(extra_inputs_frame, text="OD:").grid(row=1, column=2, padx=5, pady=5)
OD_var_s = tk.IntVar(value=5)
ttk.Entry(extra_inputs_frame, textvariable=OD_var_s, width=6).grid(row=1, column=3)

# HP
ttk.Label(extra_inputs_frame, text="HP:").grid(row=1, column=4, padx=5, pady=5)
HP_var_s = tk.IntVar(value=5)
ttk.Entry(extra_inputs_frame, textvariable=HP_var_s, width=6).grid(row=1, column=5)

# CS
ttk.Label(extra_inputs_frame, text="CS:").grid(row=2, column=0, padx=5)
CS_var_s = tk.IntVar(value=5)
ttk.Entry(extra_inputs_frame, textvariable=CS_var_s, width=6).grid(row=2, column=1)

# AR
ttk.Label(extra_inputs_frame, text="AR:").grid(row=2, column=2, padx=5)
AR_var_s = tk.IntVar(value=5.5)
ttk.Entry(extra_inputs_frame, textvariable=AR_var_s, width=6).grid(row=2, column=3)

# -----------------

ModeSelect.add(frame2, text='osu!Taiko (太鼓の達人)')

# --- Dropdown for Taiko Reworks ---
Taiko_reworks = [
    "Select a Rework",
    "Mar 2025 - Now", 
    "Oct 2024 - Mar 2025", 
    "Sep 2022 - Oct 2024", 
    "Sep 2020 - Sep 2022", 
    "Mar 2014 - Sep 2020"
]

rework_label = ttk.Label(frame2, text="Select PP Rework:")
rework_label.pack(pady=(4, 0))

rework_dropdown_t = ttk.Combobox(
    frame2, 
    values=Taiko_reworks, 
    state="readonly"
)
rework_dropdown_t.current(0)  # default to first rework
rework_dropdown_t.pack(pady=(0, 4))# Create left and right frames inside the Taiko tab
left_taiko_frame = ttk.Frame(frame2, width=500, height=1080)
left_taiko_frame.pack(side="left", fill="y", padx=10, pady=10)

right_taiko_frame = ttk.Frame(frame2, width=500, height=1080)
right_taiko_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
right_taiko_frame.pack_propagate(False)

Graph_taiko_frame = ttk.Frame(frame2, width=500, height=1080)
Graph_taiko_frame.pack(side="left", fill="y", padx=10, pady=10)
Graph_taiko_frame.pack_propagate(False)



# --- Notes frame ---
# --- Toggleable Side Panel for Taiko ---

# Container for left panel + toggle button
side_panel_wrapper = ttk.Frame(left_taiko_frame)
side_panel_wrapper.pack(side="left", fill="y", padx=(5, 10))

# Canvas button to simulate vertical toggle
toggle_canvas = Canvas(side_panel_wrapper, width=30, height=100, bg="#d9d9d9", highlightthickness=0)
toggle_canvas.pack(side="left", fill="y")

# Actual side panel (initially hidden)
side_panel = ttk.Frame(side_panel_wrapper, relief="ridge", padding=5, width=200)
side_panel_visible = False

bold_font = ("TkDefaultFont", 12, "bold")
size_down_font = ("TkDefaultFont", 9)
# Add content to the side panel
ttk.Label(side_panel, text="Variable Exclusivities:", font=bold_font).pack(anchor="nw", pady=5)
ttk.Label(side_panel, text="Mono Factor - Mar 2025 (auto set at 0.22 - 0.719)", font=size_down_font).pack(anchor="nw")
ttk.Label(side_panel, text="Inaccuracies:", font=bold_font).pack(pady=[10,5], anchor="nw")
ttk.Label(side_panel, text="Mar 2025 is a 99% Confidence, not perfect").pack(anchor="nw")
ttk.Label(side_panel, text="Sep 2022 is Perfect (Excluding SR truncation)").pack(anchor="nw")

# Draw vertical text
def draw_rotated_text(text):
    toggle_canvas.delete("all")
    toggle_canvas.create_text(15, 90, text=text, angle=90, fill="black", font=("Segoe UI", 10), tags="label")

# Handle click
def on_toggle_click(event=None):
    global side_panel_visible
    if side_panel_visible:
        side_panel.pack_forget()
        draw_rotated_text("▶ Open Panel")
    else:
        side_panel.pack(side="left", fill="y")
        draw_rotated_text("◀ Close Panel")
    side_panel_visible = not side_panel_visible

draw_rotated_text("▶ Open Panel")
toggle_canvas.bind("<Button-1>", on_toggle_click)


# --- Mods Frame to the left of inputs ---
mods_frame = ttk.Frame(left_taiko_frame)
mods_frame.pack(pady=(1, 5))

# Place mods_frame and extra_inputs_frame side by side
mods_and_inputs = ttk.Frame(left_taiko_frame)
mods_and_inputs.pack(pady=(0, 5))

mods_frame = ttk.Frame(mods_and_inputs)
mods_frame.pack(side="left", padx=(0, 0))

extra_inputs_frame = ttk.Frame(mods_and_inputs)
extra_inputs_frame.pack(side="left")

def toggle_mod(var, button, style_on, label):
    var.set(not var.get())
    if var.get():
        button.config(text=label, style=style_on)
    else:
        button.config(text="Off", style="TButton")  # Default unstyled

extra_inputs_frame = ttk.Frame(left_taiko_frame)
extra_inputs_frame.pack(pady=(10, 5))

ttk.Label(extra_inputs_frame, text="Star Rating:").grid(row=0,column=0, padx=5,pady=25)
star_var_t = tk.DoubleVar(value=5.0)
ttk.Entry(extra_inputs_frame, textvariable=star_var_t,width=6).grid(row=0,column=1,pady=25)

ttk.Label(extra_inputs_frame, text="Misses:").grid(row=1, column=0, padx=5)
miss_var_t = tk.IntVar(value=0)
ttk.Entry(extra_inputs_frame, textvariable=miss_var_t, width=6).grid(row=1, column=1)

ttk.Label(extra_inputs_frame, text="100s Count:").grid(row=2, column=0, padx=5, pady=5)
acc_var_t = tk.DoubleVar(value=100)
ttk.Entry(extra_inputs_frame, textvariable=acc_var_t, width=6).grid(row=2, column=1)

ttk.Label(extra_inputs_frame, text="Max Combo:").grid(row=3, column=0, padx=5, pady=5)
com_var_t = tk.DoubleVar(value=1250)
ttk.Entry(extra_inputs_frame, textvariable=com_var_t, width=6).grid(row=3, column=1)

ttk.Label(extra_inputs_frame, text="OD:").grid(row=4, column=0, padx=5)
OD_var_t = tk.DoubleVar(value=5)
ttk.Entry(extra_inputs_frame, textvariable=OD_var_t, width=6).grid(row=4, column=1)

# --- Mods and Inputs Frame ---
mods_and_inputs = ttk.Frame(left_taiko_frame)
mods_and_inputs.pack(pady=(10, 5))

# Left: Mods
mods_frame = ttk.Frame(mods_and_inputs)
mods_frame.pack(side="left", padx=(0, 0))

# Right: Input fields
extra_inputs_frame = ttk.Frame(mods_and_inputs)
extra_inputs_frame.pack(side="left")

def toggle_EZ_HR_t(var, button):
    current = var.get()
    if current == "Off":
        var.set("EZ_t")
        button.config(text="EZ", style="EZ.TButton")  # apply custom style if needed
    elif current == "EZ_t":
        var.set("HR_t")
        button.config(text="HR", style="HR.TButton")
    else:
        var.set("Off")
        button.config(text="Off", style="TButton")  # fallback/default style

def toggle_DT_HT_t(var, button):
    current = var.get()
    if current == "Off":
        var.set("DT_t")
        button.config(text="DT", style="DT.TButton")
    elif current == "DT_t":
        var.set("HT_t")
        button.config(text="HT", style="HD.TButton")
    else:
        var.set("Off")
        button.config(text="Off", style="TButton")



# Boolean variables for mod state
EZ_HR_var_t = tk.StringVar(value="False")
DT_HT_var_t = tk.StringVar(value="False")
HD_var_t = tk.BooleanVar(value=False)
FL_var_t = tk.BooleanVar(value=False)

# Mod toggle buttons
EZ_HR_t_btn = ttk.Button(mods_frame, text="Off", width=6,
    command=lambda: toggle_EZ_HR_t(EZ_HR_var_t, EZ_HR_t_btn))
EZ_HR_t_btn.grid(row=6, column=1)
ttk.Label(mods_frame, text="EZ/HR:").grid(row=6, column=0)

DT_HT_t_btn = ttk.Button(mods_frame, text="Off", width=6,
    command=lambda: toggle_DT_HT_t(DT_HT_var_t, DT_HT_t_btn))
DT_HT_t_btn.grid(row=9, column=1, pady=5)
ttk.Label(mods_frame,text="DT/HT:").grid(row=9, column=0, padx=8, pady=5)

HD_btn = ttk.Button(mods_frame, text="Off", width=6,
    command=lambda: toggle_mod(HD_var_t, HD_btn, "HD.TButton", "HD"))
HD_btn.grid(row=7, pady=5, column=1)
ttk.Label(mods_frame,text="Hidden:").grid(row=7, column=0, padx=8)

FL_btn = ttk.Button(mods_frame, text="Off", width=6,
    command=lambda: toggle_mod(FL_var_t, FL_btn, "FL.TButton", "FL"))
FL_btn.grid(row=8, column=1)
ttk.Label(mods_frame,text="Flashlight:").grid(row=8, column=0, padx=8)

from Modes.Taiko.TaikoMar25 import ODt_calc_25t
ODt_result_var = tk.StringVar()
ttk.Label(extra_inputs_frame, textvariable=ODt_result_var).grid(row=3, column=2, padx=[10,0])
ODt_result_var.set(str(ODt_calc_25t(OD_var_t, EZ_HR_var_t, DT_HT_var_t)))

def update_OD(*args):
    ODt_result_var.set(str(ODt_calc_25t(OD_var_t, EZ_HR_var_t, DT_HT_var_t)))
OD_var_t.trace_add("write", update_OD)
EZ_HR_var_t.trace_add("write", update_OD)
DT_HT_var_t.trace_add("write", update_OD)
ttk.Label(extra_inputs_frame, text="ms").grid(row=3,column=3)

def EZ_Detect_T1(EZ_HR_var_t):
    if EZ_HR_var_t == "EZ_t":
        return 0.9  # Easy reduces difficulty
    else:
        return 1  # "Off"
    
def HD_Detect_T1(HD_var_t):
    if HD_var_t == True:
        return 1.025
    else:
        return 1

def FL_Detect_T1(FL_var_t):
    if FL_var_t == True:
        return max(1, 1.05 - min(0.5 / 50, 1)) * (1 + (min(1,com_var_t.get() / 1500 ) / 10))
    else:
        return 1
    
def HDFL_Detect_T1(HD_raw, FL_raw):
    if HD_raw == True and FL_raw == True:
        return max(1, 1.05 * min(1.15, pow((com_var_t.get() / 1500), 0.3)))
    else:
        return 1


# --- Right: Single Panel ---
# Assuming all your input variables like miss_var_t, acc_var_t, etc. are defined
pp_result_var = tk.StringVar()
pp_result_var2 = tk.StringVar()
from Modes.Taiko.TaikoMar25 import PP_Calc_2025_03
def pp_taiko25():
    StarVT = star_var_t.get()
    ComboT = com_var_t.get()
    MissT = miss_var_t.get()
    EZ_raw = EZ_HR_var_t.get()
    EZ_mul = EZ_Detect_T1(EZ_raw)
    HD_raw = HD_var_t.get()
    HD_mul = HD_Detect_T1(HD_raw)
    FL_raw = FL_var_t.get()
    FL_mul = FL_Detect_T1(FL_raw)
    ms = ODt_calc_25t(OD_var_t, EZ_HR_var_t, DT_HT_var_t)
    HDFL_mul = HDFL_Detect_T1(HD_raw, FL_raw)
    AccT = acc_var_t.get()
    result = PP_Calc_2025_03(StarVT, ComboT, MissT, EZ_mul, HD_mul, FL_mul, AccT, ms, HDFL_mul)
    return result

nested_panel_t = ttk.Frame(right_taiko_frame)
nested_panel_t.pack(expand=True, fill="both")

def update_pp_label():
    star_value_t = star_var_t.get()
    Combo_t = com_var_t.get()
    Miss_t = miss_var_t.get()
    EZ_raw = EZ_HR_var_t.get()
    EZ_mul = EZ_Detect_T1(EZ_raw)
    HD_raw = HD_var_t.get()
    HD_mul = HD_Detect_T1(HD_raw)
    FL_raw = FL_var_t.get()
    FL_mul = FL_Detect_T1(FL_raw)
    ms = ODt_calc_25t(OD_var_t, EZ_HR_var_t, DT_HT_var_t)
    AccT = acc_var_t.get()
    HDFL_mul = HDFL_Detect_T1(HD_raw, FL_raw)
    result = PP_Calc_2025_03(star_value_t, Combo_t, Miss_t, EZ_mul, HD_mul, FL_mul, AccT, ms, HDFL_mul)
    pp_result_var.set(result)

def Acc_perc(com_var_t, acc_var_t, miss_var_t):
    A1 = (com_var_t - acc_var_t - miss_var_t) * 100
    A2 = acc_var_t * 50
    A3 = (A1 + A2) / com_var_t
    return A3

from Modes.Taiko.TaikoSep22 import PP_calc_2022_09
def pp_taiko22():
    StarVT = star_var_t.get()
    ms = ODt_calc_25t(OD_var_t, EZ_HR_var_t, DT_HT_var_t)
    Combo = com_var_t.get()
    meh = acc_var_t.get()
    miss = miss_var_t.get()
    acc = Acc_perc(Combo, meh, miss)
    EZ_raw = EZ_HR_var_t.get()
    EZ_mul = EZ_Detect_T1(EZ_raw)
    HD_raw = HD_var_t.get()
    HD_mul = HD_Detect_T1(HD_raw)
    FL_raw = FL_var_t.get()
    FL_mul = FL_Detect_T1(FL_raw)
    OD = OD_var_t.get()
    EZ_Det_t2 = EZ_HR_var_t.get()
    DT_Det_t2 = DT_HT_var_t.get()
    FL_bool = FL_var_t.get()
    HD_bool = HD_var_t.get()
    result = PP_calc_2022_09(StarVT, Combo, miss, acc, EZ_mul, HD_mul, FL_mul, OD, EZ_Det_t2, DT_Det_t2, FL_bool, HD_bool)
    return result


def update_pp_label2():
    result = pp_taiko22()
    pp_result_var2.set(f"{result:.5f}")



# test content
def update_label(event):
    selected_rework = rework_dropdown_t.get()

    # Check if a label already exists and remove it
    for widget in nested_panel_t.winfo_children():
        if isinstance(widget, ttk.Label):
            widget.destroy()

    # Add the new label based on the selected rework
    if selected_rework == "Mar 2025 - Now":
        ttk.Button(nested_panel_t, text="Calculate PP", command=update_pp_label).grid(row=0, column=0)
        ttk.Label(nested_panel_t, textvariable=pp_result_var).grid(row=2, column=0)
        ttk.Label(nested_panel_t, text="pp").grid(row=2, column=1)
    elif selected_rework == "Oct 2024 - Mar 2025":
        ttk.Label(nested_panel_t, text="Test 2").grid(row=4)
    elif selected_rework == "Sep 2022 - Oct 2024":
        ttk.Button(nested_panel_t, text="Calculate PP", command=update_pp_label2).grid(row=0, column=0)
        ttk.Label(nested_panel_t, textvariable=pp_result_var2).grid(row=2)
        ttk.Label(nested_panel_t, text="pp").grid(row=2,column=1)
    elif selected_rework == "Sep 2020 - Sep 2022":
        ttk.Label(nested_panel_t, text="Test 4").grid(row=4)
    elif selected_rework == "Mar 2014 - Sep 2020":
        ttk.Label(nested_panel_t, text="Test 5").grid(row=4)

# Bind the combobox to trigger this function when a selection is made
rework_dropdown_t.bind("<<ComboboxSelected>>", update_label)

# Taiko Graphs


ModeSelect.add(frame3, text='osu!Catch (The Beat)')
# --- Dropdown for Catch Reworks ---
CTB_reworks = [
    "Select a Rework",
    "Oct 2024 - Now",
    "May 2020 - Oct 2024", 
    "Mar 2014 - May 2020"
]

rework_label = ttk.Label(frame3, text="Select PP Rework:")
rework_label.pack(pady=(4, 0))

rework_dropdown_c = ttk.Combobox(
    frame3, 
    values=CTB_reworks, 
    state="readonly"
)
rework_dropdown_c.current(0)  # default to first rework
rework_dropdown_c.pack(pady=(0, 4))

star_frame = ttk.Frame(frame3)
star_frame.pack(pady=(10, 5))

ttk.Label(star_frame, text="Star Rating:").pack(side="left", padx=(0, 5))

star_var_c = tk.DoubleVar(value=5.0)
star_entry = ttk.Entry(star_frame, textvariable=star_var_c, width=10)
star_entry.pack(side="left")

extra_inputs_frame = ttk.Frame(frame3)
extra_inputs_frame.pack(pady=(10, 5))

# Miss Count
ttk.Label(extra_inputs_frame, text="Misses:").grid(row=0, column=0, padx=5)
miss_var_c = tk.IntVar(value=0)
ttk.Entry(extra_inputs_frame, textvariable=miss_var_c, width=6).grid(row=0, column=1)

# Accuracy
ttk.Label(extra_inputs_frame, text="Accuracy (%):").grid(row=0, column=2, padx=5)
acc_var_c = tk.DoubleVar(value=100.0)
ttk.Entry(extra_inputs_frame, textvariable=acc_var_c, width=6).grid(row=0, column=3)

ttk.Label(extra_inputs_frame, text="OD:").grid(row=0, column=4, padx=5)
OD_var_c = tk.DoubleVar(value=5)
ttk.Entry(extra_inputs_frame, textvariable=OD_var_c, width=6).grid(row=0, column=5)

ttk.Label(extra_inputs_frame, text="CS:").grid(row=1, column=0, padx=5, pady=5)
CS_var_c = tk.DoubleVar(value=5)
ttk.Entry(extra_inputs_frame, textvariable=CS_var_c, width=6).grid(row=1, column=1)

ttk.Label(extra_inputs_frame, text="HP:").grid(row=1, column=2, padx=5, pady=5)
HP_var_c = tk.DoubleVar(value=5)
ttk.Entry(extra_inputs_frame, textvariable=HP_var_c, width=6).grid(row=1, column=3)


ModeSelect.add(frame4, text='osu!Mania')
# --- Dropdown for Mania Reworks ---
Mania_reworks = [ 
    "Select a Rework",
    "Oct 2024 - Now", 
    "Oct 2022 - Oct 2024", 
    "May 2018 - Oct 2022", 
    "Mar 2014 - May 2018"
]

rework_label = ttk.Label(frame4, text="Select PP Rework:")
rework_label.pack(pady=(4, 0))

rework_dropdown_m = ttk.Combobox(
    frame4, 
    values=Mania_reworks, 
    state="readonly"
)
rework_dropdown_m.current(0)  # default to first rework
rework_dropdown_m.pack(pady=(0, 4))

star_frame = ttk.Frame(frame4)
star_frame.pack(pady=(10, 5))

ttk.Label(star_frame, text="Star Rating:").pack(side="left", padx=(0, 5))

star_var_m = tk.DoubleVar(value=5.0)
star_entry = ttk.Entry(star_frame, textvariable=star_var_m, width=10)
star_entry.pack(side="left")

right_mania_frame = ttk.Frame(frame4, width=500, height=1080)
right_mania_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)
right_mania_frame.pack_propagate(False)


extra_inputs_frame = ttk.Frame(frame4)
extra_inputs_frame.pack(pady=(10, 5))


ttk.Label(right_mania_frame, text="OD:").grid(row=1, column=0, padx=5, pady=5)
OD_var_m = tk.DoubleVar(value=5)
ttk.Entry(right_mania_frame, textvariable=OD_var_m, width=6).grid(row=1, column=1)

ttk.Label(right_mania_frame, text="CS:").grid(row=2, column=0, padx=5, pady=5)
CS_var_m = tk.DoubleVar(value=5)
ttk.Entry(right_mania_frame, textvariable=CS_var_m, width=6).grid(row=2, column=1)

ttk.Label(right_mania_frame, text="HP:").grid(row=3, column=0, padx=5, pady=5)
HP_var_m = tk.DoubleVar(value=5)
ttk.Entry(right_mania_frame, textvariable=HP_var_m, width=6).grid(row=3, column=1)

from Modes.Mania import Mania_Stats
Mania_Stats.Accuracy(right_mania_frame)
Mania_Stats.Accuracy2(right_mania_frame)

ttk.Separator(right_mania_frame, orient="vertical").grid(row=1, column=3, rowspan=20, sticky="ns", padx=[10,0])

def toggle_EZ_HR_m(var, button):
    current = var.get()
    if current == "Off":
        var.set("EZ_m")
        button.config(text="EZ", style="EZ.TButton")  # apply custom style if needed
    elif current == "EZ_m":
        var.set("HR_m")
        button.config(text="HR", style="HR.TButton")
    else:
        var.set("Off")
        button.config(text="Off", style="TButton")  # fallback/default style

def toggle_DT_HT_m(var, button):
    current = var.get()
    if current == "Off":
        var.set("DT_m")
        button.config(text="DT", style="DT.TButton")
    elif current == "DT_m":
        var.set("HT_m")
        button.config(text="HT", style="HD.TButton")
    else:
        var.set("Off")
        button.config(text="Off", style="TButton")



EZ_HR_var_m = tk.StringVar(value="False")
DT_HT_var_m = tk.StringVar(value="False")
HD_var_m = tk.BooleanVar(value=False)
FL_var_m = tk.BooleanVar(value=False)
NF_var_m = tk.BooleanVar(value=False)

# Mod toggle buttons
EZ_HR_m_btn = ttk.Button(
    right_mania_frame, text="Off", width=6,
    command=lambda: toggle_EZ_HR_m(EZ_HR_var_m, EZ_HR_m_btn)
)
EZ_HR_m_btn.grid(row=12, column=1)
ttk.Label(right_mania_frame, text="EZ/HR:").grid(row=12, column=0)

DT_HT_m_btn = ttk.Button(
    right_mania_frame, text="Off", width=6,
    command=lambda: toggle_DT_HT_m(DT_HT_var_m, DT_HT_m_btn)
)
DT_HT_m_btn.grid(row=15, column=1, pady=5)
ttk.Label(right_mania_frame, text="DT/HT:").grid(row=15, column=0, padx=8, pady=5)

HD_btn_m = ttk.Button(
    right_mania_frame, text="Off", width=6,
    command=lambda: toggle_mod(HD_var_m, HD_btn_m, "HD.TButton", "HD")
)
HD_btn_m.grid(row=13, column=1, pady=5)
ttk.Label(right_mania_frame, text="Hidden:").grid(row=13, column=0, padx=8)

FL_btn_m = ttk.Button(
    right_mania_frame, text="Off", width=6,
    command=lambda: toggle_mod(FL_var_m, FL_btn_m, "FL.TButton", "FL")
)
FL_btn_m.grid(row=14, column=1)
ttk.Label(right_mania_frame, text="Flashlight:").grid(row=14, column=0, padx=8)

NF_btn_m = ttk.Button(
    right_mania_frame, text="Off", width=6,
    command=lambda: toggle_mod(NF_var_m, NF_btn_m, "NF.TButton", "NF")   
)
NF_btn_m.grid(row=16, column=1)
ttk.Label(right_mania_frame, text="No Fail").grid(row=16,column=0,padx=8)


def update_label(event):
    selected_rework = rework_dropdown_m.get()

    # Check if a label already exists and remove it
    for widget in nested_panel_t.winfo_children():
        if isinstance(widget, ttk.Label):
            widget.destroy()

    # Add the new label based on the selected rework
    if selected_rework == "Oct 2022 - Oct 2024":
        ttk.Button(right_mania_frame, text="Calculate PP", command=update_pp_label_mania).grid(row=0,column=6,padx=[8,0])
        ttk.Label(right_mania_frame, textvariable=pp_result_var_m).grid(row=1,column=6)
        ttk.Label(right_mania_frame, text="PP").grid(row=1,column=7)


# -------------------- Different Game ---------------------
ModeSelect.add(frame5, text='ProSekai ft.初音ミク')
from Other_Games.ProSekai import PJSEKAI_math

Calc_Reworks = [
    "Select a Calculator",
    "Event Points Calculator",
    "Max Score Calculator"
]

# --- Wrapper frame for centering ---
dropdown_frame = ttk.Frame(frame5)
dropdown_frame.grid(row=0, column=0, pady=(4, 0), sticky="n")
# sticky="n" keeps it top-centered in column 0

# Label + Dropdown inside the centered wrapper
ttk.Label(dropdown_frame, text="Select a Calculator").pack()
calc_dropdown_sekai = ttk.Combobox(
    dropdown_frame,
    values=Calc_Reworks,
    state="readonly",
    width=21
)
calc_dropdown_sekai.pack()
calc_dropdown_sekai.current(0)

# --- Frames to switch between ---
Event_Frame = ttk.Frame(frame5, width=600, height=400)
Max_Calc_Frame = ttk.Frame(frame5, width=600, height=400)
PJSEKAI_math.GUI_Event(Event_Frame)
PJSEKAI_math.GUI_Max(Max_Calc_Frame)

# --- Frame switching logic ---
def show_selected_frame(event=None):
    Event_Frame.grid_remove()
    Max_Calc_Frame.grid_remove()

    selection = calc_dropdown_sekai.get()
    if selection == "Event Points Calculator":
        Event_Frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    elif selection == "Max Score Calculator":
        Max_Calc_Frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

calc_dropdown_sekai.bind("<<ComboboxSelected>>", show_selected_frame)

# Layout config
frame5.rowconfigure(1, weight=1)
frame5.columnconfigure(0, weight=1)

# ---------------------------


def add_creator_label(frame, text="Created by King Furret"):
    label = ttk.Label(frame, text=text)
    label2 = ttk.Label(frame, text="Build V1.0 (19/6/2025)")
    label.place(relx=0.0, rely=0.979, anchor='sw', y=-5)
    label2.place(relx=0.0, rely=1.0, anchor='sw', y=-5)

add_creator_label(frame1)
add_creator_label(frame2)
add_creator_label(frame3)
add_creator_label(frame4)
add_creator_label(frame5)


Window.mainloop()
