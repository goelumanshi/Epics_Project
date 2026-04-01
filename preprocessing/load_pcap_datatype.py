import os
from datetime import datetime
import gc
from scapy.all import rdpcap, load_layer
from extract_header_payload_packets import extract_header_payload_packets

# Try to import other modules (they may not exist yet)
try:
    from Break_Data_File import Break_Data_File
except ImportError:
    print("Break_Data_File.py not found - skipping file breaking")
    Break_Data_File = None

def get_file_size(filepath, unit='bytes'):
    size = os.path.getsize(filepath)
    if unit.lower() == 'mb':
        return size / (1024 * 1024)
    return size

def load_pcap_datatype(file_name_dict):
    print("=== Starting load_pcap_datatype (safe version) ===")
    
    # Load Scapy layers (this was failing before)
    try:
        load_layer("tls")
        load_layer("ssl")
        print("Scapy TLS/SSL layers loaded")
    except Exception as e:
        print(f"Warning: Could not load TLS/SSL layers: {e}")
    
    extracted_results = []
    
    for k, v in file_name_dict.items():
        print(f"\nProcessing file: {os.path.basename(k)} | Label: {v}")
        
        # Skip very large files
        size_mb = get_file_size(k, 'mb')
        if size_mb > 500:  # Skip anything over 500 MB for now
            print(f"Skipping large file ({size_mb:.1f} MB)")
            continue
        
        try:
            # For small test files, read directly (no breaking for now)
            print(f"Reading packets at {datetime.now().time()}")
            packets = rdpcap(k)
            print(f"Read {len(packets)} packets at {datetime.now().time()}")
            
            # Call the core extraction function (this is what we really need)
            working_dir = os.path.splitext(os.path.basename(k))[0]
            extracted = extract_header_payload_packets(packets, k, v)
            extracted_results.append(extracted)
            
            print(f"Successfully extracted header+payload for {os.path.basename(k)}")
            
            # Memory cleanup - critical for your 16GB RAM
            del packets
            gc.collect()
            
        except Exception as e:
            print(f"Error processing {os.path.basename(k)}: {e}")
            gc.collect()
    
    print("=== load_pcap_datatype finished ===")
    return extracted_results