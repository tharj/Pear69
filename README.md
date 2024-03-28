An open source 65-ish% keyboard running on KMK firmware designed mainly with KiCad.

I had previously made a couple of keyboards, first an ergo and later a 65% board with a proprietary space split. For myself, I mainly wanted to change from ZMK to KMK firmware for, in my opinion, easier modifications on the keymaps and functionality. At the same time I also wanted to include the possibility for different layouts, in case I end up building this for someone that doesn't want ANSI or split space.

!(https://github.com/tharj/Pear69/blob/main/img/1.png)

## Basics

Default layout for me is ANSI with split space. It's not quite the normal 65% layout, as the top right corner will house the microcontroller running the keyboard. Keyboard layout editor(KLE) (http://www.keyboard-layout-editor.com/) Makes configuring the layout very easy, the extra keys for additional layouts are configured as well, for later use when we get to the actual PCB design. KLE lets you download the layout as a .json-file, that will be used in KiCad to make the actual switch positioning a breeze.

I configured the PCB for the Helios, which is a RP2040 based controller form 0xCB (https://github.com/0xCB-dev/0xCB-Helios). I also designed a way over engineered case for 3D-printing that I used for the first board I put together. 

There is support for one encoder on the right hand side, and also breakouts for an OLED (just under the controller, to cover the controller), and also breakouts for the extra pins that were not used in the key matrix, with 5v, 3.3v and ground. 

## KiCad

For starters, KiCad is going to need a couple of things to make the design process a bit smoother:
- A library containing most of the symbols(for schematic) and footprints(for PCB) (https://github.com/ebastler/marbastlib)
- And a plugin to use the .json generated by KLE earlier (https://github.com/zykrah/kicad-kle-placer)

Design started with the schematic and figuring out the shape of the key matrix. Modern mechanical keyboard works by scanning a matrix of columns and rows, with diodes to prevent ghosting when used. There are a couple of different ways to configure the switches and diodes, I used diode direction "from column to row" here.

I won't go into detail on the basic function of the matrix scanning, as it's been covered multiple times in different places. Take a look at https://docs.qmk.fm/#/how_a_matrix_works?id=how-a-keyboard-matrix-works if you want to understand the whole process in more depth. In very basic level, pressing a key connects column and row pins on the controller. 

I ended up with a matrix of 7 columns and 10 rows, which allows for up to 70 keys, this leaves quite a few spare pins on the controller for an encoder and OLED and such.  Physical layout of course is not 7x10, so the PCB will end up with some tricky routing of traces.

Using a MX switch and a diode from the marbastlib we imported earlier, I created the 7x10 grid and ended up cutting it in half, to resemble the actual physical layout. With some tweaks to the grid due to the multiple layouts I ended up with a ready schematic for the key switches: 
![[Pasted image 20240327194027.png]]


From here you can assign a footprint of your choosing, I used a simple MX solder footprint. I tried to go with a hot swap socket at first, but the ANSI/ISO hybrid layout around the enter region got a bit too crowded and I downgraded to solder mount switches. 

After selecting the footprints for the switches and diodes (SOD123, small SMD diode in this case), while in the PCB view, you can update the PCB from the schematic and get all your switches and diodes in to the PCB. 

### KLE placer plugin 

First, it's a good idea to check that the switch and diode footprints are on the right side of the PCB, i.e. in the right layer, in this case the back layer. Select all and flip to the appropriate side if needed. 

For the KLE placer plugin, the best way for me was to look for the switch and diode with index 0, and lay them out as you like, then the KLE plugin will not only put the switch footprints in the right locations, but also can move all the corresponding diodes according to the index 0 example you've given. KLE placer can also locate stabilizers where needed, but I ended up adding them by hand later, because of the split space needing multiple different stabilizer positions. 

When you run the KLE placer plugin, it places the switches exactly as shown in the KLE UI, so the additional layout keys have to be dragged to their place. This step requires some back and forth between the schematic and PCB, I ended up sharing some diodes between different keys in different layouts (and of course deleting the now extra diodes). Some switch orientations needed to be turned 90 to 180 degrees, to accommodate the different layout footprints. 

### Controller and routing

First I routed the traces for the rows and columns, mostly using one side of the PCB for rows and the other side for column traces, those got routed near the top right of the PCB, where the controller will be seated. Some layer changes needed to be made and the routing got a bit crowded in certain areas, mainly due to the difference in electrical matrix and physical layout of the keys.

I went with the Helios, which is a RP2040 based c-usb controller, footprint for it was also in the marbastlib library. After adding it to the schematic and to the PCB, I added tags for all the rows and columns, and started to figure out suitable pins on the controller. Having things actually connected in the schematic, will enable nets in the PCB, showing where everything needs to connect and further making it possible to check the validity of all connections with DCR (Design rules checker). It is much easier to sanity check your connections in the schematic vs in the PCB, having an error pop up if you are missing a connection or there is some other violation, is very nice. 

![[Pasted image 20240327201259.png]]
As I had some spare pins, I added a OLED breakout below the controller and also an encoder(volume knob) on the right. Rest of the pins got broken out in the arrow cluster in the bottom right, just in case. 

I added the necessary stabilizers for the longer keys that use them, along with some mounting holes, allowing a tray mounting the PCB.

I also wanted a 'switch plate' for the keyboard, and simply took a copy of the KiCad project, deleted the unnecessary components and changed the switch footprints out to switch cut-outs from the marbastlib. Switch plate is just a PCB with no electrical function, to enable different mounting options. 

Using KiCads Fabrication outputs, I exported the necessary gerber files and drill files, that the PCB manufacturer requires. I used JLCPCB and at least they have a guide for settings when exporting gerber files for manufacturing.

## Case and assembly

While I was waiting on the PCBs to be manufactured, I grabbed the plates from KiCad to Solidworks and started to design a case around them. I wanted something quick and dirty so I could build one board when the PCBs arrive. Nothing special in the case design, just top and bottom parts cut in half to get them to a printable size. 

![[Pasted image 20240327203137.png]]

When I actually got to printing, it took a few tries to get everything to line up with the PCBs. As a first time ABS printer I quickly learned that it likes to shrink while cooling. Scaling everything up by 0.7% was the final adjustment that made everything fit perfectly.

After the PCBs arrived, I soldered up a first prototype with some nice linear Alpaca switches I had lying around so I could get to tinkering around the firmware. There is plenty of videos going over actually building a custom keyboard, so I won't get into it here. 

## Setting up KMK

The basic process for a custom board is quite straight forward. Find the proper release of CircuitPython for your board from https://circuitpython.org/downloads and flash the controller with the .UF2 by drag and drop to the drive according to the instructions(you have to be in the bootloader mode for the controller to accept UF2 files). 

After flashing the controller with the CircuitPython, installing KMK is really simple. They have good documentation for the first steps in http://kmkfw.io/docs/Getting_Started. I got KMK running very quickly with the instructions they provided. 

I thought it would be easier to understand what is going on by first making a version with hand configured keymaps etc. and ended up with a single code.py containing all info about the controller pins, diode orientation and coordinate mapping (which does the same thing as matrix transformation in ZMK) and also the encoder handling with keymaps for the whole matrix.

After few hours of tinkering I had a working config for the board with two layers containing most of the functionality I was after at this point. 

### Peg

I also wanted to use the GUI built for KMK (https://peg.software/) and that required some modifications to the configs. After looking around in the Peg repo, it looked like the default structure was a kb.py for creating a python object containing the hardware config like pins and coordinate mapping and a main.py for keymaps, different modules(addons) like media keys. Peg also requires a layout.json, firstly for some configuration on what is found on the keyboard, device name and enabling or disabling certain features. The layout.json also contains the coordinates and sizes of keys for the graphical interface that is used with Peg. On top of those, I also have a boot.py for hiding the storage device when connecting among other things.

There is some issues with compatibility when using latest stock KMK on CircuitPython and Peg together. These would be solved by using a custom firmware on the controller from boardsource called boardsource-python. It is only available for a handful of controllers at the moment, and the Helios is not among them, at least yet. Building bs-python for a new controller is a bit out of my comfort zone for now.

The problem with the current setup is that when the layout in Peg includes a momentary layer change (MO(#)), Peg includes imports to modules that are not found in the current KMK repo, but have been moved to another module with different name. I worked around this by grabbing the "missing" modtap.py from an old fork of KMK and while it's not a elegant solution, it works for now. The real fix would be to port bs-python for the particular controller, it seems to include the same version of KMK that Peg is configured with.

![[Pasted image 20240327212501.png]] 

## TBD

I still have the OLED to install and configure. There also were some oversights in the first version of the PCBs that I ordered, that have since been fixed. I only had one of the Helios controllers and it is out of stock in EU right now, so depending when they restock, I might end up changing it out to something with Bluetooth. 
