import argparse





def parse_list(arg):
        el=arg.split(',')
        el=[els.strip() for els in el]
        return el
        
class parse_arguments:
    def __init__(self):
        self.parser=argparse.ArgumentParser()
        self.parser.add_argument("--input_path",type=str,help="path of directory containing txt files")
        self.parser.add_argument("--sample_rate",type=int,default=200,help="Sample rate of the wave data")
        self.parser.add_argument("--notch_freq", type=float, default=60, help="Notch filter frequency")
        self.parser.add_argument("--Q", type=float, default=30, help="Quality factor of the notch filter")
        self.parser.add_argument("--channels", type=int, default=4, help="Number of channels in the wave data")
        self.parser.add_argument("--n_mfcc",type=int,default=40,help="Number of mfcc features to be used")
        self.parser.add_argument("--n_mels",type=int,default=8,help="Number of melspectrogram features")
        self.parser.add_argument("--fmax",type=int,default=50,help="Maximum frequency to sample data")
        self.parser.add_argument("--event_channel",type=bool,default=False,help="if event channel exists or not")
        self.parser.add_argument("--event_channel_num",type=parse_list,help="channel number for event")
        self.args=self.parser.parse_args()

        
    def parse_path(self):
        input_path=self.parser.parse_args()
        return input_path
    def parse_preprocess(self):
        return 0