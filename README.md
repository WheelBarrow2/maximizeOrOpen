# Maximize Or Open (moro)
**For Linux Systems using X-Server (Ubuntu, Linux Mint etc)**

Maximize or Open is a python script which maximizes a given application, or opens it if it is not running. This application is designed to be used with a keybind.

**Example:** You only want CTRL+ALT+t to open a new terminal if there is none running. By keybinding CTRL+ALT+t too moro, CTRL+ALT+t will only open a new terminal if none is already running.

## Installation

You can either use the python script dierctly after installing the depdendencies, or you can download the .deb package or add an apt repository. 

**Download deb package**

[moro_0.1_all.deb](/moro_0.1_all.deb)

**Installing apt repository**
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6EC44EE9
sudo add-apt-repository "deb http://lofdev.net/repositories/ trusty main"
sudo apt update
sudo apt install moro
```

## Usage
```
moro [OPTIONS]
```

Where options are
* **-a** The application to be ran or maximized, see -l for a complete list of a compatible applications
* **-l** Lists a complete list of all compatible applications
* **-v** Toggles verbose mode
* **-n** If this is set, a new window will be opened regardless if one is already opened
* **-o** If this is set, override the supported application block.
* **-k** Lists all windows the scripts detects
* **-h** Prints usage

**Example 1:** I want to run gnome-terminal
```
python moro.py -a gnome-terminal
```

## Supported applications
At the moment, the supported applications are as follows:
* google-chrome-stable
* nemo
* spotify
* atom
* gnome-terminal

Please note that this script is written so that most applications are supported by default. If you use the **-o** flag, you can find which name to pass into **-a** by running the script with the **-k** flag. `python moro.py -k`

## Requirements
The requirements for this script is as follows:
* wmctrl v 1.07, Earlier versions might work, not tested

Both are available with apt-get.

## Features I'd like to implement
This is a list of features I'd like to implement. If I ever do however, I don't know
* If there are more than one window of an application, executing the script multiple times would tab through them

## FAQ

##### Does this run on Windows or Mac?
No, only Linux systems using X-Server, since it uses wmctrl.

## Other
##### Linux Mint keybidning
Open System Settings -> Keyboard -> Shortcuts -> Custom Shortcuts
Add a custom shortcut, where the Name is arbitrary. The Command should be `moro -a appToRun`. If we want to do this with google-chrome, we would have `moro -a google-chrome-stable`
![alt text](http://i.imgur.com/nGT0HNI.gif)
