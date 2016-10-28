    This work as a BurpSuite Extension Demo to Hijack
    parsing HTTP requests and modifying related data.
 
 

#Before you run:
    Complete the functions of Hijacking
    HijackRequestHeader(Header)
    
    
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
            -Options
                Edit        Binding to All interfaces
                OK
                
    Setup Proxy
        Android:            Settings - WLAN - LongPress on Current Hotspot - Modify Network
                            - Advanced Settings - Proxy:Manual FiFServerIP 8080
        iOS:                same
        Windows/Mac/Linux:  ...


