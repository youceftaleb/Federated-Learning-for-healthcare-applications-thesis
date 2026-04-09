import os
import pydicom
import numpy as np
import matplotlib.pyplot as plt
import dicom2nifti
import nibabel as nib

# ==============================
# 1. SET PATH
# ==============================
dicom_folder = "1.3.6.1.4.1.14519.5.2.1.108969460987830173394456969708181753586"        # change this for each file
output_folder = "nifti_output"

os.makedirs(output_folder, exist_ok=True)

# ==============================
# 2. LOAD DICOM FILES
# ==============================
print("Loading DICOM files...")

slices = []
for file in os.listdir(dicom_folder):
    if file.endswith(".dcm"):
        path = os.path.join(dicom_folder, file)
        ds = pydicom.dcmread(path)
        slices.append(ds)

print(f"Loaded {len(slices)} slices")

# ==============================
# 3. SORT SLICES (CRITICAL)
# ==============================
try:
    slices.sort(key=lambda x: float(x.ImagePositionPatient[2]))
except:
    slices.sort(key=lambda x: float(x.SliceLocation))

print("Slices sorted")

# ==============================
# 4. BUILD 3D VOLUME
# ==============================
images = np.stack([s.pixel_array for s in slices])

print("\n===== MRI VOLUME =====")
print("Shape:", images.shape)  # (slices, height, width)

# ==============================
# 5. NORMALIZE
# ==============================
images = images.astype(np.float32)
images = (images - images.min()) / (images.max() - images.min())

# ==============================
# 6. VISUALIZE SLICES
# ==============================
print("Displaying slices...")

for i in range(0, images.shape[0], max(1, images.shape[0] // 10)):
    plt.imshow(images[i], cmap='gray')
    plt.title(f"Slice {i}")
    plt.axis("off")
    plt.show()

# ==============================
# 7. SAVE NUMPY
# ==============================
np.save("mri_volume.npy", images)
print("Saved NumPy volume!")

# ==============================
# 8. CONVERT TO NIFTI
# ==============================
print("Converting to NIfTI...")

dicom2nifti.convert_directory(
    dicom_folder,
    output_folder
)

print("Conversion done!")

# ==============================
# 9. LOAD NIFTI (VERIFY)
# ==============================
print("Loading NIfTI file...")

# find generated .nii file
nii_file = None
for file in os.listdir(output_folder):
    if file.endswith(".nii") or file.endswith(".nii.gz"):
        nii_file = os.path.join(output_folder, file)
        break

if nii_file:
    nii = nib.load(nii_file)
    nii_data = nii.get_fdata()

    print("\n===== NIFTI DATA =====")
    print("Shape:", nii_data.shape)

    # visualize middle slice
    mid = nii_data.shape[2] // 2
    plt.imshow(nii_data[:, :, mid], cmap='gray')
    plt.title("Middle Slice (NIfTI)")
    plt.axis("off")
    plt.show()
else:
    print("No NIfTI file found!")

print("\n✅ DONE: MRI ready for deep learning!")