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

def signal(x):
    """
    Получение значения сигнала от координаты.
    """
    if x < -2 or x > 6:
        return 0
    elif x >= -2 and x <= 2:
        return 1.0
    else:
        return 0.2

def auto_correlation(signal):
    """Вычисляет автокорреляцию для функции."""
    range_ = np.linspace(-6, 6, 256)
    signal_1 = np.array([signal(x) for x in range_])
    signal_2 = np.array([signal(x) for x in range_])

    fft_1 = FFT(signal_1)
    fft_2 = FFT(signal_2)

    fft_2 = np.conjugate(fft_2)

    fourier_inverse = np.fft.ifft(np.multiply(fft_1, fft_2))
    return fourier_inverse

if __name__ == "__main__":
    t = np.linspace(-6, 6, 256)
    values = np.array([signal(x) for x in t])
    fft_result = FFT(values)
    # correlation = auto_correlation(signal)
    # fft_result = np.fft.fft(values)
    plt.plot(fft_result)
    plt.show()
