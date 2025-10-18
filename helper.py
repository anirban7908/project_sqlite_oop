import os
import json

def read_file(file_name, file_path):
    if file_path in ('', '.'):
        full_path = file_name
    else:
        full_path = os.path.join(file_path, file_name)

    # Check folder if folder path is not '' or '.'
    if file_path not in ('', '.') and not os.path.isdir(file_path):
        print(f"Directory not found: {file_path}")
        return False

    if not os.path.exists(full_path):
        print(f"File not found: {full_path}")
        return False

    try:
        with open(full_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("File exists but contains invalid JSON.")
        return []
    except Exception as e:
        print("An unexpected error occurred:", e)
        return []

def add_videos_by_file(db_obj, file_name, file_path):
    videos = read_file(file_name, file_path)
    if not videos:
        print("Please provide a valid JSON file.")
        return
    
    for index, video in enumerate(videos, start=1):
        exists = db_obj.check_video(video['name'], video['time'])
        if exists:
            print(f"{index}. Video with same name: {exists[0]} and time: {exists[1]} already exists")
        else:
            db_obj.add_video(video['name'], video['time'], video['video_link'])
            print(f"{index}. Added video: {video['name']}")
