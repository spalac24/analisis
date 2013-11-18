import cmath
import numpy
import scikits.audiolab as audio
import matplotlib.pyplot as plt
import random


def w(p, q):
   return cmath.exp((2.0 * cmath.pi * 1j * q) / p)

def pad(inputList):  #Expande la lista para que tenga tama~no 2**k
   k = 0
   while 2**k < len(inputList):
      k += 1
   return numpy.concatenate((inputList, ([0] * (2**k - len(inputList)))))

def fft(signal):   #Aplica FFT
   n = len(signal)
   if n == 1:
      return signal
   else:
      Fe = fft([signal[i] for i in xrange(0, n, 2)])
      Fo = fft([signal[i] for i in xrange(1, n, 2)])

      combined = [0] * n
      for m in xrange(n/2):  #Aplica el paso recursivo, para reducir el orden, se resta en m+n/2 por el factor omega
         combined[m] = Fe[m] + w(n, -m) * Fo[m]
         combined[m + n/2] = Fe[m] - w(n, -m) * Fo[m]

      return combined

def ifft(signal): #Inverso de la FFT, que se define como Fi(f) = F*(f*)
   inv = fft([x.conjugate() for x in signal])
   return [x.conjugate()/len(signal) for x in inv]


norm = lambda x: cmath.polar(x)[0]


def frequencyFilter(signal): #cleans noise signal
    for i in range(20000, len(signal)-20000):
      signal[i] = 0


def process(signal): #takes noised signal, applies FFT, cleans noise, applies IFFT
   transformedSignal = numpy.array(fft(pad(signal)))
   frequencyFilter(transformedSignal)

   cleanedSignal = ifft(transformedSignal)
   return numpy.array(cleanedSignal, dtype=numpy.float64)


filename = raw_input('Ingrese el nombre del archivo  **_ent.wav  ')


(iSignal, samplingRate, bits) = audio.wavread(filename+'_ent.wav')
iSignal = numpy.array([x/2.0 + random.random()*0.1 for x in iSignal])

noised = audio.Sndfile(filename+'_noisy.wav', 'w', audio.Format('wav'), 1, samplingRate)
noised.write_frames(iSignal)
noised.close()

oSignal = process(iSignal)

oFile = audio.Sndfile(filename+'_transformed.wav', 'w', audio.Format('wav'), 1, samplingRate)
oFile.write_frames(oSignal)
oFile.close()
