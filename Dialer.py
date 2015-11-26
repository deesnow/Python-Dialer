def asteriskCheck():
    import subprocess
    cmd = "/etc/init.d/asterisk status"
    service = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if "Active: active" in service.communicate()[0]:
        return True
    else:
        return False
        
    
    
    



def dialFileGen(numToCall, duration, waitBeforeDtmf, dtmfs):
    print 'Channel: Local/s@greeting'   
    print 'Context: from-sip'
    print 'Extension: 777'
    print 'Priority: 1'
    print 'Callerid: "Dialer-out"<111{}>'.format(str(numToCall))
    print 'Archive: Yes'
    print 'MaxRetries: 0'
    print 'RetryTime: 10'
    if dtmfs <> "":
        print 'WaitTime: {}'.format(waitBeforeDtmf)
        print 'Set: PassedInfo={}-{}-{}'.format(str(duration),str(numToCall), str(dtmfs))
    else:
        print 'WaitTime: '+str(5)
        print 'Set: PassedInfo={}-{}-empty'.format(str(duration),str(dtmfs))
        


dialFileGen(995533, 30, 5,"www3")