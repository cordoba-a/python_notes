# Data Extraction from Images with Python

This project contains a Python script that processes an image of a student list (captured from an original PDF document) and extracts the columns of interest: enrollment number and student name. The extracted data is then saved in a CSV file.

## Prerequisites

1. Have Python 3.6 or later installed.
2. Install the following required libraries:
   ```bash
   pip install pytesseract 
      ```
   ```bash
   pillow pandas
   ```
   On macOS, install Tesseract OCR with:
   ```bash
   brew install tesseract
   ```

## Process Description

1. **Image Capture**:
   - An image containing the columns of interest (enrollment number and student name) was captured from an original PDF document.

2. **Text Processing**:
   - The script uses Tesseract OCR to extract text from the image.
   - Enrollment numbers and student names are cleaned and separated using regular expressions.

3. **Creating DataFrames**:
   - The extracted data is organized into columns using the pandas library.

4. **Exporting Results**:
   - The final result is saved to a CSV file named `datos_extraidos.csv`.

## Usage

### 1. Update the Image Path

Modify the `image_path` variable with the full path to your image:
```python
image_path = "path/to/your/image.png"
```

### 2. Run the Script

Execute the provided code in your Python environment.

### 3. Output

The script will generate a file named `datos_extraidos.csv` with the following format:

| No. | Enrollment  | Student Name              |
|-----|-------------|-----------------------------------|
| 1   | 244020028   | BRETON NICASIO DIEGO ALEJANDRO    |
| 2   | 244020007   | CARREON ROSALES MARGARITA         |
| ... | ...         | ...                               |
