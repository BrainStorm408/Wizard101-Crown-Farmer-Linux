```ascii
██╗    ██╗██╗███████╗ █████╗ ██████╗ ██████╗ ███████╗ ██╗ ██████╗  ██╗     ██████╗██████╗  ██████╗ ██╗    ██╗███╗   ██╗    ███████╗ █████╗ ██████╗ ███╗   ███╗███████╗██████╗ 
██║    ██║██║╚══███╔╝██╔══██╗██╔══██╗██╔══██╗██╔════╝███║██╔═████╗███║    ██╔════╝██╔══██╗██╔═══██╗██║    ██║████╗  ██║    ██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██╔══██╗
██║ █╗ ██║██║  ███╔╝ ███████║██████╔╝██║  ██║███████╗╚██║██║██╔██║╚██║    ██║     ██████╔╝██║   ██║██║ █╗ ██║██╔██╗ ██║    █████╗  ███████║██████╔╝██╔████╔██║█████╗  ██████╔╝
██║███╗██║██║ ███╔╝  ██╔══██║██╔══██╗██║  ██║╚════██║ ██║████╔╝██║ ██║    ██║     ██╔══██╗██║   ██║██║███╗██║██║╚██╗██║    ██╔══╝  ██╔══██║██╔══██╗██║╚██╔╝██║██╔══╝  ██╔══██╗
╚███╔███╔╝██║███████╗██║  ██║██║  ██║██████╔╝███████║ ██║╚██████╔╝ ██║    ╚██████╗██║  ██║╚██████╔╝╚███╔███╔╝██║ ╚████║    ██║     ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝ ╚═╝ ╚═════╝  ╚═╝     ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
               by Lucas Clark                                                                                                 Version 1.0                                                                                                                                                               
```

![MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)
![Chrome](https://img.shields.io/badge/Google%20Chrome-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### A program that uses selenium to complete the online trivia for wizard101 accounts and collect crowns.

```
- Use it at your own risk, Kingsisle may ban your account
```

## Installation

1. You will require latest [python](https://wiki.archlinux.org/title/python) and pip. Download using your package manager.
2. Using pip, install the requirements using this command:
   `pip install -r requirements.txt`
3. [Chromium](https://wiki.archlinux.org/title/chromium) or Chrome will have to be installed. Download using your package manager.
4. [ffmpeg](https://wiki.archlinux.org/title/FFmpeg) will have to be installed. Use package manager.
4. In project directory, run setup.py which will ask for account username and password or you can manually set it by editing the accounts.json.example. \
Then when finished editing, remove the .example.
4. ProtonVPN-cli will have to be installed. This is complicated and will have a longer explanation. \
Click this [link](https://github.com/ProtonVPN/linux-cli) and follow instructions based on your distro. \
You will have to download all dependencies such as: \
[Proton VPN NM Library](https://github.com/ProtonVPN/protonvpn-nm-lib) \
[Proton API Python Client](https://github.com/ProtonMail/proton-python-client) \
Which all have their own dependencies which they explain on how to install. \
Once you have their dependencies and their zip or tar.gz file. Extract the compressed file and open the terminal in its main directory. \
Run the command python setup.py install. Do this with all proton zips downloaded. If you get an error installing due to write access run sudo. \
Once all is functional you should be able to run command protonvpn-cli c -r which gives a random vpn connection and disconnect using protonvpn-cli d. \
If you have an issue using protonvpn-cli c -r saying an unknown issue occurred. Try installing network-manager-applet and restarting then trying it. \
This is the process I went through to get protonvpn-cli to work on arch. Others experiences will vary.
```
ProtonVPN is used to negate IP blockage from Recaptcha.
```

## Note

Windows is not supported. Possibly will make a script for windows. No idea how I will add vpn rotation.

If any issues occur. Relaunch code and try again.

Headless can be disabled in browser.py and just comment out or remove the headless option