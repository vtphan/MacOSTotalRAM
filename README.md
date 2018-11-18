
This program is intended to be useful when you want to estimate how much RAM
is needed for a system to have little memory pressure, i.e. without memory
compression on a MacOS system.

The program computes the total amount of RAM of all programs being run on a
MacOS system.  Total RAM is not the same as "memory usage", displayed by
Activity Monitor.  Due to memory compression, memory usage is always less
than the system memory.  Memory usage is, therefore, not the total of RAM
of all programs being run.

## Usage
```
python total_RAM.py
```