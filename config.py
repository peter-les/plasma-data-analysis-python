# config.py

from pathlib import Path

VIDEO_PATH = Path("data/900mbar_300A.avi")

# MATLAB:
# N0=1;
# Nf=30000;

N0 = 1
NF = 30000

# MATLAB:
# faktor=0.128205128;

FACTOR = 0.128205128

# MATLAB:
# riadok=86+1;

ROW = 87

# MATLAB:
# down=75;

THRESHOLD = 75

# MATLAB:
# zaciatok=86;
# koniec=185+1;

START_PIXEL = 86
END_PIXEL = 186

# 300000 fps

FRAME_TIME_US = 10.0 / 3.0

ANODE_OFFSET_MM = 14.0

GRAPHS = True