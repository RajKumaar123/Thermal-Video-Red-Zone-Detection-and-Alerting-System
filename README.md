
# Thermal Video Red Zone Detection and Alerting System

This project is designed to automatically detect and track areas of high red intensity in thermal or surveillance videos. These red zones often indicate rising temperatures, heat leaks, or potential fire hazards. The system uses Python with OpenCV and NumPy to process each video frame and alert when the intensity of red crosses a certain threshold.

## What This Project Does

- Reads and analyzes video frame-by-frame to detect areas with high red intensity.
- Marks and saves frames where red pixels are found in excess, which can signal thermal anomalies.
- Logs alerts with timestamps whenever the red intensity exceeds a specified limit.
- Creates a visual plot showing how red intensity changes over time in the video.
- Outputs an annotated video, making it easier to review where red zones occurred.

## Why This Project Matters

This system is useful for:
- Monitoring industrial equipment for overheating.
- Detecting heat leaks or fire-prone areas in buildings or plants.
- Analyzing thermal surveillance footage for unusual patterns.

It can help improve safety by providing early warnings before a situation becomes dangerous.

## Key Features

- Simple and clear logic using Python (OpenCV, NumPy, Matplotlib)
- Customizable red intensity threshold
- Visual feedback through saved images, plots, and videos
- Jupyter Notebook version included for better understanding and step-by-step experimentation

## How to Use

1. Place your video in the input directory.
2a. Run the notebook `Vcvision04.ipynb` to work on video. Video should be kept in 'Thermal Video' Folder.
2b. Run the notebook `cvision04.ipynb`to work on Image. Image should be kept in 'Thermal Image' Folder.
3. Review the output video and alert frames in the output folder.
4. Use the plotted chart to see how red activity changed over time.

## 🔧 New Feature: Synthetic Image Generator

- Added `app.py` to generate synthetic thermal images for testing.
- Enhanced image analysis via scripts inside `Thermal Image/`.
- Output is saved in `OutputImages/`.

## Synthetic Thermal Image Generator (app.py)
This script generates synthetic thermal images of industrial pipeline systems using a guided prompt-based image generation model. It's designed to help simulate different heat intensity zones (red, yellow, green, blue) for testing and analysis.

✅ Features
Prompts simulate varying thermal conditions across frames
Supports GPU for faster image generation
Generates realistic heatmaps using a reference image
Automatically saves generated images to the output folder