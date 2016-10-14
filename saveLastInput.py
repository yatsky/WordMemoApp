#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import cfg
def saveLastInput(lastFile='MedicalTermsComplete', lastTarget=1, lastMode='Chinese'):
    # lastFile = lastFile
    # lastTarget = lastTarget
    # lastMode = lastMode
    last = [lastFile, str(lastTarget), lastMode]
    last = '\n'.join(last)
    path = os.path.join(os.getcwd(), 'configs')
    path = os.path.join(path, 'inputs')
    
    if not os.path.isfile(path):
        with open(path, 'w') as f:
            f.write(None)
            
    with open(path, 'w') as f:
        # f.write(lastFile)
        # f.write(lastMode)
        # f.write(lastTarget)
        f.writelines(last)
    print "User inputs saved!"
    return None