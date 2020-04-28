from miplant import MiPlant

sensors = MiPlant.discover(interface_index=0, timeout=5)
print('Found ' + str(len(sensors)) + ' sensor/s')

for plant in sensors:
        print('--------------------------')
        print('Address: %s' % plant.address)
        print('Battery level: %i%%' % plant.battery)
        print('Firmware: %s' % plant.firmware)
        print('Temperature: %.01f °C' % plant.temperature)
        print('Light: %.0f lx' % plant.light)
        print('Moisture: %.0f%%' % plant.moisture)
        print('Conductivity: %.0f µS/cm' % plant.conductivity)
