import subprocess
import uuid





def asteriskCheck():
    #import subprocess
    cmd = "/etc/init.d/asterisk status"
    service = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    if "Active: active" in service.communicate()[0]:
        return True
    else:
        return False
        
def asteriskStart():
    #import subprocess
    cmd = "sudo service asterisk start"
    service = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)    

def asteriskStop():
    #import subprocess
    cmd = "sudo service asterisk stop"
    service = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)    
    



def dialFileGen(numToCall, duration, waitBeforeDtmf, dtmfs, filename):
    fo = open(filename, "w")
    fo.write('Channel: Local/s@greeting'+'\n'
    'Context: from-sip'+'\n'
    'Extension: 777'+'\n'
    'Priority: 1'+'\n'
    'Callerid: "Dialer-out"<111{}>'.format(str(numToCall))+'\n'
    'Archive: Yes'+'\n'
    'MaxRetries: 0'+'\n'
    'RetryTime: 10'+'\n')
    if dtmfs <> "":
        fo.write('WaitTime: {}'.format(waitBeforeDtmf)+'\n'
        'Set: PassedInfo={}-{}-{}'.format(str(duration),str(numToCall), str(dtmfs))+'\n')
    else:
        fo.write('WaitTime: '+str(5)+'\n'
        'Set: PassedInfo={}-{}-empty'.format(str(duration),str(dtmfs))+'\n')
    fo.close()
        


dialFileGen(995533, 30, 5,"www3")