import os
import shutil
import glob
from shutil import copyfile
import numpy as np
from python_speech_features import mfcc
import scipy.io.wavfile as wav
import scipy.io.wavfile as wav

#phn = ['aa', 'ae', 'ah', 'ao', 'aw', 'ax', 'ax-h', 'axr', 'ay', 'b', 'bcl', 'ch', 'd', 'dcl', 'dh', 'dx', 'eh', 'el', 'em', 'en', 'eng', 'epi', 'er', 'ey', 'f', 'g', 'gcl', 'h#', 'hh', 'hv', 'ih', 'ix', 'iy', 'jh', 'k', 'kcl', 'l', 'm', 'n', 'ng', 'nx', 'ow', 'oy', 'p', 'pau', 'pcl', 'q', 'r', 's', 'sh', 't', 'tcl', 'th', 'uh', 'uw', 'ux', 'v', 'w', 'y', 'z', 'zh']

def function2(rootdir,label_dir):#This function makes a dictionary of the phonemes in the file mapping with phn
    count = 0
    for subdir, dirs, files in os.walk(rootdir):
         for file in files:
            fullFilename = os.path.join(subdir,file)
            filenameNoSuffix =  os.path.splitext(fullFilename)[0]
            #gets the entire path from timit to end
            #eg:TIMIT/TRAIN/DR8/MMWS0/SX78
            #print (filenameNoSuffix)
            if file.endswith('.WAV'):
                    labelFilename = filenameNoSuffix + '.WAV'
                    (rate,sig) = wav.read(fullFilename)

					# get mfcc
                    mfcc_feat = mfcc(sig,rate,winlen=0.005,winstep=0.001)
                    print (np.shape(mfcc_feat))
                    count+=1
                    print ("File index:",count)
                    #important Line
                    labelFilename = label_dir+filenameNoSuffix.split('/')[-1]+'.npy'
                    print(labelFilename)
                    np.save(labelFilename,mfcc_feat)

function2('./WAVFiles','./mfccnpyFiles/')
#Use the below code for creating label npy files that is
'''import numpy as np
data = np.load('./phonemeLabels/FADG0-SA1.npy')
print(data)'''