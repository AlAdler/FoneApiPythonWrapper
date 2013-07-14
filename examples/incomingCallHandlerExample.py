'''
Created on Jul 14, 2013

@author: Alain Adler
'''

from FoneApiPythonWrapper.CallBackResponse import CallBackResponse

#call this function when foneapi call your incomingCallHandler service to get the json foneapi expects
def handleIncomingCall(callerId):
    response = CallBackResponse()
    #connect the incoming call with another phone number
    response.dial("5557654321", callerId, "http://myserver/dialCallEndedHandler", record = True)
    #limit the call duration to 10 minutes
    response.setLimitCallDuration(600)
    #return the json
    return response.json()
    
    
print handleIncomingCall("5551231231")