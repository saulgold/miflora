#https://github.com/open-homeautomation/miflora/blob/master/demo.py
from miflora.miflora_poller import MiFloraPoller
from btlewrap.bluepy import BluepyBackend
from miflora import miflora_scanner
from miflora.miflora_poller import MiFloraPoller, \
            MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY
import signal
device_1 = 'C4:7C:8D:66:64:39' #white sensor
device_2 = '80:EA:CA:89:03:71' #green sensor

#devices = miflora_scanner.scan(BluepyBackend,10)
#print(devices)
#poller_1 = MiFloraPoller(device_1, BluepyBackend)
#poller_2 = MiFloraPoller(device_2, BluepyBackend)
#print("Temperature white : {}".format(poller_1.parameter_value(MI_TEMPERATURE)))
#print("Temperature green : {}".format(poller_2.parameter_value(MI_TEMPERATURE)))

class MiSensor:
    def __init__(self, mac):
        self.poller = MiFloraPoller(mac, BluepyBackend, cache_timeout=1, retries=0)
        self.mac = mac

        name = self.poller.name()




    def get_temperature(self):
        self.last_temperature = self.poller.parameter_value(MI_TEMPERATURE)
        return self.last_temperature
    
    def get_battery(self):
        self.last_battery = self.poller.parameter_value(MI_BATTERY)
        return self.last_battery

    def get_moisture(self):
        
        self.last_moisture = self.poller.parameter_value(MI_MOISTURE)
        return self.last_moisture
    
    def get_conductivity(self):
        self.last_conductivity = self.poller.parameter_value(MI_CONDUCTIVITY)
        return self.last_conductivity
    
    def get_light(self):
        self.last_light = self.poller.parameter_value(MI_LIGHT)
        return self.last_light



# if __name__ == '__main__':
#     sens = MiSensor(device_2)
#     temp = sens.get_temperature()
#     print(temp)
