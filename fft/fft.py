import cmath

def omega(p,q):
    return cmath.exp((2.0* cmath.pi * 1j * q)/p)

def fft(signal):
    n = len(signal)
    if n == 1:
        return signal
    else:
        Feven = fft(signal[0::2])
        Fodd = fft(signal[1::2])

        combined = [0]*n
        for m in xrange(n/2):
            if n == 8:
                print m
            combined [m] = Feven[m] + omega(n,-m) * Fodd[m]
            combined[m+n/2] = Feven[m] - omega(n,-m) * Fodd[m]
        return combined
