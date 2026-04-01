#  Dataset Information

##  Dataset Used

This project uses the **ISCX VPN-NonVPN 2016 Dataset** provided by the Canadian Institute for Cybersecurity.

🔗 Dataset Link: [link](https://www.unb.ca/cic/datasets/vpn.html)

---

##  Description

The dataset contains real network traffic data including both:

* **VPN (Encrypted Traffic)**
* **Non-VPN (Normal Traffic)**

It includes multiple application categories such as:

* Chat
* Email
* Streaming
* File Transfer
* VoIP

The dataset is widely used for research in:

* Network Traffic Classification
* Cybersecurity
* Intrusion Detection Systems

---

##  Data Format

* Packet capture files (**PCAP**)
* Extracted features (CSV format after preprocessing)

---
##  Note

* The dataset is **not included in this repository** due to its large size.
* Please download it manually from the official source.

---

##  Citation

If you use this dataset, please cite:

> Canadian Institute for Cybersecurity (CIC), ISCX VPN-NonVPN Dataset, 2016.

---

## Additional Info

* Data imbalance exists across classes
* Preprocessing is required before training
* Suitable for both binary and multi-class classification tasks
