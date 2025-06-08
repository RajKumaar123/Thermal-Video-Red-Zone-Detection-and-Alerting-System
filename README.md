# Thermal Video Red Zone Detection and Alerting System

This project focuses on automatically detecting and monitoring areas with high red intensity in thermal or surveillance videos—commonly linked to rising temperatures, potential fire zones, or heat leaks. Built using Python, OpenCV, and NumPy, the system analyzes each frame of the video to track red pixel intensity in real time.

It features automated alert logging when red intensity goes beyond a set threshold, along with visual outputs such as annotated videos and red activity plots over time. These insights help identify heat-related anomalies early, enabling quicker and more informed responses.

The solution is ideal for industrial safety monitoring, environmental surveillance, and thermal event analysis. It's fully customizable, letting users adjust sensitivity levels to suit different operational needs.

We use the UNO-FLUX model from Hugging Face to generate synthetic thermal images. These images simulate realistic heatmaps with zones representing different temperature levels (e.g., red for hot, blue for cool).
The generated results are saved in the Thermal Image folder and can be used for analysis—just like real thermal input.

This approach helps test the system without needing actual thermal footage and can also be extended to generate synthetic video frames for full pipeline evaluation.

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
   - `Vcvision03.ipynb` → for video red zone detection for all the frames.
   - `Vcvision04.ipynb` → for video red zone detection with visulazation .
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
