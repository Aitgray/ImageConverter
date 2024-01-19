# Image Converter

## Overview

Image Converter is a Python utility designed to convert images from the HEIC format to the JPG format. This tool is particularly useful for processing images captured on devices like iPhones, which often use the HEIC format for photos.

## Features

1. **HEIC to JPG Conversion**: Converts images from the HEIC format to the more widely used JPG format.
2. **Directory Image Loading**: Loads all HEIC images from a specified directory.
3. **Automated Image Sorting**: (In Development) Sorts images into different categories based on their content, using PyTorch for image analysis. Currently, this feature is focused on distinguishing between people, animals, and landscapes, though it may be improved in the future.

## Installation

To run this script, you need Python 3 installed on your system. Additionally, the following libraries are required:
- `os`
- `subprocess`
- `sys`
- `torch`
- `PIL`
- `face_recognition`

You can install the required libraries using pip:
```bash
pip install torch PIL face_recognition
```

## Usage

Run the script in a Python environment, ensuring that the directory path provided contains HEIC images. The script will automatically convert these images to JPG format. Eventually I might try to figure out GUIs but I'll save that for another day.

## Future Enhancements and Improvements

1. **Enhanced Image Sorting**: The current sorting algorithm could be improved to handle a wider variety of image types and provide more accurate categorization.

2. **User Interface**: Developing a user-friendly interface (CLI/GUI) for easier interaction with the script.

3. **Batch Processing Enhancements**: Optimizing the script for batch processing of large numbers of images, including better error handling and progress reporting.

4. **Customization Options**: Allowing users to specify output formats other than JPG, and providing options for resolution and quality adjustments.

5. **Integration with Cloud Storage**: Enabling the script to directly interact with cloud storage services for uploading or downloading images.

6. **AI Enhancements**: Improving the AI model used for image sorting to increase its accuracy and efficiency.

7. **Automated Backup**: Before converting, the script could offer to create backups of the original HEIC files.

8. **Cross-Platform Compatibility**: Ensuring the script runs smoothly across different operating systems.

## Contributions
Me!
