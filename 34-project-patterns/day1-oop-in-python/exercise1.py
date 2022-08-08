# exercise 1
# build a class named Television
# to initialize, it receives the screen size
# private attributes are: volume, channel, and on
# create the following methods:
# raise and lower volume between 0 and 99
# change channels between 1 and 99
# turn tv on and off

class Television:
    def __init__(self, size):
        self.__volume = 50
        self.__channel = 1
        self.__size = size
        self.__on = False

    def raise_volume(self):
        if self.__volume == 99:
            self.__volume = 99
        else:
            self.__volume += 1

    def lower_volume(self):
        if self.__volume == 0:
            self.__volume = 0
        else:
            self.__volume -= 1

    def change_channel(self, channel):
        if not int(channel) or (channel > 99 or channel < 1):
            raise ValueError("invalid channel")
        else:
            self.__channel = channel

    def on_off(self):
        if self.__on:
            self.__on = False
        else:
            self.__on = True


tv = Television(60)
tv.change_channel(2)
tv.change_channel(152)
tv.raise_volume()
tv.lower_volume()
tv.on_off()
