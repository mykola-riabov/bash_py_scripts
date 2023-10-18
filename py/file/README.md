
---

## Directory Scanner and File List Generator

This Python script allows you to scan a specified directory and generate a list of file paths based on user-defined criteria such as file extension or partial filename. The results are saved to a text file for easy reference.

### How to Use

1. Run the script and provide the following inputs:
    - **Directory Path:** Enter the path to the directory you want to scan.
    - **File Extension:** Optionally, specify a file extension (e.g., 'txt') to filter the scanned files. Leave empty to include all file types.
    - **Partial Filename:** Optionally, enter a partial filename to filter the scanned files. Leave empty to include all files.
    - **Output File Path:** Enter the path to the text file where the results will be saved.

2. The program will scan the specified directory, filter the files based on the provided criteria, and save the file paths to the specified text file.

### Example Usage

```bash
python scan_directory.py
```

### Note

- The script replaces '~' with the actual home directory path if included in the file path.

---