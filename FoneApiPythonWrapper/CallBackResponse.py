'''
Created on Jul 13, 2013

@author: Alain Adler
'''

import json

class CallBackResponse(object):
    
    def __init__(self):        
        self.actions = []
        self.settings = []
        
    def answer(self):
        self.actions.append({ "answer":{} })
        
    def dial(self, numbers, callerId, url, record = False):
        dialAction = { "dial":{"numbers":numbers, "caller_id":callerId, "url":url, "record":record} }
        self.actions.append(dialAction)
        
    def bridgeTo(self, otherCallId, url):
        bridgeToAction = { "bridge_to":{ "other_call_id":otherCallId, "url": url } }
        self.actions.append(bridgeToAction)
        
    def setLimitCallDuration(self, limitCallDurationSeconds):
        found = False
        for item in self.settings:
            if "set_limit_call_duration" in item:
                item["set_limit_call_duration"] = {"seconds":limitCallDurationSeconds}
                found = True
                break
        if found == False:
            self.settings.append({ "set_limit_call_duration": {"seconds":limitCallDurationSeconds} })
    
    def json(self):
        retVal = { "actions" : self.actions }
        if len(self.settings) > 0:
            retVal["settings"] = self.settings
        return json.dumps(retVal)
        