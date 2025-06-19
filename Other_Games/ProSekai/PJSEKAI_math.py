import tkinter as tk
from tkinter import ttk

Song_List = ['Tell Your World', 'Next Nest', 'Hand in Hand', '39 Music!', 'Greenlights Serenade', 'Melt', 'World is Mine', 'Hatsune Miku no Shoushitsu', 'Blessing', 'Bless Your Breath', 'Gimme×Gimme', 'Junky Night Town Orchestra', 'Leia - Remind', 'on the rocks', 'Jangsanbeom', 'Alone', 'Gakgaejeontu','Beotkkotbi']
Difficulty_List = {
    'Tell Your World': [5,10,16,22,26,'Append 25'],
    'Next Nest': [6,13,18,27,30],
    'Hand in Hand': [6,13,16,23,28,'Append 28'],
    '39 Music!': [6,11,16,23,28],
    'Greenlights Serenade': [9,14,19,27,31],
    'Melt': [7,12,17,25,29],
    'World is Mine': [7,13,17,24,29],
    'Hatsune Miku no Shoushitsu': [9,15,22,30,35],
    'Blessing': [5,11,16,23,27],
    'Bless Your Breath': [7,13,17,24,29],
    'Gimme×Gimme': [6,11,18,26,29],
    'Junky Night Town Orchestra': [6,13,18,26,31],
    'Leia - Remind': [9,13,18,25,29]
}

def GUI_Event(frame):
    ttk.Label(frame,text="Talent Score:").grid(row=1,column=0, padx=5,pady=5)
    frame.Talent = tk.DoubleVar(value=10000)
    ttk.Entry(frame, textvariable=frame.Talent, width=8).grid(row=1,column=1)

    ttk.Separator(frame, orient='horizontal').grid(row=2,column=0,columnspan=6,sticky='ew',pady=[5,2])

    ttk.Label(frame, text="Song:").grid(row=3, column=0, padx=5, pady=5)
    frame.SongVar = tk.StringVar()
    Dropdown = ttk.Combobox(frame, textvariable=frame.SongVar, values=Song_List, state="readonly", width=26)
    Dropdown.grid(row=4, column=0, padx=5, pady=5)

    ttk.Label(frame, text="Difficulty:").grid(row=3, column=1, padx=5, pady=5)
    frame.DiffVar = tk.StringVar()  
    frame.DiffDropdown = ttk.Combobox(frame, textvariable=frame.DiffVar, state="readonly", width=8)
    frame.DiffDropdown.grid(row=4, column=1, padx=5, pady=5)

    multiplier_val = tk.StringVar(value="23x")
    Total_Multi = tk.StringVar(value="37.95x")

    def update_difficulty(event):
        selected_song = frame.SongVar.get()
        difficulties = Difficulty_List.get(selected_song, [])
        frame.DiffDropdown['values'] = difficulties
        if difficulties:
            frame.DiffDropdown.current(0)
        else:
            frame.DiffDropdown.set('')

    Dropdown.bind("<<ComboboxSelected>>", update_difficulty)

    ttk.Separator(frame, orient='horizontal').grid(row=5,column=0,columnspan=6,sticky='ew',pady=5)

    # Bonus Percent smart placeholder
    ttk.Label(frame,text="Team Bonus Percent (%):").grid(row=6,column=0, padx=5,pady=5)
    frame.BonusP = tk.StringVar(value="65")
    user_edited_bonus = tk.BooleanVar(value=False)

    def validate_bonus_input(new_value):
        if new_value == "":
            return True
        try:
            float(new_value)
            return True
        except ValueError:
            return False

    def on_focus_in_bonus(event):
        if frame.BonusP.get() == "0" and not user_edited_bonus.get():
            event.widget.delete(0, tk.END)

    def on_focus_out_bonus(event):
        if not frame.BonusP.get().strip():
            frame.BonusP.set("0")
            user_edited_bonus.set(False)

    def on_user_typing_bonus(event):
        user_edited_bonus.set(True)

    vcmd_bonus = (frame.register(validate_bonus_input), "%P")
    bonus_entry = ttk.Entry(frame, textvariable=frame.BonusP, width=8, validate="key", validatecommand=vcmd_bonus)
    bonus_entry.grid(row=6,column=1)
    bonus_entry.bind("<FocusIn>", on_focus_in_bonus)
    bonus_entry.bind("<FocusOut>", on_focus_out_bonus)
    bonus_entry.bind("<Key>", on_user_typing_bonus)

    # Current Event Points with smart placeholder
    ttk.Label(frame,text="Current Event Points:").grid(row=7,column=0, padx=5,pady=5)
    frame.EventP1 = tk.StringVar(value="0")
    user_edited_event_points = tk.BooleanVar(value=False)

    def validate_event_points(new_value):
        if new_value == "":
            return True
        try:
            float(new_value)
            return True
        except ValueError:
            return False

    def on_focus_in_event_points(event):
        if frame.EventP1.get() == "0" and not user_edited_event_points.get():
            event.widget.delete(0, tk.END)

    def on_focus_out_event_points(event):
        if not frame.EventP1.get().strip():
            frame.EventP1.set("0")
            user_edited_event_points.set(False)

    def on_user_typing_event_points(event):
        user_edited_event_points.set(True)

    vcmd_event = (frame.register(validate_event_points), "%P")
    event_points_entry = ttk.Entry(frame, textvariable=frame.EventP1, width=8, validate="key", validatecommand=vcmd_event)
    event_points_entry.grid(row=7,column=1)
    event_points_entry.bind("<FocusIn>", on_focus_in_event_points)
    event_points_entry.bind("<FocusOut>", on_focus_out_event_points)
    event_points_entry.bind("<Key>", on_user_typing_event_points)

    # Desired Event Points (simple entry)
    ttk.Label(frame,text="Desired Event Points:").grid(row=8,column=0, padx=5,pady=5)
    frame.EventP2 = tk.DoubleVar(value=100000)
    ttk.Entry(frame, textvariable=frame.EventP2, width=8).grid(row=8,column=1)

    frame.EventP3 = tk.DoubleVar(value=100000)

    def update_difference(*args):
        try:
            p1 = float(frame.EventP1.get())
        except ValueError:
            p1 = 0
        try:
            p2 = frame.EventP2.get()
        except tk.TclError:
            p2 = 0
        frame.EventP3.set(int(p2 - p1))

    frame.EventP1.trace_add("write", update_difference)
    frame.EventP2.trace_add("write", update_difference)

    ttk.Label(frame, text="Remaining Points:").grid(row=9, column=0, padx=5, pady=5)
    ttk.Label(frame, textvariable=frame.EventP3).grid(row=9, column=1)

    # Energy slider & multiplier display
    energy_val = tk.IntVar(value=5)
    ttk.Label(frame, text="Energy:").grid(row=0, column=0, padx=5, pady=5)
    ttk.Scale(frame, from_=0, to=10, orient='horizontal',
             command=lambda val: update_multiplier(int(round(float(val)))), value=5
            ).grid(row=0, column=1)
    ttk.Label(frame, textvariable=energy_val, width=5).grid(row=0, column=2, padx=5)

    def update_multiplier(val):
        val = int(round(float(val)))
        energy_val.set(val)
        result = (
            0.004662 * val**4
            - 0.0990676 * val**3
            + 0.469697 * val**2
            + 3.96037 * val
            + 0.902098
        )
        multiplier_val.set(f"{round(result)}x")
        update_total_multiplier()

    def update_total_multiplier(*args):
        try:
            raw_multiplier = float(multiplier_val.get().replace("x", ""))
            bonus = float(frame.BonusP.get()) / 100
            result = raw_multiplier * (1 + bonus)
            Total_Multi.set(f"{result:.2f}x")
        except Exception:
            Total_Multi.set("??x")

    # Trace BonusP changes to update total multiplier
    frame.BonusP.trace_add("write", update_total_multiplier)
    multiplier_val.trace_add("write", update_total_multiplier)

    ttk.Label(frame, text="Energy Points Multiplier:").grid(row=10, column=0,pady=[0,5])
    ttk.Label(frame, textvariable=multiplier_val).grid(row=10, column=1)

    ttk.Label(frame, text="Total Multiplier:").grid(row=11,column=0)
    ttk.Label(frame, textvariable=Total_Multi).grid(row=11,column=1)
    

def GUI_Max(frame):
    ttk.Label(frame,text="Test2").grid(row=1,column=0)

