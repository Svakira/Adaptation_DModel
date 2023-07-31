import os
import requests
import json

def convert_text(src_folder_path,destination_file):
    mp3_files = [file for file in os.listdir(src_folder_path) if 
    file.endswith('.mp3')]

    for mp3_file in mp3_files:
        mp3_file_path = os.path.join(src_folder_path, mp3_file)
        output_file_path = os.path.join(destination_file, 
    f"{os.path.splitext(mp3_file)[0]}.txt")

        with open(mp3_file_path, 'rb') as f:
            response = requests.post('http://207.178.107.92:8080/', files={'data': 
    f})

            print(output_file_path)
            print(response)
            print(response.content)
            transcript = ""
            utterances = response.json()
            for utterance in utterances:
                transcript += f"{utterance['text']}\n"
            print(transcript)
            with open(output_file_path, 'w') as output_file:
                        output_file.write(transcript)

def clean_text(file_path):
    with open(file_path, 'r', encoding='latin-1') as f:
        lines = f.readlines()
    
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    return '\n'.join(cleaned_lines)

def convert_to_jsonl(src_folder):
    jsonl_data = []
    for root, _, files in os.walk(src_folder):
        for file in files:
            # Only process .txt files
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                cleaned_content = clean_text(file_path)
                jsonl_data.append({"file_name": file, "content": cleaned_content})
    return jsonl_data

def merge_to_jsonl(src_folder, destination_file):
    jsonl_data = convert_to_jsonl(src_folder)
    with open(destination_file, "w", encoding="latin-1") as f:
        for item in jsonl_data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    # Replace 'source_folder_path' with the path to your source folder
    src_folder_path = "./"
    # Replace 'destination_file_path' with the desired destination JSONL file path
    destination_file_path = "./merged_output.jsonl"
    destination_file="./"

    merge_to_jsonl(src_folder_path, destination_file_path)
    convert_text(src_folder_path,destination_file)
    print("Text files cleaned, converted to JSONL, and merged successfully!")
