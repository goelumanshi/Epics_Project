import os
import numpy as np
import gc
from sklearn.utils import shuffle

print("=== Local Subsampling + Global Shuffle (15%) ===")

data_path = r'D:\CBS_Project\CBS\final_processed'
output_path = r'D:\CBS_Project\CBS\final_processed_shuffled'

os.makedirs(output_path, exist_ok=True)

# Load data
print("Loading data...")
X_packet = np.load(os.path.join(data_path, 'X_packet.npy'))
X_stats = np.load(os.path.join(data_path, 'X_stats.npy'))
y = np.load(os.path.join(data_path, 'y_labels.npy'))

print(f"Original shapes: X_packet={X_packet.shape}, X_stats={X_stats.shape}, y={y.shape}")

# Global shuffle
print("Performing global shuffle...")
X_packet, X_stats, y = shuffle(X_packet, X_stats, y, random_state=42)

# Subsampling
sample_fraction = 0.15   # 15% sampling
n_samples = int(len(X_packet) * sample_fraction)

print(f"Subsampling to {sample_fraction*100}% ({n_samples:,} samples)...")

indices = np.random.choice(len(X_packet), n_samples, replace=False)

X_packet = X_packet[indices]
X_stats = X_stats[indices]
y = y[indices]

print(f"Final shapes after subsampling:")
print(f"  X_packet : {X_packet.shape}")
print(f"  X_stats  : {X_stats.shape}")
print(f"  y        : {y.shape}")

# Save
print("Saving files...")
np.save(os.path.join(output_path, 'X_packet.npy'), X_packet.astype(np.float32))
np.save(os.path.join(output_path, 'X_stats.npy'), X_stats.astype(np.float32))
np.save(os.path.join(output_path, 'y_labels.npy'), y)

print(f"\n✅ Saved to: {output_path}")
print("You can now zip this folder ('final_processed_shuffled') and upload to Google Drive.")

gc.collect()