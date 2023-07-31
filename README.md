## Python Script Documentation

### Introduction

The Python script provided in this document serves three main tasks related to converting MP3 audio files to text and organizing the text data into a JSONL (JSON Lines) file. The script utilizes external libraries and a remote speech recognition service to achieve these tasks.

### Requirements

- Python 3.x installed on the system.
- Internet connection to interact with the remote speech recognition service.
- The `requests` library must be installed to make HTTP requests.

### Task 1: Convert MP3 Audio to Text

#### `convert_text(src_folder_path, destination_file)`

This function takes the path of a folder containing MP3 audio files and a destination folder path where the converted text files will be saved.

**Parameters:**

- `src_folder_path` (str): The path to the folder containing the MP3 audio files.
- `destination_file` (str): The path to the folder where the converted text files will be saved.

**Functionality:**

1. The function scans the `src_folder_path` for MP3 files and compiles a list of all files with the ".mp3" extension.
2. For each MP3 file, it reads the binary data of the file and sends it to a remote server for speech recognition.
3. The remote server responds with transcribed text, divided into multiple utterances.
4. The function processes the JSON response and saves the transcribed text as separate text files with the same name as the original MP3 files but with the ".txt" extension in the `destination_file` folder.

**Note:** The actual speech recognition is performed by a remote server. Ensure that the server specified in the `requests.post()` call (`http://207.178.107.92:8080/`) is operational and provides the speech-to-text service.

### Task 2: Clean Text Files

#### `clean_text(file_path)`

This function takes the path to a text file as input and returns the contents of the file with leading and trailing whitespaces removed.

**Parameters:**

- `file_path` (str): The path to the text file that needs to be cleaned.

**Functionality:**

1. The function reads the contents of the specified text file.
2. It removes any leading or trailing whitespaces from each line of the file.
3. The cleaned lines are stored in a list, and the function returns the joined cleaned lines as a single string.

### Task 3: Merge Cleaned Text into JSONL

#### `convert_to_jsonl(src_folder)`

This function takes the path of a folder containing text files and compiles their contents into a JSONL (JSON Lines) format.

**Parameters:**

- `src_folder` (str): The path to the folder containing the text files.

**Functionality:**

1. The function traverses through all the files in the `src_folder`.
2. For each text file, it calls the `clean_text()` function to obtain the cleaned content.
3. The function then creates a list of dictionaries, where each dictionary contains the file name and its cleaned content.
4. The list of dictionaries is returned, representing the JSONL data.

#### `merge_to_jsonl(src_folder, destination_file)`

This function takes the path of a folder containing text files and a destination file path where the JSONL data will be saved.

**Parameters:**

- `src_folder` (str): The path to the folder containing the text files.
- `destination_file` (str): The path to the JSONL file that will be created.

**Functionality:**

1. The function calls the `convert_to_jsonl()` function to obtain the JSONL data.
2. It writes the JSONL data to a new file specified by `destination_file`, where each line contains a JSON object representing a text file's content.

### Execution and Output

- The script can be executed in a Python environment, and it requires proper configuration for the source folder, destination folder, and remote speech recognition service.
- Once executed, the script will convert the MP3 files to text files, clean their contents, and create a JSONL file containing the cleaned text data.

### Notes

- The script's functionality relies on the availability and functionality of the remote speech recognition server specified in the code.
- Ensure that the necessary libraries (`requests`) are installed before running the script.
- Handle any potential exceptions and errors that may arise during execution.
