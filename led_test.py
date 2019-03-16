

import smbus
import time

# channel = 1
# address = 0x5a

bus = smbus.SMBus(1)

# reset
bus.write_i2c_block_data(0x5a, 0x80, [0x63])
# enable gpio
bus.write_i2c_block_data(0x5a, 0x5e, [0x00])
# gpio to led driver
bus.write_i2c_block_data(0x5a, 0x77, [0xff])
# direction out
bus.write_i2c_block_data(0x5a, 0x76, [0xff])
# led-driver mode 
bus.write_i2c_block_data(0x5a, 0x73, [0xff])
bus.write_i2c_block_data(0x5a, 0x74, [0xff])

for i in range(10):
    time.sleep(1)
    bus.write_i2c_block_data(0x5a, 0x75, [4])
    time.sleep(1)
    bus.write_i2c_block_data(0x5a, 0x75, [0])


