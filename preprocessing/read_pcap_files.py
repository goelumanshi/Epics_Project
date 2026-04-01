import os

def read_pcap_files():
    root_dir = r'D:\CBS_Project\CBS\batch4_hangouts_voip'   # Your test folder
    
    file_name_list_full_path = []
    file_name_list = []
    file_name_dict = {}
    
    print("=== Starting read_pcap_files ===")
    print(f"Looking for pcap files in: {root_dir}")
    
    # List all files
    for path in os.listdir(root_dir):
        full_path = os.path.join(root_dir, path)
        if os.path.isfile(full_path) and (path.endswith(".pcap") or path.endswith(".pcapng")):
            print(f"Found file: {path}")
            file_name_list_full_path.append(full_path)
            file_name_list.append(path)
    
    print(f"Total pcap files found: {len(file_name_list)}")
    
    # Assign categories (simplified from your earlier snippet)
        # Improved labeling based on filename (closer to preprocessing-traffic-label.py and dataset)
    for i in range(len(file_name_list)):
        fname = file_name_list[i].lower()
        full_path = file_name_list_full_path[i]
        
        if "vpn" in fname:
            if any(x in fname for x in ["chat", "aim", "icq", "gmail", "facebook_chat", "skype_chat", "hangouts_chat"]):
                category = 1   # VPN-Chat
            elif any(x in fname for x in ["email"]):
                category = 2   # VPN-Email
            elif any(x in fname for x in ["audio", "voip", "skype_audio", "hangouts_audio"]):
                category = 3   # VPN-VoIP/Audio
            elif any(x in fname for x in ["video", "netflix", "vimeo", "youtube", "facebook_video"]):
                category = 4   # VPN-Streaming/Video
            elif any(x in fname for x in ["ftp", "sftp", "scp", "file"]):
                category = 5   # VPN-File Transfer
            else:
                category = 6   # Other VPN
        else:
            if any(x in fname for x in ["chat", "aim", "icq", "gmail", "facebook_chat"]):
                category = 7   # NonVPN-Chat
            elif any(x in fname for x in ["email"]):
                category = 8   # NonVPN-Email
            elif any(x in fname for x in ["audio", "voip", "skype_audio"]):
                category = 9   # NonVPN-VoIP
            elif any(x in fname for x in ["video", "netflix", "vimeo", "youtube"]):
                category = 10  # NonVPN-Streaming
            elif any(x in fname for x in ["ftp", "sftp", "scp"]):
                category = 11  # NonVPN-File Transfer
            else:
                category = 12  # Other NonVPN
        
        file_name_dict[full_path] = category
        print(f"Assigned category {category} to {file_name_list[i]}")
    
    # Try to call the next function if it exists
    try:
        from load_pcap_datatype import load_pcap_datatype
        print("Calling load_pcap_datatype...")
        load_pcap_datatype(file_name_dict)   # Adjust arguments if needed
    except ImportError:
        print("load_pcap_datatype.py not found or import failed - this is expected for now")
    except Exception as e:
        print(f"Error in load_pcap_datatype: {e}")
    
    print("=== read_pcap_files finished ===")
    return file_name_dict

if __name__ == "__main__":
    read_pcap_files()