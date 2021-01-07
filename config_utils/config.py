import yaml

def load_configs():
    with open(r'/home/pi/miflora/config_utils/config.yaml') as f:
        configs = yaml.load(f, Loader = yaml.FullLoader)
        return configs

#if __name__ == '__main__':
#    print(load_configs())
