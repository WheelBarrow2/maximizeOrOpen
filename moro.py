import os
import sys
import getopt


def inAppList(app, appListLocal):
    if len([item for item in appListLocal if item[0] == app]) > 0:
        return True
    else:
        return False


def idByName(app, appListLocal):
    for a in appListLocal:
        if a[0] == app:
            return a[1]
    return ""

try:
    opts, args = getopt.getopt(sys.argv[1:], "ha:nvlok")
except:
    print('Error, please see -h')
    sys.exit()

supportedApps = ['google-chrome-stable', 'nemo', 'spotify', 'atom',
                 'gnome-terminal']

helpString = ('moro.py 1.0\n'
              'Usage: python moro.py [OPTION]...\n'
              'Actions:\n'
              '-a \t The application to be ran or maximized, see -l for a comp'
              'lete list of compatible applications\n'
              '-l \t Lists a complete list of all compatible applications\n'
              '-v \t Toggles verbose mode \n'
              '-n \t If this is set, a new window will be opened regardless '
              'if one is already opened \n'
              '-o \t Overrides the suported applications list. This might be b'
              'uggy \n'
              '-k \t Lists all windows the script detects\n'
              '-h \t Shows this information \n'
              'Requirements:\n'
              'Screen v 4.0 (GNU), Earlier versions might work, not tested\n'
              'wmctrl v 1.07, Earlier versions might work, not tested')
# State Variables
app = 'none'
new = False
verbose = False
notRun = False
overrideSupported = False

for o, a in opts:
    if o == '-a':
        app = a.lower()
    elif o == '-n':
        new = True
    elif o == '-v':
        verbose = True
    elif o == '-l':
        notRun = True
        print('Supported Applications: ')
        for sA in supportedApps:
            print(sA)
    elif o == '-o':
        overrideSupported = True
    elif o == '-k':
        appList = []
        wmCtrlListRaw = os.popen('wmctrl -l').read()
        wmCtrlList = wmCtrlListRaw.split('\n')
        del wmCtrlList[len(wmCtrlList)-1]
        for appInList in wmCtrlList:
            appId = appInList[:10]
            response = os.popen('xprop -id '+appId+' -notype WM_CLASS').read()
            cList = []
            i = 0
            for c in response:
                if c == '"':
                    cList.append(i)
                i = i + 1
            appList.append((response[cList[0]+1:cList[1]], appId))
        print appList
        sys.exit()
    elif o == '-h':
        notRun = True
        app = 'help'
        print(helpString)

if app not in supportedApps and notRun is False and overrideSupported is False:
    print("Error, please use -h for help")
    sys.exit()
elif new is False:
    appList = []
    wmCtrlListRaw = os.popen('wmctrl -l').read()
    wmCtrlList = wmCtrlListRaw.split('\n')
    del wmCtrlList[len(wmCtrlList)-1]
    for appInList in wmCtrlList:
        appId = appInList[:10]
        response = os.popen('xprop -id '+appId+' -notype WM_CLASS').read()
        cList = []
        i = 0
        for c in response:
            if c == '"':
                cList.append(i)
            i = i + 1
        appList.append((response[cList[0]+1:cList[1]], appId))
    if verbose:
        print('App list:')
        print(appList)
    if app in supportedApps or overrideSupported is True:
        if inAppList(app, appList):
            os.system('wmctrl -i -a '+idByName(app, appList))
            if verbose:
                print("Maximizing " + app)
        elif app == 'google-chrome-stable' and inAppList('google-chrome',
                                                         appList):
            os.system('wmctrl -i -a '+idByName('google-chrome', appList))
            if verbose:
                print("Maximizing google-chrome-stable")
        else:
            os.system('screen -d -m ' + app)
            if verbose:
                print("Starting new " + app)
elif new is True:
    if app in supportedApps or overrideSupported is True:
        os.system('screen -d -m ' + app)
        if verbose:
            print("Starting new " + app + ". New flag was true")
