

import smbus
import time

# channel = 1
# address = 0x5a

bus = smbus.SMBus(1)

# reset
bus.write_i2c_block_data(0x5a, 0x80, [0x63])
# enable gpio
bus.write_i2c_block_data(0x5a, 0x5e, [0x00])
# gpio to led driver (and input)
bus.write_i2c_block_data(0x5a, 0x77, [0xff])
# direction in (out is 1)
bus.write_i2c_block_data(0x5a, 0x76, [0x00])
# input with internal pull-down
#bus.write_i2c_block_data(0x5a, 0x73, [0xff]) # ctl0 to 1
#bus.write_i2c_block_data(0x5a, 0x74, [0x00]) # ctl1 to 0

# input with internal pull-up
bus.write_i2c_block_data(0x5a, 0x73, [0xff]) # ctl0 to 1
bus.write_i2c_block_data(0x5a, 0x74, [0xff]) # ctl1 to 1

start = time.time()
for i in range(1000):
    time.sleep(0.1)
    #bus.write_i2c_block_data(0x5a, 0x75, [4])
    #print bus.read_i2c_block_data(0x5a, 0x75)
    #time.sleep(0.01)
    #bus.write_i2c_block_data(0x5a, 0x75, [0])
    #print bus.read_i2c_block_data(0x5a, 0x75)
    data = bus.read_i2c_block_data(0x5a, 0x75)
    #print "%s" % (bin(data[11]).zfill(8))
    #print data[11] % 64, data[11] % 128
    print '{0:07b}'.format(data[11])

print time.time()-start
