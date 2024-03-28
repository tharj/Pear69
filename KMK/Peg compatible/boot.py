import board

from kmk.bootcfg import bootcfg

bootcfg(
    # col and row pins for matrix position (0,0) i.e. ESC, press while pluggin in
    # to disable boot config to show the circuitpy drive
    sense=board.GP20, # COL
    source=board.GP1, # ROW, DiodeOrientation is COL2ROW
    midi=False,
    mouse=True,
    storage=False,
)