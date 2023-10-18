import os


def scan_directory_and_write_to_file(directory_path, output_file, file_extension=None, partial_filename=None):
    try:
        with open(output_file, 'w') as file:
            for root, dirs, files in os.walk(directory_path):
                for filename in files:
                    if (file_extension is None or filename.lower().endswith(file_extension.lower())) and \
                            (partial_filename is None or partial_filename.lower() in filename.lower()):
                        file_path = os.path.join(root, filename)
                        file.write(file_path + '\n')
        print("Scanning completed successfully. Results have been saved to a file.")
    except FileNotFoundError:
        print("The specified directory does not exist.")
    except PermissionError:
        print("No access to files in the specified directory.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Request user input for directory, file type, and partial filename
directory_to_scan = input("Enter the directory path for scanning: ")
file_extension = input("Enter the file extension (e.g., 'txt'), or leave empty for all files: ").strip()
partial_filename = input("Enter a partial filename, or leave empty for all files: ").strip()
output_file_path = input("Enter the file path to save the results: ")

# Replace '~' with the actual home directory path if applicable
output_file_path = os.path.expanduser(output_file_path)

scan_directory_and_write_to_file(directory_to_scan, output_file_path, file_extension, partial_filename)
