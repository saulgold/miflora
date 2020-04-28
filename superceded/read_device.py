from flowercare import FlowerCare

#initialize FlowerCare device
device = FlowerCare(
        mac='c4:7c:8d:66:64:39', # device address
                interface='hci0' # hci0 is default, explicitly static for demo purpose
                )
while True:
    try:
        real_time_data = device.real_time_data
    
    except:
        print('failed to connect')
