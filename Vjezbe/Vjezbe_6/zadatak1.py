import harmonic_oscillator as ha

h = ha.HarmonicOscillator()
h.init(0.1, 10, 0.3, 0)
h.oscillate(2)
h.plot_trajectory()

