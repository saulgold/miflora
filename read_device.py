from flowercare import FlowerCare

#initialize FlowerCare device
device = FlowerCare(
            mac='c4:7c:8d:xx:xx:xx', # device address
                interface='hci0' # hci0 is default, explicitly static for demo purpose
                )

print('Name: {}'.format(device.name))

