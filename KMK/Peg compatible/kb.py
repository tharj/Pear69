import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.encoder import RotaryioEncoder
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        self.matrix = [MatrixScanner(
            column_pins=self.col_pins,
            row_pins=self.row_pins,
        ),
        RotaryioEncoder(
            pin_a=board.GP15,
            pin_b=board.GP14,
            divisor=4,
        )]

    row_pins = (
        board.GP1,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7,
        board.GP10,
        board.GP13,
        board.GP16,
        board.GP23,
        board.GP21,
    )
    col_pins = (
        board.GP20,
        board.GP22,
        board.GP26,
        board.GP27,
        board.GP28,
        board.GP29,
        board.GP0,
    )

    diode_orientation = DiodeOrientation.COL2ROW

    # sw29 missing from ANSI layout
    # sw67 missing due to 1.5u RALT and RCTRL
    coord_mapping = [ 
        0,  1,  2,  3,  4,  5,  6,  41, 40, 39, 38, 37, 36, 35,
        7,  8,  9,  10, 11, 12, 13, 48, 47, 46, 45, 44, 43, 42,
        14, 15, 16, 17, 18, 19, 20, 55, 54, 53, 52, 51, 50, 49,
        21, 22, 23, 24, 25, 26, 27, 62, 61, 60, 59, 58, 57, 56,
        28, 30, 31,     32, 33, 34,     68, 66,     65, 64, 63,
        70, 71
    ]