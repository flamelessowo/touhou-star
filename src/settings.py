
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../assets/settings")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    360.0,
    image=image_image_1
)

canvas.create_text(
    519.0,
    518.0,
    anchor="nw",
    text="Focus",
    fill="#000000",
    font=("Milonga Regular", 36 * -1)
)

canvas.create_text(
    468.0,
    91.0,
    anchor="nw",
    text="Key Remapping owo",
    fill="#000000",
    font=("Milonga Regular", 36 * -1)
)

canvas.create_text(
    464.0,
    30.0,
    anchor="nw",
    text="Its a settings, man!!",
    fill="#BA2E2E",
    font=("Milonga Regular", 36 * -1)
)

canvas.create_text(
    519.0,
    152.0,
    anchor="nw",
    text="Up",
    fill="#000000",
    font=("Milonga Regular", 36 * -1)
)

canvas.create_text(
    519.0,
    335.0,
    anchor="nw",
    text="Down",
    fill="#000000",
    font=("Milonga Regular", 36 * -1)
)

canvas.create_text(
    519.0,
    213.0,
    anchor="nw",
    text="Left",
    fill="#000000",
    font=("Milonga Regular", 36 * -1)
)

canvas.create_text(
    519.0,
    274.0,
    anchor="nw",
    text="Right",
    fill="#000000",
    font=("Milonga Regular", 36 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    606.0,
    170.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#CF2929",
    highlightthickness=0
)
entry_1.place(
    x=587.0,
    y=152.0,
    width=38.0,
    height=34.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    611.0,
    231.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#BA2E2E",
    highlightthickness=0
)
entry_2.place(
    x=597.0,
    y=213.0,
    width=28.0,
    height=34.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    641.0,
    292.0,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#BA2E2E",
    highlightthickness=0
)
entry_3.place(
    x=625.0,
    y=274.0,
    width=32.0,
    height=34.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    652.0,
    358.0,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#BA2E2E",
    highlightthickness=0
)
entry_4.place(
    x=640.0,
    y=340.0,
    width=24.0,
    height=34.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    652.5,
    417.0,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#BA2E2E",
    highlightthickness=0
)
entry_5.place(
    x=638.0,
    y=399.0,
    width=29.0,
    height=34.0
)

canvas.create_text(
    519.0,
    396.0,
    anchor="nw",
    text="Bomb",
    fill="#000000",
    font=("Milonga Regular", 36 * -1)
)

canvas.create_text(
    519.0,
    457.0,
    anchor="nw",
    text="Shoot",
    fill="#000000",
    font=("Milonga Regular", 36 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    652.5,
    480.0,
    image=entry_image_6
)
entry_6 = Text(
    bd=0,
    bg="#BA2E2E",
    highlightthickness=0
)
entry_6.place(
    x=640.0,
    y=462.0,
    width=25.0,
    height=34.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    664.0,
    536.0,
    image=entry_image_7
)
entry_7 = Text(
    bd=0,
    bg="#BA2E2E",
    highlightthickness=0
)
entry_7.place(
    x=624.0,
    y=518.0,
    width=80.0,
    height=34.0
)

canvas.create_text(
    468.0,
    579.0,
    anchor="nw",
    text="Music volume",
    fill="#000000",
    font=("Milonga Regular", 36 * -1)
)

canvas.create_text(
    460.0,
    640.0,
    anchor="nw",
    text="Sound volume",
    fill="#000000",
    font=("Milonga Regular", 36 * -1)
)

canvas.create_text(
    740.0,
    584.0,
    anchor="nw",
    text="100",
    fill="#BA2E2E",
    font=("Milonga Regular", 36 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=815.0,
    y=602.0,
    width=27.0,
    height=0.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=815.0,
    y=663.0,
    width=27.0,
    height=0.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=703.0,
    y=602.0,
    width=27.0,
    height=0.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=705.0,
    y=663.0,
    width=27.0,
    height=0.0
)

canvas.create_text(
    740.0,
    645.0,
    anchor="nw",
    text="100",
    fill="#BA2E2E",
    font=("Milonga Regular", 36 * -1)
)
window.resizable(False, False)
window.mainloop()
