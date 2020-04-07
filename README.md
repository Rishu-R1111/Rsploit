# Rsploit 
----------------by RISHU RIKSHT

<h4 align="center">Exploitation Framework for ATtiny85 HID Attacks</h4>

<p align="center">
	<img src="https://img.shields.io/badge/Python-3-brightgreen.svg?style=plastic">
	<img src="https://img.shields.io/badge/ATtiny85-red.svg?style=plastic">
	<img src="https://img.shields.io/badge/Exploitation-red.svg?style=plastic">
</p>



<p align="center">
  <br>
  <b>Available in</b>
  <br>
  <img src="https://i.imgur.com/1wJVDV5.png">
</p>

Rsploit is an Exploitation Framework for Attacks using ATtiny85 HID Devices such as Digispark USB Development Board, Rsploit generates Arduino IDE Compatible (.ino) Scripts based on User Input and then Starts a Listener in Metasploit-Framework if Required by the Script, in Summary : Automatic Script Generation with Automated msfconsole.

<p align="center">
<img src="https://i.imgur.com/D8peKaN.jpg" width="15%" height="auto">
</p>

## Features

* TODO : Add Linux and OSX Scripts

### Windows

#### Data Exfiltration

* Extract all WiFi Passwords and Uploads an XML to SFTP Server |  : 

* Extract Network Configuration Information of Target System and Uploads to SFTP Server | :

[![Youtube](https://i.imgur.com/BxvJpUI.png)]


* Extract Passwords and Other Critical Information using Mimikatz and Uploads to SFTP Server | : 

#### Reverse Shells

* Get Reverse Shell by Abusing Microsoft HTML Apps (mshta) |  : 

[![Youtube](https://i.imgur.com/57JP6DJ.png)]


* Get Reverse Shell by Abusing Certification Authority Utility (certutil)
* Get Reverse Shell by Abusing Windows Script Host (csript)
* Get Reverse Shell by Abusing Windows Installer (msiexec)
* Get Reverse Shell by Abusing Microsoft Register Server Utility (regsvr32)

#### Miscellaneous

* Change Wallpaper of Target Machine |  : 

[![Youtube](https://i.imgur.com/qujjnuF.png)]

* Make Windows Unresponsive using a .bat Script (100% CPU and RAM usage)

[![Youtube](https://i.imgur.com/XlYfUT6.png)]

* Drop and Execute a File of your Choice, a ransomware maybe? ;)
* Disable Windows Defender Service on Target Machine

[![Youtube](https://i.imgur.com/4ghSjXO.png)]

## Tested on

* Kali Linux 2019.2
* BlackArch Linux

## Dependencies

Rsploit Depends upon 4 Packages which are Generally Pre-installed in Major Pentest OS : 

* Metasploit-Framework
* Python 3
* SFTP
* PHP

If you think I should still make an Install Script, Open an issue. 

## Installation / Usage

#### BlackArch Linux

```bash
pacman -S Rsploit
```

#### Kali Linux

```bash
git clone https://github.com/thewhiteh4t/Rsploit.git 
cd Rsploit
python3 Rsploit.py 
```
