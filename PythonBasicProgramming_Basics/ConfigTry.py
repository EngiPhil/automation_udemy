from configparser import ConfigParser

# Created object of ConfigParser class
config = ConfigParser()

# to read data from config file
config.read("C:/Users/FilipV/Filip/PyCharm/Automation1/InputFiles/Config.cfg")

# Why is this not workin?
# config.read("./InputFiles/Config.cfg")

print(config.get("Section1", "username"))
