import json
from collections import OrderedDict
from flowercare import FlowerCare, FlowerCareScanner

# Do this if permission issues with bluepy: 
#  sudo setcap cap_net_raw+e  <PATH>/bluepy-helper
#  sudo setcap cap_net_admin+eip  <PATH>/bluepy-helper

# Initialize the scanner with BT interface and a 
# custom callback for newly discovered devices.
scanner = FlowerCareScanner(
            interface='hci0',  # hci0 is default, explicitly stating for demo purpose
                callback=lambda device: print('Found device', device.addr) # any lambda with the device as the sole argument will do
                )
print(" initialised scanner")


# Scan advertisements for 10 seconds 
# and return found device list.
print("scanning devices...")

devices = scanner.scan(timeout=10)
print(len(devices))
# Iterate over results and query the information 
# for each individual device.
device_information = OrderedDict()
print("device loop")
for device in devices:
    device = FlowerCare(
                        mac=device.addr, # address of the device to connect to
                        interface='hci0' # hci0 is default, only explicitly stating for demo purpose
                        )

    print(device.mac)
    print(device)
    print(device.real_time_data)
   
    #print(device_information[device.mac])
    #device_information[device.mac] = OrderedDict([('name', device.name), ('firmware', device.firmware_version), ('battery', device.battery_level), ('measurements', device.real_time_data.__dict__)])

#Pretty print device information
print(json.dumps(device_information, indent=4))
