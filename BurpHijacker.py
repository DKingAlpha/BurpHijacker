'''
    This works as a BurpSuite Extension to control every
    content of your requests, by parsing HTTP requests and modifying related data.
 
#Notice:
    This is not a Download&Run Project !
    You have to complete this project before it works for you!


#Before you run:
    Complete the functions in lib/injector.py !
    

#How to setup:

    Python 2.7
    Jython2.7.jar
    BurpSuite
        -Extender
            -Options
                Python Environment
                    Locate  jython.jar and FiFHack/
            -Extensions
                Add FifBurpExt.py
                Next
        Tick to Launch the Filter
        -Proxy
            -Intercept      Intercept Off
            -Options
                Edit        Binding to All interfaces
                OK
                
    Setup Proxy
        Android:            Settings - WLAN - LongPress on Current Hotspot - Modify Network
                            - Advanced Settings - Proxy:Manual ServerIP 8080
        iOS:                same
        Windows/Mac/Linux:  ...



'''

from burp import IBurpExtender
from burp import IProxyListener
from burp import IHttpRequestResponse
from java.io import PrintWriter
from lib.injector import request_match,modifypost,modifyjson,modifyheader


#cannot use ConfigObj because jython path
conf = {}
conf['FLAG'] = 'POST /users/sign_in HTTP/1.1'



VERSION = (0, 1)
__version__ = '1.0.0'
__description__ = 'A Demo of Burp Extension'
__author__ = 'DKing'
__author_email__ = 'DKingCHN@gmail.com'
__license__ = 'GPL'


class BurpExtender(IBurpExtender,IProxyListener):


    def registerExtenderCallbacks(self, callbacks):
        callbacks.setExtensionName("Burp Request Auto Intruder")
        callbacks.registerProxyListener(self)
        self._helpers = callbacks.getHelpers()
        self._stdout = PrintWriter(callbacks.getStdout(), True)
        self._stderr = PrintWriter(callbacks.getStderr(), True)
        #self._stdout.println() to debug


        

    def processProxyMessage(self,messageIsRequest,message):
        if messageIsRequest:
            request = message.getMessageInfo()
            parsed_request = self._helpers.analyzeRequest(request)
            header = parsed_request.getHeaders()
            if request_hasbody(header):
                body = request.getRequest()[parsed_request.getBodyOffset():]
                sbody = self._helpers.bytesToString(body)
            if request_match(header,sbody,conf):
                hackheader = modifyheader(header,conf)
                if request_hasbody(header):
                    hackbody = modifypost(sbody,conf)
                else:
                    hackbody = ''
                request.setRequest(self._helpers.buildHttpMessage(hackheader, hackbody))
                message.getMessageInfo().setComment("Hacked!")
                message.getMessageInfo().setHighlight("green")


def request_hasbody(header):
    if header[0].startswith('POST') or header[0].startswith('PUT'):
        return True
    else:
        return False