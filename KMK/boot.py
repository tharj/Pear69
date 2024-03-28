import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP20,
    source=board.GP1,
    nkro = False,
    usb_id=('Karjula', 'Pear69'),
    storage = True,
)