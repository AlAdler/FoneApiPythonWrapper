'''
Created on Jul 14, 2013

@author: Alain Adler
'''

from FoneApiPythonWrapper.FoneApiClient import FoneApiClient
import time

#create a client
client = FoneApiClient("http://my_foneapiserver/api/1.0/switch", "my_key", "my_secret")

#dial a call
dialResponse = client.dial(FoneApiClient.NUMBER_DESTINATION_TYPE, "5551234567", "http://my_server/callansweredhandler", 0, "verizon_trunk")

print dialResponse

if dialResponse["status"] == 0:
    #hear the phone ring for 10 seconds
    time.sleep(10)   
     
    #hang up the call
    hangupResponse = client.hangup(dialResponse["call_id"])
    print hangupResponse