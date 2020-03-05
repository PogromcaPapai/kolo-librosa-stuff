import librosa
import numpy
from random import random

y1, sr1 = librosa.load(librosa.util.example_audio_file())
tempo1, beats1 = librosa.beat.beat_track(y=y1, sr=sr1)
#librosa.output.write_wav('gg.wav', *librosa.load(librosa.util.example_audio_file()))

y2, sr2 = librosa.load('Kevin_MacLeod_-_Anachronist.wav')
tempo2, _ = librosa.beat.beat_track(y=y2, sr=sr2)
y2_new = librosa.effects.time_stretch(y2, tempo1/tempo2)
tempo2_new, beats2_new = librosa.beat.beat_track(y=y2_new, sr=sr2)

beats2_new = librosa.core.frames_to_samples(beats2_new)
beats1 = librosa.core.frames_to_samples(beats1)
chosen = True
finished = y2_new[:beats2_new[0]]

if len(beats1)>len(beats2_new):
    length = len(beats2_new)
    longer = beats1
else:
    length = len(beats1)
    longer = beats2_new

for i in range(length-1):
    if chosen:
        finished = numpy.append(finished, y1[beats1[i]:beats1[i+1]])
    else:
        finished = numpy.append(finished, y2_new[beats2_new[i]:beats2_new[i+1]])
    if random()<0.2:
        chosen = not(chosen)
numpy.append(finished, longer[length:])

librosa.output.write_wav('dd.wav', finished, sr1, norm=True)