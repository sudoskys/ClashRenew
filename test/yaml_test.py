import yaml

_nowConfig = yaml.load("", Loader=yaml.CFullLoader)

print(_nowConfig)