


# print devices
i2cdetect -y 1

## soft reset
i2cset -y 1 0x5a 0x80 0x63

## enable gpio (stop mode)
i2cset -y 1 0x5a 0x5e 0x00

## enable gpio-pins to led driver
i2cset -y 1 0x5a 0x77 0xff

## direction out (gpio-pins to led driver)
i2cset -y 1 0x5a 0x76 0xff

## led driver mode ct10=1 ct11=1
i2cset -y 1 0x5a 0x73 0xff
i2cset -y 1 0x5a 0x74 0xff


## turn on led 3: 00000100 = 4
i2cset -y 1 0x5a 0x75 4





