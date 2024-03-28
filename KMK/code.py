print("Starting")

import board
# import digitalio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys



keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]


keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

# keyboard.pull = digitalio.Pull.DOWN
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.col_pins = (
    board.GP20,
    board.GP22,
    board.GP26,
    board.GP27,
    board.GP28,
    board.GP29,
    board.GP0,
)
keyboard.row_pins = (
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

encoder_handler.pins = ((board.GP15, board.GP14, None, False),)

keyboard.coord_mapping = (
    0,  1,  2,  3,  4,  5,  6,  41, 40, 39, 38, 37, 36, 35,
    7,  8,  9,  10, 11, 12, 13, 48, 47, 46, 45, 44, 43, 42,
    14, 15, 16, 17, 18, 19, 20, 55, 54, 53, 52, 51, 50, 49,
    21, 29, 22, 23, 24, 25, 26, 27, 62, 61, 60, 59, 58, 57, 56,
    28, 30, 31,     32, 33, 34,     68, 67, 66,     65, 64, 63
)


keyboard.keymap = [

    #Layer 1
    [
    KC.ESC,    KC.N1,  KC.N2,  KC.N3,  KC.N4,  KC.N5,  KC.N6,  KC.N7,  KC.N8,  KC.N9,  KC.N0,  KC.MINS,  KC.EQL,  KC.BSPC,
    KC.TAB,    KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,   KC.LBRC,  KC.RBRC, KC.BSLS,
    KC.MO(1),   KC.A,   KC.S,   KC.D,   KC.F,   KC.G,   KC.H,   KC.J,   KC.K,   KC.L,   KC.SCLN, KC.QUOT, KC.ENT,  KC.MUTE,
    KC.LSFT,   KC.NO,  KC.Z,   KC.X,   KC.C,   KC.V,   KC.B,   KC.N,   KC.M,   KC.COMM, KC.DOT, KC.SLSH, KC.LSFT, KC.UP,   KC.DEL,
    KC.LCTL,  KC.LGUI, KC.LALT,        KC.SPC, KC.ENT, KC.BSPC,        KC.RALT, KC.RGUI, KC.RCTL, KC.LEFT, KC.DOWN, KC.RIGHT
    ],

    #Layer 2
    [
    KC.GRV,    KC.F1,  KC.F2,  KC.F3,  KC.F4,  KC.F5,  KC.F6,  KC.F7,  KC.F8,  KC.F9,  KC.F10, KC.NO,    KC.NO,   KC.NO,
    KC.TAB,    KC.H,   KC.W,   KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,   KC.LBRC,  KC.RBRC, KC.BSLS,
    KC.NO,   KC.A,   KC.S,   KC.D,   KC.F,   KC.G,   KC.H,   KC.J,   KC.K,   KC.L,   KC.SCLN, KC.QUOT, KC.ENT,  KC.MUTE,
    KC.LSFT,   KC.NO,  KC.Z,   KC.X,   KC.C,   KC.V,   KC.B,   KC.N,   KC.M,   KC.COMM, KC.DOT, KC.SLSH, KC.LSFT, KC.UP,   KC.DEL,
    KC.LCTL,  KC.LGUI, KC.LALT,        KC.SPC, KC.ENT, KC.BSPC,        KC.RALT, KC.RGUI, KC.RCTL, KC.LEFT, KC.DOWN, KC.RIGHT
    ]

]

encoder_handler.map = [
    [(KC.VOLD, KC.VOLU),] # Layer 1
]

if __name__ == "__main__":
    keyboard.go()