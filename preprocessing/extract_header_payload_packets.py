import os
import numpy as np
import gc
from scapy.all import *

def extract_header_payload_packets(packets, filename, label):
    print(f"Extracting header+payload from {len(packets)} packets | File: {os.path.basename(filename)}")
    
    extracted_records = []
    MAX_LEN = 1500   # Fixed length - matches common practice in CBS-style papers
    
    count = 0
    for pkt in packets:
        try:
            raw = bytes(pkt)
            if len(raw) > MAX_LEN:
                record = raw[:MAX_LEN]
            else:
                record = raw + b'\x00' * (MAX_LEN - len(raw))
            
            extracted_records.append([int(b) for b in record])
            
            count += 1
            if count % 2000 == 0:
                print(f"  Processed {count} packets...")
        except:
            continue
    
    data_array = np.array(extracted_records, dtype=np.uint8)
    
    base_name = os.path.splitext(os.path.basename(filename))[0]
    output_dir = os.path.join(os.path.dirname(filename), "extracted")
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, f"{base_name}_extracted.npy")
    np.save(output_path, data_array)
    
    print(f"✓ Saved {data_array.shape[0]} records to {output_path}")
    
    del extracted_records, data_array
    gc.collect()
    
    return output_path