import utime
from machine import I2C, Pin
from ak8963 import AK8963
from mpu9250 import MPU9250
from mpu6500 import MPU6500, SF_G, SF_DEG_S

i2c = I2C(scl=Pin(12), sda=Pin(14))
ak8963 = AK8963(
    i2c,
    offset=(-11.6288, 20.7088, -55.9863),
    scale=(0.951743, 1.06654, 0.988447)
)
mpu6500 = MPU6500(i2c, accel_sf=SF_G, gyro_sf=SF_DEG_S)
sensor = MPU9250(i2c, mpu6500=mpu6500, ak8963=ak8963)

print("MPU9250 id: " + hex(sensor.whoami))

data_file = open('data.txt', 'a+')

while True:
    data_file.write('Acceleration: {}\n'.format(sensor.acceleration))
    data_file.write('Gyro: {}\n'.format(sensor.gyro))
    data_file.write('Magnetic: {}\n'.format(sensor.magnetic))
    data_file.flush()
    utime.sleep_ms(166)
