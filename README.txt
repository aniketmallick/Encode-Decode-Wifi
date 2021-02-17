# enc-dec-wifi

Restricted Data Access Programs: Developed Linux-based programs to communicate confidential information over the network encrypted using 
unique keys and advanced XOR algorithms. Technology Used: Python
The target audience being the organizations which communicate confidential information over intranet and internet,
this software aims to facilitate data access only to specific network users ensuring an increased layer of security,
even on data leakage.

The skills demanded by the project included:
->Basic information about Network Protocols and router hardware for retrieving
network's Unique Device Identifier, etc.
->Cryptography required for encrypting the messages sent.Here I modified the XOR encryption and used it for encryption.
->Python Programming required for making encrypt and decrypt programs.

The overview of the project can be described as:
It encrypts the network information in the way that even if the message is intercepted would be not readable or decryptable by the person. 
Even if the same message is sent twice it may not be same string transmitted. 
This increases the data security as it won't show any type of redundancy of the encrypted text making it impossible for the malicious 
end to decipher new text through known encrypted and actual texts. This technology is router specific.It uses basic router information 
like BSSID, wifiname, etc to encrypt the text.This increases data security within an organisation.