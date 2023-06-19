import numpy as np
import pandas as pd
import librosa

class GetFeatures:
    def __init__(self,wave,sample_rate=200,n_mfcc=40,n_mels=8,fmax=50,compute_mfc=True,compute_mel=True,compute_chr=True):
        self.wave=wave
        self.sr=sample_rate
        self.n_m=n_mfcc
        self.n_mels=n_mels
        self.fmax=fmax
        self.mfc=[]
        self.mel=[]
        self.chr=[]
        self.combined_features=[]
        self.compute_mfc=compute_mfc
        self.compute_mel=compute_mel
        self.compute_chr=compute_chr
        
    def compute_features(self):
        if self.compute_mfc:
            self.mfc=np.mean(librosa.feature.mfcc(y=self.wave, sr=self.sr, n_mfcc=self.n_m,n_fft=10).T, axis=0) 
        if self.compute_mel:
            self.mel=np.mean(librosa.feature.melspectrogram(y=self.wave, sr=self.sr, n_mels=self.n_mels, fmax=self.fmax).T,axis=0)
        if self.compute_chr:
            self.chr=np.mean(librosa.feature.chroma_stft(y=self.wave, sr=self.sr).T,axis=0)
    def combine(self):
        combined_feature=[]
        if self.compute_mfc:
            combined_feature.append(self.mfc)
        if self.compute_mel:
            combined_feature.append(self.mel)
        if self.compute_chr:
            combined_feature.append(self.chr)
        #print(combined_feature)
        self.combined_features=np.concatenate(combined_feature,axis=0) if combined_feature else None
        combined_feature.clear()  #not absolutely necessary as python will clear garbage anyway