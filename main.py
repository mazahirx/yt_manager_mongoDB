from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

db_url = os.getenv("DATABASE_URL")

client = MongoClient(db_url)
db = client["youtube_manager"]
video_collections = db["videos"]


def main():
    
    while True:

        print("\n- > Youtube Manager < -")
        print("1. Add videos")
        print("2. View video")
        print("3. Edit video")
        print("4. Delete video")
        print("5. Exit")

        choice = int(input("Chose option : "))

        if choice == 1:
            add_video(name, dur)
        elif choice == 2:
            view_videos(video_id)
        elif choice == 3:
            edit_video(video_id, new_name,new_dur)
        elif choice == 4:
            delete_video(video_id)
        elif choice == 5:
            break
        else:
            print("Chose valid option!")
        
if __name__ == "__main__":
    main()