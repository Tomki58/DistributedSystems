import math
import numpy as np
import matplotlib.pyplot as plt

def DFT_slow(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def FFT(x):
    """A recursive implementation of the 1D Cooley-Tukey FFT"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:  # this cutoff should be optimized
        return DFT_slow(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate(
            [X_even + factor[: int(N / 2)] * X_odd, X_even + factor[int(N / 2) :] * X_odd]
        )

# TODO: реализовать функцию для вычисления значения сигнала
def signal(x):
    pass

if __name__ == "__main__":
    t = np.arange(256)
    fft_result = FFT(np.sin(t))
    plt.plot(fft_result)
    plt.show()
