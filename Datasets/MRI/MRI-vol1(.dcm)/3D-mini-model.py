import numpy as np
import torch
import torch.nn as nn
from scipy.ndimage import zoom

# ==============================
# 1. LOAD SAVED VOLUME
# ==============================
data = np.load("mri_volume.npy")  # shape: (512, 512, 174)
print("Loaded shape:", data.shape)

# ==============================
# 2. TRANSPOSE → (D, H, W)
# ==============================
data = np.transpose(data, (2, 0, 1))  # (174, 512, 512)
print("After transpose:", data.shape)

# ==============================
# 3. DOWNSAMPLE (CRITICAL)
# Target: (64, 128, 128) — safe for CPU + GPU
# ==============================
target = (64, 128, 128)
zoom_factors = (
    target[0] / data.shape[0],
    target[1] / data.shape[1],
    target[2] / data.shape[2],
)
data_small = zoom(data, zoom_factors, order=1)  # bilinear
print("After downsampling:", data_small.shape)  # (64, 128, 128)

# ==============================
# 4. PREPARE TENSOR → (1, 1, D, H, W)
# ==============================
x = torch.tensor(data_small, dtype=torch.float32)
x = x.unsqueeze(0).unsqueeze(0)  # (1, 1, 64, 128, 128)
print("Tensor shape (model input):", x.shape)

# ==============================
# 5. MINI 3D CNN (unchanged)
# ==============================
class Mini3DCNN(nn.Module):
    def __init__(self, num_classes=2):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv3d(1, 8, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool3d(2),             # → (1, 8, 32, 64, 64)

            nn.Conv3d(8, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool3d(2),             # → (1, 16, 16, 32, 32)

            nn.Conv3d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool3d(1),     # → (1, 32, 1, 1, 1)

            nn.Flatten(),                # → (1, 32)
            nn.Linear(32, num_classes)   # → (1, 2)
        )

    def forward(self, x):
        return self.net(x)

# ==============================
# 6. RUN FORWARD PASS
# ==============================
model = Mini3DCNN(num_classes=2)
model.eval()

with torch.no_grad():
    output = model(x)

print("\n===== OUTPUT =====")
print("Raw logits:", output)
print("Predicted class:", torch.argmax(output, dim=1).item())
print("\n✅ 3D Mini Model ran successfully!")