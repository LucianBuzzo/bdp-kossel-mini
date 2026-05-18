## Research for sintron kossel 2020 delta printer

Instruction PDF: 
https://www.robotdigg.com/upload/pdf/2a823cc8a8dcff9da99cce92710cc745.pdf?fbclid=IwdGRleAQrs41leHRuA2FlbQIxMQBzcnRjBmFwcF9pZAo2NjI4NTY4Mzc5AAEeyqaOx1LogWIayOW0oUYV_VILu1vvB6Acsutw1AKCeKG5gGuFozUbRTVZH4Q_aem_xH_YQ8n3ndAM4vQvxPs-Cw

Note that carriage riders don't match the assembly instructions.


Is it an ebay kit?
https://reprap.org/forum/read.php?178,540379,545012,quote=1

This kit - https://sintron-hk.com/products/sintron-kossel-mini-plastic-printed-parts-full-kit-for-mk8-extuder-reprap-rostock-delta-3d-printer-pla-red?srsltid=AfmBOopnsKctdFDb7zQvba5C0OjBmHsSj9J4RFeGflgKltViRqwsQQrE&utm_source=chatgpt.com

## Key dimensions
- 200mm diameter print area
- 220mm height
- 230mm diagonal
- 220mm diameter build plate
- 2020 extrusion
- 40mm cap between connecting rod arms
- 240mm horizontal extrusions

## Flying extruder & remote cooling

https://www.youtube.com/watch?v=3-xiBsnWhsM

> 
@jamespray
4 years ago (edited)
 @tinchodias  I have not put out much about my current setup, but you are correct.  I use a .16A fan powering one compressor for the heatsink (which doesn't need high-powered cooling) and a .3A compressor with a .16A axial fan as an intake booster to get lots of airflow for the layer cooling.  The wiring goes to the same places on the board as the stock fans.  I just had to make up my own wiring extensions (with a split to power the two layer cooling fans in parallel).  The compressors sit on shelves in a scratchbuilt tower enclosure alongside my printer (you can see this in the background of the latest video on my channel, https://www.youtube.com/watch?v=3j8eR_cYwak, around the 0:16 mark).  You don't have to build my compressors to make it work, though -- back in this video, I was using cheap .25A blowers stacked inlet-to-outlet (for two per hose) and they actually performed quite well.  The noise was just awful, and I mean AWFUL.  Well, and they blew one of the fan MOSFETS on my board, and one of them melted!  So be sure you stay within the amperage your fan drivers can handle.

## TODO:

### Printable parts

- [ ] Cracked top mounting plate - print replacement from MKVS or similar
    - [ ] top plate x3
    - [ ] endstop mounts x3
    - [ ] Towers to use double shear

- [ ] Linear rails for carriages
    - [ ] Linear rail mounts
    - [ ] carriages x3
        - https://www.thingiverse.com/thing:2206030

- [ ] Effector rebuild
    - Settle on new size
    - https://www.thingiverse.com/thing:4329200
    - https://github.com/chirpy2605/voron/blob/main/general/CraneFly/README.md
    - chube compact

- [ ] PSU mount

- [ ] Pico mount

- [ ] Extruder, sherpa heavy with pancake nema 17
    - https://www.printables.com/model/549890-sherpa-extra-heavy-with-nema17-update-2

- [ ] Remote cooling
    - thingiverse.com/thing:6329080

### Order of operations

- [ ] Print off replacement corners and top plates
- [ ] Rebuild frame with linear rails and new 2020 corners
    - Remix https://www.thingiverse.com/thing:4571307
- [ ] Rebuild PSU mount and wire in PSU
- [ ] Install Pico and install stepper motors
- [ ] Install and wire motors, endstops, and fans
    - Wireless endstop detection?
- [ ] Flash pico with klipper and test motors
- [ ] Wire in heatbed
- [ ] Rebuild effector with new design
- [ ] Wire in effector fans, hotend and bltouch



## Links
- General info on kossel mini http://blog.think3dprint3d.com/2014/06/kossel-mini-and-more.html
- MKVS remix https://github.com/Verohomie/MKVS
- SKR E3-DIP V1.1 pinout https://github.com/bigtreetech/BIGTREETECH-SKR-E3-DIP-V1.0/blob/master/Hardware/SKR%20E3-DIP-V1.1-PIN.pdf