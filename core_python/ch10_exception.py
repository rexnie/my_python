#!/usr/bin/env python

def safe_float(obj):
    """safe version of float(),show try-except statement"""
    try:
        retval = float(obj)
    except (ValueError,TypeError),diag:
        retval = str(diag)
        
    return retval

def card_run():
    log = open('cardlog.txt','w')
    
    try:
        ccf = open('carddate.txt','r')
    except IOError,e:
        log.write('no txns this month,error= %s\n' % str(e))
        log.close()
        return
    
    txns = ccf.readlines()
    ccf.close()
    total = 0.00
    log.write('account log:\n')
    
    for each in txns:
        ret = safe_float(each)
        if(isinstance(ret,float)):
            total += ret
            log.write('date ... processed\n')
        else:
            log.write('ignored: %s' % ret)
    
    print '$%.2f (new balance)' % total
    log.close()
    
if __name__ == "__main__":
    card_run()