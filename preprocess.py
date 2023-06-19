from scipy import signal
import numpy as np

class PreProcess:
    def __init__(self,wave,sample_rate=200,notch_freq=60,Q=30,channels=4,event_channel=False,event_channel_num=4):
        self.sr=sample_rate
        self.wave=wave
        self.nf=notch_freq
        self.Q=Q
        self.ch=channels
        self.nw=[]
        self.ec=event_channel     #if event channel is true then we need channel number
        if self.ec:
            if isinstance(ecn,list):
                self.ecn=even_channel_num
            else:
                self.ecn=[event_channel_num]
            self.ch=self.ch-len(self.ecn)   #if event channel exists number of channel is reduced by that amount
    


    def notched_wave(self):
        b, a = signal.iirnotch(self.nf, self.Q, self.sr)
        
        for i in range(len(self.wave)):
            new_array=[]
            new_array.append(signal.filtfilt(b,a,self.wave[i][:self.ch,:],axis=1))
            new_array=np.stack(new_array)
            pad=np.zeros((self.ch,20000))
            pad[:,:len(self.wave[i][1])]=new_array
            self.nw.append(pad)
        
        
    #def bandpass_filter(self):
        