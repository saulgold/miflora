#https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
from miplant import MiPlant
import datetime
import csv
import os 
import collections
import time
import logging
import yaml

from sensor_utils import MiSensor
from config_utils.config import load_configs
configs = load_configs()
sensor_data_csv = configs['sensor_data_path']
log_path = configs['sensor_log_path']
logging.basicConfig(filename = log_path, level=logging.DEBUG)
logging.info('bluetooth sensor logging initialised')
logging.info('Initialising sensor')
print(configs['sensor_white'])
#sensor = MiPlant(address = 'c4:7c:8d:66:64:39')
sensor_white = MiSensor(configs['sensor_white'])
sensor_green = MiSensor(configs['sensor_green'])

logging.info('Sensor initialised')
wait_time = 5 

def dict_to_csv(in_dict, save_file): 
    my_dict = in_dict
    with open(save_file, 'a') as f:
        w = csv.DictWriter(f, my_dict.keys())
        if f.tell() == 0:
            w.writeheader()
            w.writerow(my_dict)
        else: 
            w.writerow(my_dict)
if __name__ == '__main__':
    logging.info('Entering loop')
    while True:
 
        now = datetime.datetime.now()
        print(now)
        logging.info('Time: %s',  now.strftime("%m/%d/%Y, %H:%M:%S"))
        logging.info('Reading from sensor')
       
        
        sensor_dict = collections.OrderedDict()
        print(sensor_dict)
        logging.info('Read successful')
        sensor_dict['time'] =  now
        #sensor_dict['temperature_white']= sensor_white.get_temperature()
        sensor_dict['temperature_green'] = sensor_green.get_temperature()
        sensor_dict['battery_green'] = sensor_green.get_battery()
        sensor_dict['light_green'] = sensor_green.get_light()
        sensor_dict['moisture_green'] = sensor_green.get_moisture()
        sensor_dict['conductivity_green'] = sensor_green.get_conductivity()
        print(sensor_dict)
       
        logging.info('Saving sensor data to: '+sensor_data_csv)
        if not os.path.isdir(os.path.dirname(sensor_data_csv)):
            os.makedirs(os.path.dirname(sensor_data_csv))
        dict_to_csv(sensor_dict, sensor_data_csv)
        logging.info('Save successful')
        logging.info('Waiting : %s seconds', str( wait_time))
        time.sleep(wait_time)
