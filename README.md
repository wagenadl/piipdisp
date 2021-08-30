# Introduction

PiIPDisp is a tiny little program that allows a Raspberry Pi computer
to advertise its IP address on an SSD1306 display. This is mainly
useful for headless applications in DHCP environments where the user
does not have control over the router.

SSD1306-based displays can be obtained from many sources, and 128x32
pixel modules are available for only a few dollars a piece (Summer
2021).

# Connection

To connect the SSD1306 display to the Pi, it is useful to know that the
first few GPIO pins of the Pi are as follows:

    3.3V   5V
    GP2    5V
    GP3    Gnd
    ...    ...

The top in this list corresponds to the pins farthest away from the
USB connectors, i.e., closest to the corner of the Pi.

My SSD1306 breakout board has only 4 pins. They get connected as
follows:

    Vcc <-> 3.3V
    Gnd <-> Gnd
    SDA <-> GP2
    SCL <-> GP3

# Dependencies

You will need to install PIL and RPi.GPIO. On Ubuntu, the easiest way
to do that is:

    sudo apt install python3-pil
    sudo apt install python3-rpi.gpio

Using "pip" is also an option.

PiIPDisp also uses the Adafruit SSD1306 library, but that library is
included with PiIPDisp, for convenience.

# Running the software

There is no need to "install" the software: You can either run the
"ipdisp.py" script in place, or copy it to some convenient
location. In that case, you must make sure that python can "find" the
adafruit_ssd1306.py module. This is most easily done by copying it
along.

You may have to make it executable by running

    chmod a+x piipdisp.py

or some such.

This program is obviously most useful if it is started
automatically. If you configure your Raspberry Pi to log you in
without a password, you can use Gnome's "Startup Applications" to do
this. Otherwise, you may have to place a wrapper in
/etc/systemd/system. An example wrapper is provided as
piipdisp.service. This assumes that you have copied piipdisp.py as
well as adafruit_ssd1306.py to /usr/local/bin. After copying the
wrapper to /etc/systemd/system (or creating a soft link there), you
still have to run

    systemctl enable piipdisp

to run piipdisp at startup time.
