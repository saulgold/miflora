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
sensor_data_dir = configs['data_dir']
log_path = configs['sensor_log_path']
logging.basicConfig(filename = log_path, level=logging.DEBUG)
logging.info('bluetooth sensor logging initialised')
logging.info('Initialising sensor')

logging.info('Sensor initialised')
wait_time = 60 

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
        sensors = configs['sensors']
        for sensor in sensors:
            sensor_data_csv = os.path.join(sensor_data_dir,sensor+'.csv')

            mac = sensors[sensor]
            ms = MiSensor(mac)

            now = datetime.datetime.now()
            print(now)
            logging.info('Time: %s', now.strftime("%m/%d/%Y, %H:%M:%S"))
            logging.info('Reading from sensor')

            sensor_dict = collections.OrderedDict()
            logging.info('Read successful')
            sensor_dict['time'] = now
            sensor_dict['temperature'] = ms.get_temperature()
            sensor_dict['battery'] = ms.get_battery()
            sensor_dict['light'] = ms.get_light()
            sensor_dict['moisture'] = ms.get_moisture()
            sensor_dict['conductivity'] = ms.get_conductivity()
            print(sensor_dict)

            logging.info('Saving sensor data to: ' + sensor_data_csv)
            print('Saving sensor data to: ' + sensor_data_csv)
            if not os.path.isdir(os.path.dirname(sensor_data_csv)):
                os.makedirs(os.path.dirname(sensor_data_csv))
            dict_to_csv(sensor_dict, sensor_data_csv)
            logging.info('Save successful')
            logging.info('Waiting : %s seconds', str(wait_time))



        time.sleep(wait_time)
