#!/bin/python

import sys

from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2

print("Hello " + sys.argv[1])

clientobj = GreengrassCoreIPCClientV2()
config_response = clientobj.get_configuration()
print("printing TestValue:: " + config_response.value["TestValue"])


