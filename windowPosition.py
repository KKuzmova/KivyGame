import subprocess
import platform

def getDisplaySize():
    p = platform.platform()
    if p.startswith('Linux'):
        cp = subprocess.run('xdpyinfo', stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            universal_newlines=True)
        if cp.returncode == 0:
            lines = cp.stdout.split('\n')
            for line in lines:
                line = line.strip()
                if line.startswith('dimensions:'):
                    size = line.split()[1]
                    tokens = size.split('x')
                    try:
                        width = int(tokens[0])
                        height = int(tokens[1])
                        return (width, height)
                    except:
                        continue
    elif p.startswith('Windows'):
        cp = subprocess.run(['wmic', 'desktopmonitor', 'get',  'ScreenHeight,ScreenWidth'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        universal_newlines=True)
        if cp.returncode == 0:
            lines = cp.stdout.split('\n')
            for line in lines:
                tokens = line.split()
                try:
                    width = int(tokens[0])
                    height = int(tokens[1])
                    return (width, height)
                except:
                    continue

        # try another method
        cp = subprocess.run(['wmic', 'path', 'Win32_VideoController', 'get', 'CurrentHorizontalResolution,CurrentVerticalResolution'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            universal_newlines=True)
        if cp.returncode == 0:
            lines = cp.stdout.split('\n')
            for line in lines:
                tokens = line.split()
                try:
                    width = int(tokens[0])
                    height = int(tokens[1])
                    return (width, height)
                except:
                    continue
    # failed to get display size
    return (0,0)

dispSize = getDisplaySize()

if dispSize[0] !=0 and dispSize[1] != 0:
    from kivy.config import Config
    w = int(Config.get('graphics', 'width'))
    h = int(Config.get('graphics', 'height'))
    # print('Display Size:', dispSize)
    # print('App Width, Height:', w, h)
    Config.set('graphics', 'position', 'custom')
    Config.set('graphics', 'left', dispSize[0] - w)
    Config.set('graphics', 'top', dispSize[1] - h)
