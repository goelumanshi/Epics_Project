import os
import numpy as np
import gc

batch_name = input("Enter batch name (e.g. batch2_skype_youtube): ").strip()

input_dir = rf'D:\CBS_Project\CBS\{batch_name}\extracted'
output_dir = rf'D:\CBS_Project\CBS\{batch_name}\normalized'

os.makedirs(output_dir, exist_ok=True)

print(f"Normalizing files from batch: {batch_name}")

for file in os.listdir(input_dir):
    if file.endswith('_extracted.npy'):
        path = os.path.join(input_dir, file)
        data = np.load(path).astype(np.float32) / 255.0
        out_path = os.path.join(output_dir, file.replace('_extracted', '_normalized'))
        np.save(out_path, data)
        print(f"Normalized {file} → shape {data.shape}")
        del data
        gc.collect()

print(f"Normalization completed for {batch_name}")