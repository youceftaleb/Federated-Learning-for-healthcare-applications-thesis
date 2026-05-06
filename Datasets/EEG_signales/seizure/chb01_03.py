import mne
import numpy as np
import matplotlib.pyplot as plt

# ==============================
# 1. LOAD EDF FILE
# ==============================
file_path = "chb01_03.edf"

raw = mne.io.read_raw_edf(file_path, preload=True)

print("\n===== BASIC INFO =====")
print(raw)
print("\nChannels:", raw.ch_names)
print("Sampling rate:", raw.info['sfreq'])

# ==============================
# 2. FIX DUPLICATE CHANNEL NAMES
# ==============================
raw.rename_channels(lambda x: x.strip())
raw.set_montage("standard_1020", on_missing='ignore')

# ==============================
# 3. FILTER SIGNAL (VERY IMPORTANT)
# ==============================
raw.filter(l_freq=0.5, h_freq=40)

# ==============================
# 4. INTERACTIVE VIEWER
# ==============================
print("\nOpening EEG viewer...")
raw.plot(n_channels=10, duration=10, scalings='auto')

# ==============================
# 5. EXTRACT NUMPY DATA
# ==============================
data, times = raw.get_data(return_times=True)

print("\n===== NUMPY DATA =====")
print("Shape:", data.shape)  # (channels, time)
print("Time vector:", times.shape)

# ==============================
# 6. SAVE NUMPY FILES
# ==============================
np.save("eeg_data.npy", data)
np.save("eeg_times.npy", times)

print("Saved EEG as NumPy!")

# ==============================
# 7. SEGMENT INTO WINDOWS
# ==============================
fs = int(raw.info['sfreq'])   # sampling frequency
window_sec = 5                # 5 seconds window
window_size = fs * window_sec

segments = []

for start in range(0, data.shape[1] - window_size, window_size):
    segment = data[:, start:start + window_size]
    segments.append(segment)

segments = np.array(segments)

print("\n===== SEGMENTS =====")
print("Segments shape:", segments.shape)
# (num_segments, channels, time_steps)

# Save segments
np.save("eeg_segments.npy", segments)

# ==============================
# 8. PLOT ONE SEGMENT (DEBUG)
# ==============================
plt.figure()
plt.plot(segments[0][0])  # first segment, first channel
plt.title("Example EEG Segment")
plt.show()

# ==============================
# 9. OPTIONAL: LABELING (MANUAL)
# ==============================
# Example seizure interval (you must get from summary file)
seizure_intervals = [
    (1000, 1100),  # seconds (example)
]

labels = []

for i in range(len(segments)):
    start_time = i * window_sec
    end_time = start_time + window_sec

    label = 0  # normal
    for s_start, s_end in seizure_intervals:
        if (start_time < s_end) and (end_time > s_start):
            label = 1  # seizure
            break

    labels.append(label)

labels = np.array(labels)

print("\n===== LABELS =====")
print(labels.shape)

np.save("eeg_labels.npy", labels)

print("\n✅ DONE: Data ready for ML!")