# pyPM5
A python package for interfacing with the Virginia Diodes PM5 terahertz powermeter. This works via the PM5() object which communicates to the powermeter with pyvisa, and interprets the results. The user can read powers and control the instrument, by changing the power range, cal factor, etc.

-------------
Prerequisites
-------------

Must have the python programming language installed with the following 
packages:

- pyvisa

------------
Installation
------------

Python and required packages (pyvisa) must be installed prior to installing.
- To install use     
```
pip install pyPM5
```
- And to import use
```
from pyPM5 import pyPM5
```

-----
Example Usage
-----
```
from pyPM5 import pyPM5
power_meter = pyPM5.PM5()
PM5.list_resources()
>>> ["ASRL1::INSTR"]
power_meter.connect("ASRL1::INSTR")
power_meter.read_power()
>>> 0.00215

```
-----------
Change Log
-----------
v 0.0.4
- Changed ability to import

## CLASSES
    builtins.object
        PM5

    class PM5(builtins.object)
     |  A class that wraps the pyvisa object and allows for automatic power readings and
     |  range changes. The "powermeter" object contains the original pyvisa object that is used for
     |  communication. The read_power function basically sends a write/read command and interprets the returned information.
     |
     |  Methods defined here:
     |
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  close(self)
     |
     |  connect(self, COMport)
     |      Connect device using COM port
     |      Args:
     |          COMport (str): string containing COM port as listed by rm.list_resources(), e.g ASRL16::INSTR
     |
     |  read(self, num_of_bytes)
     |      Allows access to native pyvisa object read_bytes function
     |      Args:
     |          num_of_bytes (int): number of bytes to be read by function
     |
     |  read_power(self)
     |      Returns the a single reading in units of watts, and updates
     |      range_setting and cal_factor properties. Note that currently the conversion assumes a positive reading, as
     |      it uses unsigned integers
     |
     |  set_range(self, range_index, range_hold=1)
     |      Manually set the reading range, whilst the front panel is set to "Remote".
     |      Args:
     |          range_index (int) : index corresponding to the chosen power meter range
     |              1 : 200 microW
     |              2 : 2 mW
     |              3 : 20 mW
     |              4 : 200 mW
     |              5 : 200 uW auto
     |              6 : 2 mW auto
     |              7 : 20 mW auto
     |              8 : 200 mW auto
     |          range_hold (int): variable to choose whether to activate range hold mode, i.e to stop it
     |              automatically changing.
     |              0 : Range hold off
     |              1 : Range hold on
     |
     |  set_zero(self)
     |      Remotely zeros the powermeter
     |
     |  write(self, x)
     |      Allows access to native pyvisa object write function
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
