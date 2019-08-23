# IMU-project

This project is meant to run on an esp8266
with the IMU sensor attached to it.

## ESP8266

The esp8266 used when writing this was
a crowtail esp8266 running with lua firmware.
I have erased that firmware and flashed micropython
on it instead.

To reflash micropython follow the docs [here](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html)

To reflash lua on the board also follow the docs [here](https://www.elecrow.com/wiki/index.php?title=ESP8266_IOT_Board(Arduino_IDE_or_NodeMCU_Lua_Programming)#Load_the_firmware)

## Micropython

Once the device is attached to your laptop through USB
You can use screen to access the python interpreter.

`screen /dev/ttyUSB0 115200`

To upload/download files from the device you can use 
the [ampy](https://github.com/pycampers/ampy) library

`ampy --port /dev/ttyUSB0 ls`

`ampy --port /dev/ttyUSB0 get`

`ampy --port /dev/ttyUSB0 put`

## The code

`main.py` is where the logic lies since micropython automatically
runs it on startup (Default micropython behaviour)

It simply loads the sensor classes then starts a loop that
endlessly appends to a file called `data.txt`. Which should be
retrieved afterwards.

## IMU 
The IMU contains two sensors BMP280 and MPU9250

The MPU9250 is a accelerometer/gyro/compass while the
BMP280 is a barometric pressure and temperature sensor.

## Libraries
The libraries for both modules are in the repo and 
have been uploaded on the device but the code currently 
only reads the MPU9250 sensor.

The library files have been converted to `.mpy` files (micropython byte code) to save memory when loading them. This was done using 
`mpy-cross`. 

# References

#### mpy-cross

https://github.com/micropython/micropython/tree/master/mpy-cross

#### mpu9250
https://github.com/tuupola/micropython-mpu9250

#### BMP280
https://github.com/dafvid/micropython-bmp280


#### The esp8266 used: 

https://www.elecrow.com/wiki/index.php?title=ESP8266_IOT_Board(Arduino_IDE_or_NodeMCU_Lua_Programming)

#### The IMU sensor used:

https://www.elecrow.com/wiki/index.php?title=File:Crowtail-IMU-10DOF.jpg

#### Micropython docs:

https://docs.micropython.org/en/latest/