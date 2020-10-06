#!/usr/bin/env python3
import yaml
stream = open('config.yaml','r')
x = yaml.safe_load(stream)
print(x)

