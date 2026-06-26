import numpy as np
import matplotlib.pyplot as plt
from NuRadioReco.utilities import units

txt_file = "pa_trigger_rate_4channels_2_from35.0-to38.9_det-classifier_station.txt"
title=txt_file[:-4]
thresholds, n_triggers, ts, rates = np.loadtxt(txt_file, unpack=True, skiprows=16)
thresholds = np.round(thresholds, 5)

t_avg = []
rate_avg_err = []
rate_avg = []
for iThres, thres in enumerate(thresholds):
    mask = thresholds == thres
    t = np.sum(ts[mask])
    n_trig = np.sum(n_triggers[mask])
    rate = n_trig / (t)
    rate_error = n_trig ** 0.5 / (t)
    t_avg.append(thres)
    rate_avg_err.append(rate_error)
    rate_avg.append(rate)

t_avg = np.array(t_avg)
rate_avg = np.array(rate_avg)
rate_avg_err = np.array(rate_avg_err)
fig, ax = plt.subplots(1, 1)
ax.errorbar(t_avg, rate_avg / units.Hz, fmt='o', yerr=rate_avg_err / units.Hz, markersize=2)
ax.axhline(1, label='1 Hz line', color='red')
plt.minorticks_on()
ax.grid(which='major')
ax.grid(which='minor', alpha=0.25)
ax.set_title('Noise Trigger Rate vs. Trigger Threshold')
ax.set_xlabel(r"Threshold / $Vrms^2$")
ax.set_ylabel("rate [Hz]")
ax.legend(loc='upper right')
fig.tight_layout()
print('saving plot')
plt.savefig('plot')
print('plot saved')
plt.show()