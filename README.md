# MATLAB-to-Python Migration: Arc Attachment Movement Analysis

This repository contains a Python reimplementation of a MATLAB-based scientific project developed during PhD research in plasma physics.

The goal of the project is to analyze high-speed camera recordings of arc attachment motion on an anode surface and extract physical parameters such as velocity, displacement, restrike behavior, and measurement uncertainties.

---

## Original MATLAB Project

The original implementation was written in MATLAB and used high-speed recordings from a Photron FASTCAM SA-X2 system.

Key properties of the recording:

- Frame rate: 300,000 fps
- Resolution: 256 × 80 px
- Grayscale (8-bit)
- Total frames: 30,001

---

## Python Implementation

The MATLAB workflow has been fully translated into Python using NumPy, OpenCV, and Matplotlib.

The processing pipeline includes:

- Loading and reading high-speed video frames
- Detecting bright plasma attachment regions
- Computing attachment position along the anode surface
- Extracting extrema (maxima and minima)
- Calculating velocities and distances
- Estimating restrike periods
- Computing measurement uncertainties
- Visualizing results

---

## Dataset

This repository contains a trimmed version of the original recording (approximately first 30 seconds only) due to file size limitations.

The full dataset used in the original MATLAB analysis is not included.

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt

## Output

The program computes:

- Attachment velocity (m/s)
- Travel distance (mm)
- Restrike period (µs)
- Movement time (µs)
- Statistical uncertainties

Optionally, it also generates a visualization of the attachment motion.

---

## Notes

This project is a direct algorithmic translation of a MATLAB implementation.

Small numerical differences may occur due to using a trimmed video sample and differences between MATLAB and Python numerical handling.

---

## Requirements

- Python 3.9+
- NumPy
- OpenCV
- Matplotlib

---

## Author

Original MATLAB implementation: PhD research in plasma physics  
Python reimplementation: MATLAB → Python migration project for portfolio purposes
