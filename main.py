from connection import DatabaseConnection
from helper import add_videos_by_file

def main():
    db = DatabaseConnection()

    while True:
        print("\nYoutube Video App || Choose Option")
        print("1. List All Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Add videos by file")
        print("6. Exit App")

        choice = input("Enter Your Choice: ").strip()
        
        if choice == '1':
            videos = db.list_all_videos()
            print('\n' + '*' * 70)
            for v in videos:
                print(f"id: {v[0]}, Name: {v[1]}, Time: {v[2]}, Link: {v[3]}")
            print('*' * 70)
        
        elif choice == '2':
            video_name = input("Enter Video Name: ").strip()
            video_time = input("Enter Video Time: ").strip()
            video_link = input("Enter Video Link: ").strip()
            db.add_video(video_name, video_time, video_link)
        
        elif choice == '3':
            try:
                id_ = int(input("Enter Video Id: ").strip())
            except ValueError:
                print("Invalid Id")
                continue
            video_name = input("Enter Video Name: ").strip()
            video_time = input("Enter Video Time: ").strip()
            video_link = input("Enter Video Link: ").strip()
            db.update_video(id_, video_name, video_time, video_link)
        
        elif choice == '4':
            try:
                id_ = int(input("Enter Video Id: ").strip())
            except ValueError:
                print("Invalid Id")
                continue
            db.delete_video(id_)
        
        elif choice == '5':
            file_name = input("Please enter file name: ").strip()
            file_path = input("Enter path or '.' for current folder: ").strip()
            add_videos_by_file(db, file_name, file_path)
        
        elif choice == '6':
            print("Exiting...")
            db.close()
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
