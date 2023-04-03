# Phil's actually useful Hello World Greengrass Component

## (What is AWS greengrass?)

From my point of interest, it is a cloud-managed system to deliver
"Components" to run on a system automatically.

Official summary is at

https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html

## Why anothor Hello World

The existing ones I have found out there do literally nothing other than
run a python prog, normal style. The program does no real greengrass
integration

This one actually does a greengrass operation, of pulling a "TestValue" from
the configuration store.

## Deployment type: local

This is currently only set up for  local-only deployment.
You do NOT go through the fancy AWS cli to store it in AWS
and then pull it down from AWS again.

This requires that you have greengrass installed with the "greengrass-cli"
option installed


At some point, I may add an S3 example deploy though.

## Requrements


1. You need your greengrass with the "cli" module installed
   (That means that /greengrass/v2/bin/greengrass-cli exists)
   
2. You need the version of greengrass to be at least 2.9, otherwise
the local deploy may complain about missing "metadata.json" and fail.


## Component summary

This sample component prints a hello.
It then attempts to read a configuration variable.


## Deploy this sucker!

     make localdeploy
	 
	 
## Clean up this sucker!


    make remove
	
## Debug this sucker!

    tail -f /greengrass/v2/logs/com.bolthole.hello.log


# AWS API docs

## Greengrass v2

https://docs.aws.amazon.com/greengrass/v2/developerguide/interprocess-communication.html 

(look at the Example subscription handlers, and choose the python client v2 subtype)

###

List of all the annoying "allow" types for greengrass:
https://docs.aws.amazon.com/greengrass/v2/developerguide/ipc-local-deployments-components.html#ipc-local-deployments-components-authorization


## More general IoT client library

https://aws.github.io/aws-iot-device-sdk-python-v2/

## (and the more general AWS API is at)

https://aws.amazon.com/sdk-for-python/

# See also

https://github.com/aws-greengrass/aws-greengrass-component-templates/releases/download/v1.0/HelloWorld-python.zip
