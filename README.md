# Thermal Video Red Zone Detection and Alerting System

This project is designed to automatically detect and track areas of high red intensity in thermal or surveillance videos. These red zones often indicate rising temperatures, heat leaks, or potential fire hazards. The system uses Python with OpenCV and NumPy to process each video frame and alert when the intensity of red crosses a certain threshold.

---

## What This Project Does

- Analyzes video frame-by-frame to detect areas with high red intensity.
- Flags and saves frames with excessive red pixels, signaling thermal anomalies.
- Logs alerts with timestamps when red intensity exceeds a limit.
- Generates visual plots of red pixel activity over time.
- Outputs an annotated video for easier review of red zones.

---

## Why This Project Matters

This system is useful for:

- Monitoring industrial equipment for overheating.
- Detecting heat leaks or fire-prone zones in buildings or plants.
- Analyzing thermal surveillance footage for early signs of danger.

**It enhances safety by providing early warnings of heat-related anomalies.**

---

## Key Features

- Written in Python using OpenCV, NumPy, and Matplotlib.
- Customizable red intensity threshold.
- Saves alerts, annotated video, and keyframes automatically.
- Includes a Jupyter Notebook version for step-by-step analysis.
- Easy to adapt for different video or image sources.

---

## How to Use

1. **Prepare your data:**
   - Place your **video** in the `Thermal Video/` folder.
   - Place your **image** in the `Thermal Image/` folder.

2. **Run one of the notebooks:**
   - `Vcvision04.ipynb` → for video red zone detection.
   - `cvision.ipynb` → for analyzing red zones in static images.

3. **Review your outputs:**
   - Check the **output video**, **alert logs**, and **key alert frames**.
   - Review the **plotted chart** of red pixel intensity over time.

---

## New Feature: Synthetic Image Generator

A new script `app.py` has been added to simulate synthetic thermal images for testing and experimentation.

---

## Synthetic Thermal Image Generator (`app.py`)

This script generates thermal-like images of industrial pipeline systems using a prompt-driven model. It simulates different temperature zones in a heatmap style (Red = hot, Blue = cool).

### ✅ Features

- Prompts simulate varying thermal conditions frame-by-frame.
- Uses a reference image for realistic style transfer.
- GPU support for faster generation (if available).
- Saves each generated frame to the `OutputFrames/` folder.
