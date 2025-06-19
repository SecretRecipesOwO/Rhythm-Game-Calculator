import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# --- Image loading and cleaning ---
def clean_resized_image(path, size):
    img = Image.open(path).convert("RGBA")
    resized = img.resize(size, Image.Resampling.LANCZOS)
    background = Image.new("RGBA", size, (0, 0, 0, 0))  # fully transparent
    flattened = Image.alpha_composite(background, resized)
    return ImageTk.PhotoImage(flattened)

# --- Path setup ---
base_dir = os.path.dirname(__file__)  # e.g. .../modes/mania
img_path_1 = os.path.join(base_dir, "..", "..", "visuals", "grades", "ranking-X-small@2x.png")
img_path_2 = os.path.join(base_dir, "..", "..", "visuals", "grades", "ranking-S-small@2x.png")
img_path_3 = os.path.join(base_dir, "..", "..", "visuals", "grades", "ranking-A-small@2x.png")
img_path_4 = os.path.join(base_dir, "..", "..", "visuals", "grades", "ranking-B-small@2x.png")
img_path_5 = os.path.join(base_dir, "..", "..", "visuals", "grades", "ranking-C-small@2x.png")
img_path_6 = os.path.join(base_dir, "..", "..", "visuals", "grades", "ranking-D-small@2x.png")

img_tk_1 = clean_resized_image(img_path_1, (17, 20))
img_tk_2 = clean_resized_image(img_path_2, (17, 20))
img_tk_3 = clean_resized_image(img_path_3, (17, 20))
img_tk_4 = clean_resized_image(img_path_4, (17, 20))
img_tk_5 = clean_resized_image(img_path_5, (17, 20))
img_tk_6 = clean_resized_image(img_path_6, (17, 20))

# --- Shared data ---
shared_mania_vars = {}

# --- Accuracy entry UI ---
def Accuracy(right_mania_frame):
    shared_mania_vars["perfect"] = tk.DoubleVar(value=0)
    shared_mania_vars["great"]   = tk.DoubleVar(value=0)
    shared_mania_vars["good"]    = tk.DoubleVar(value=0)
    shared_mania_vars["ok"]      = tk.DoubleVar(value=0)
    shared_mania_vars["meh"]     = tk.DoubleVar(value=0)
    shared_mania_vars["miss"]    = tk.DoubleVar(value=0)

    total_var = tk.StringVar(value="0")

    def update_total(*args):
        try:
            total = sum(var.get() for var in shared_mania_vars.values())
            total_var.set(f"{total:.0f}")
        except tk.TclError:
            total_var.set("0")

    for var in shared_mania_vars.values():
        var.trace_add("write", update_total)

    ttk.Label(right_mania_frame, text="Perfects (320)").grid(row=3, column=4, padx=[10, 5], pady=5)
    ttk.Entry(right_mania_frame, textvariable=shared_mania_vars["perfect"], width=6).grid(row=3, column=5)

    ttk.Label(right_mania_frame, text="Greats (300)").grid(row=4, column=4, padx=[10, 5], pady=5)
    ttk.Entry(right_mania_frame, textvariable=shared_mania_vars["great"], width=6).grid(row=4, column=5)

    ttk.Label(right_mania_frame, text="Goods (200)").grid(row=5, column=4, padx=[10, 5], pady=5)
    ttk.Entry(right_mania_frame, textvariable=shared_mania_vars["good"], width=6).grid(row=5, column=5)

    ttk.Label(right_mania_frame, text="OKs (100)").grid(row=6, column=4, padx=[10, 5], pady=5)
    ttk.Entry(right_mania_frame, textvariable=shared_mania_vars["ok"], width=6).grid(row=6, column=5)

    ttk.Label(right_mania_frame, text="Mehs (50)").grid(row=7, column=4, padx=[10, 5], pady=5)
    ttk.Entry(right_mania_frame, textvariable=shared_mania_vars["meh"], width=6).grid(row=7, column=5)

    ttk.Label(right_mania_frame, text="Misses").grid(row=8, column=4, padx=[10, 5], pady=5)
    ttk.Entry(right_mania_frame, textvariable=shared_mania_vars["miss"], width=6).grid(row=8, column=5)

    ttk.Label(right_mania_frame, text="Total Combo:").grid(row=9, column=4, pady=10)
    ttk.Label(right_mania_frame, textvariable=total_var).grid(row=9, column=5)

# --- Accuracy + Image feedback ---
def Accuracy2(right_mania_frame):
    acc1_var = tk.StringVar(value="0.00%")
    acc2_var = tk.StringVar(value="0.00%")

    shared_mania_vars["acc1_var"] = acc1_var
    shared_mania_vars["acc2_var"] = acc2_var

    ttk.Label(right_mania_frame, text="Calculation Accuracy:").grid(row=10, column=4, pady=[0, 2])
    ttk.Label(right_mania_frame, textvariable=acc1_var).grid(row=10, column=5)
    ttk.Label(right_mania_frame, text="In Game Accuracy:").grid(row=11, column=4, pady=[2, 0])
    ttk.Label(right_mania_frame, textvariable=acc2_var).grid(row=11, column=5, padx=[0, 5])

    img_label = tk.Label(right_mania_frame, borderwidth=0, highlightthickness=0)
    img_label.grid(row=11, column=6)

    def update_accuracy(*args):
        try:
            p = shared_mania_vars["perfect"].get()
            g1 = shared_mania_vars["great"].get()
            g2 = shared_mania_vars["good"].get()
            o = shared_mania_vars["ok"].get()
            m1 = shared_mania_vars["meh"].get()
            m2 = shared_mania_vars["miss"].get()
            t = p + g1 + g2 + o + m1 + m2

            if t == 0:
                acc1 = 0.0
                acc2 = 0.0
            else:
                acc1 = ((320 * p) + (300 * g1) + (200 * g2) + (100 * o) + (50 * m1)) / (320 * t)
                acc2 = (300 * (p + g1) + 200 * g2 + 100 * o + 50 * m1) / (300 * t)

            acc1_var.set(f"{acc1 * 100:.2f}%")
            acc2_var.set(f"{acc2 * 100:.2f}%")
        except tk.TclError:
            acc1_var.set("Err")
            acc2_var.set("Err")

    def update_image(*args):
        try:
            acc = float(acc2_var.get().strip('%'))
            p = shared_mania_vars["perfect"].get() + shared_mania_vars["great"].get()
            t = sum(var.get() for var in shared_mania_vars.values() if isinstance(var.get(), (int, float)))

            if t == p and acc == 100:
                img_label.config(image=img_tk_1)
                img_label.image = img_tk_1
            elif acc >= 95 and t > p:
                img_label.config(image=img_tk_2)
                img_label.image = img_tk_2
            elif acc >= 90 and acc < 95 and t > p:
                img_label.config(image=img_tk_3)
                img_label.image = img_tk_3
            elif acc >= 80 and acc < 90 and t > p:
                img_label.config(image=img_tk_4)
                img_label.image = img_tk_4
            elif acc >= 70 and acc < 80 and t > p:
                img_label.config(image=img_tk_5)
                img_label.image = img_tk_5
            elif acc < 70 and t > p:
                img_label.config(image=img_tk_6)
                img_label.image = img_tk_6
        except ValueError:
            img_label.config(image='')
            img_label.image = None


    for var in shared_mania_vars.values():
        var.trace_add("write", update_accuracy)

    # Now also trace acc2_var directly for image update
    acc2_var.trace_add("write", update_image)

    update_accuracy()
    update_image()