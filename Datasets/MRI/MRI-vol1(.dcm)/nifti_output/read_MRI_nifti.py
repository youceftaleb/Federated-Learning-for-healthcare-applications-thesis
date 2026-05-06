import os
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt

# =========================
# 1) PATH TO NIFTI FILE
# =========================
nii_path = "503_ph3ax_dynamic.nii.gz"   # change if needed

# =========================
# 2) LOAD NIFTI
# =========================
img = nib.load(nii_path)
data = img.get_fdata()

print("NIfTI loaded successfully")
print("Shape:", data.shape)
print("Data type:", data.dtype)
print("Affine:\n", img.affine)

# =========================
# 3) CLEAN / NORMALIZE
# =========================
data = np.nan_to_num(data)
data = data.astype(np.float32)

mn, mx = data.min(), data.max()
if mx > mn:
    data = (data - mn) / (mx - mn)
else:
    data = np.zeros_like(data, dtype=np.float32)

print("Normalized shape:", data.shape)
print("Min:", data.min(), "Max:", data.max())

# =========================
# 4) VISUALIZE ALL SLICES
# =========================
n_slices = data.shape[2] if data.ndim == 3 else data.shape[-1]
cols = 6
rows = int(np.ceil(n_slices / cols))

fig, axes = plt.subplots(rows, cols, figsize=(18, 3 * rows))
axes = np.array(axes).reshape(-1)

for i in range(rows * cols):
    ax = axes[i]
    ax.axis("off")
    if i < n_slices:
        ax.imshow(data[:, :, i], cmap="gray")
        ax.set_title(f"Slice {i}", fontsize=8)

plt.tight_layout()
plt.savefig("all_slices_grid.png", dpi=200, bbox_inches="tight")
plt.show()

# =========================
# 5) VIEW MIDDLE SLICE
# =========================
mid = n_slices // 2
plt.figure(figsize=(6, 6))
plt.imshow(data[:, :, mid], cmap="gray")
plt.title(f"Middle Slice {mid}")
plt.axis("off")
plt.show()

# =========================
# 6) SAVE AS NUMPY
# =========================
np.save("mri_volume.npy", data)
print("Saved: mri_volume.npy")

# =========================
# 7) PREPARE FOR 3D CNN
# =========================
volume_3d = np.expand_dims(data, axis=0)   # (1, H, W, D) if data is 3D
volume_3d = np.expand_dims(volume_3d, axis=0)  # (1, 1, H, W, D)

print("3D CNN input shape:", volume_3d.shape)

# =========================
# 8) OPTIONAL: SHOW CENTRAL SLICES IN 3 PLANES
# =========================
if data.ndim == 3:
    h, w, d = data.shape
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    axs[0].imshow(data[h // 2, :, :], cmap="gray")
    axs[0].set_title("Sagittal")
    axs[0].axis("off")

    axs[1].imshow(data[:, w // 2, :], cmap="gray")
    axs[1].set_title("Coronal")
    axs[1].axis("off")

    axs[2].imshow(data[:, :, d // 2], cmap="gray")
    axs[2].set_title("Axial")
    axs[2].axis("off")

    plt.tight_layout()
    plt.show()