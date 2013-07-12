'''
Created on Jul 12, 2013

@author: Alain Adler
'''

import base64
import requests

class FoneApiClient(object):
    '''
    classdocs
    '''

    NUMBER_DESTINATION_TYPE = "number"
    IP_DESTINATION_TYPE = "ip"

    def __init__(self, urlBase, fapiKey, fapiSecret):
        self.urlBase = urlBase
        self.fapiKey = fapiKey
        self.fapiSecret = fapiSecret
        
    def dial(self, destinationType, destination, url, appId, trunk, fallbackUrl = "",
            dialTimeout ="", callerIdNum = "", callerIdName = "", delay = ""):
        try:
            url = self.urlBase + "/dial//"
            authKey = base64.b64encode(self.fapiKey + ":" + self.fapiSecret)
            headers = {'content-type': 'application/json', "Authorization":"Basic " + authKey}
            parameters = { "dest_type":destinationType, "dest":destination, "url":url, "app_id":appId, "trunk":trunk }
            if fallbackUrl != None and fallbackUrl != "":
                parameters["fallback_url"] = fallbackUrl
            if dialTimeout != None and dialTimeout != "":
                parameters["dial_timeout"] = dialTimeout
            if callerIdNum != None and callerIdNum != "":
                parameters["caller_id_num"] = callerIdNum
            if callerIdName != None and  callerIdName != "":
                parameters["caller_id_name"] = callerIdName
            if delay != None and delay != "":
                parameters["delay"] = delay
            response = requests.get(url, params=parameters, headers=headers)
            status = response.status_code
            if(status == 200):
                return response.json()
            else:
                return { "status":-10, "error_msg":"Failed: http status: " + str(status) }                
        except Exception as e:
            return { "status":-20, "error_msg":"Failed with exception: " + str(e) }  
        
    def hangup(self, callId):
        try:
            url = self.urlBase + "/hangup//"
            authKey = base64.b64encode(self.fapiKey + ":" + self.fapiSecret)
            headers = {'content-type': 'application/json', "Authorization":"Basic " + authKey}
            parameters = { "call_id": callId }
            response = requests.get(url, params=parameters, headers=headers)
            status = response.status_code
            if(status == 200):
                return response.json()
            else:
                return { "status":-10, "error_msg":"Failed: http status: " + str(status) }                
        except Exception as e:
            return { "status":-20, "error_msg":"Failed with exception: " + str(e) }  
        
        
        