import os
import numpy as np
import matplotlib.pyplot as plt
import SimpleITK as sitk
import nibabel as nib

# ==============================
# 1. SET PATH
# ==============================
mha_file = "Breast_MRI_0001_0000.mha"   # change this
output_folder = "nifti_output"
os.makedirs(output_folder, exist_ok=True)

# ==============================
# 2. LOAD MHA FILE
# ==============================
print("Loading MHA volume...")

img = sitk.ReadImage(mha_file)              # SimpleITK image
vol = sitk.GetArrayFromImage(img)           # NumPy array

# SimpleITK returns array as (D, H, W)
print("\n===== MRI VOLUME (MHA) =====")
print("Shape:", vol.shape)                  # (slices, height, width)
print("Spacing:", img.GetSpacing())         # (dx, dy, dz)
print("Origin:", img.GetOrigin())

# ==============================
# 3. NORMALIZE
# ==============================
vol = vol.astype(np.float32)
vmin, vmax = vol.min(), vol.max()
if vmax > vmin:
    vol = (vol - vmin) / (vmax - vmin)
else:
    vol = np.zeros_like(vol, dtype=np.float32)

# ==============================
# 4. VISUALIZE SLICES
# ==============================
print("Displaying slices...")

num_slices = vol.shape[0]
step = max(1, num_slices // 10)

for i in range(0, num_slices, step):
    plt.imshow(vol[i], cmap="gray")
    plt.title(f"Slice {i}")
    plt.axis("off")
    plt.show()

# ==============================
# 5. SAVE NUMPY
# ==============================
np.save("mri_volume_mha.npy", vol)
print("Saved NumPy volume as mri_volume_mha.npy!")

# ==============================
# 6. CONVERT TO NIFTI (OPTIONAL)
# ==============================
print("Converting MHA to NIfTI...")

nii_path = os.path.join(
    output_folder,
    os.path.splitext(os.path.basename(mha_file))[0] + ".nii.gz"
)
sitk.WriteImage(img, nii_path)  # direct MHA → NIfTI

print("Saved NIfTI:", nii_path)

# ==============================
# 7. LOAD NIFTI (VERIFY)
# ==============================
print("Loading NIfTI file for verification...")

nii = nib.load(nii_path)
nii_data = nii.get_fdata()

print("\n===== NIFTI DATA =====")
print("Shape:", nii_data.shape)

# visualize middle slice along last axis (assumed (H, W, D))
mid = nii_data.shape[2] // 2
plt.imshow(nii_data[:, :, mid], cmap="gray")
plt.title("Middle Slice (NIfTI)")
plt.axis("off")
plt.show()

print("\n✅ DONE: MHA volume ready for deep learning!")