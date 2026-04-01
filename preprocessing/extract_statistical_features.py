import os
import numpy as np
import gc

def extract_statistical_features(batch_name):
    normalized_dir = rf'D:\CBS_Project\CBS\{batch_name}\normalized'
    stats_dir = rf'D:\CBS_Project\CBS\{batch_name}\stats'
    os.makedirs(stats_dir, exist_ok=True)

    print(f"Extracting statistical features from batch: {batch_name}")

    for file in os.listdir(normalized_dir):
        if file.endswith('_normalized.npy'):
            path = os.path.join(normalized_dir, file)
            data = np.load(path).astype(np.float32)   # shape: (num_packets, 1500)

            # Statistical features per packet (6 features)
            stats = np.column_stack([
                data.mean(axis=1),      # mean
                data.std(axis=1),       # standard deviation
                data.min(axis=1),       # min
                data.max(axis=1),       # max
                np.percentile(data, 25, axis=1),   # 25th percentile
                np.percentile(data, 75, axis=1)    # 75th percentile
            ])

            out_path = os.path.join(stats_dir, file.replace('_normalized.npy', '_stats.npy'))
            np.save(out_path, stats)
            
            print(f"  ✓ Stats for {file}: {stats.shape} → saved to stats folder")
            
            del data, stats
            gc.collect()

    print(f"Statistical features extraction completed for {batch_name}\n")

# Example usage - run this after normalization
# extract_statistical_features("test_small")
# extract_statistical_features("batch1_chat_email")
if __name__ == "__main__":
    batch_name = input("Enter batch name (e.g. test_small or batch1_chat_email): ")
    extract_statistical_features(batch_name)