from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

db_url = os.getenv("DATABASE_URL")

client = MongoClient(db_url)
db = client["youtube_manager"]
video_collections = db["videos"]

def add_video(name, dur):

    name = input("Enter video title : ")
    dur = input("Enter video duration : ")

    video_details = video_collections.insert_one({
        'name' : name,
        'duration' : dur
    })

    video_id = video_details.inserted_id()

    print(f"Video added to collection ! ")
    print(f"Name : {name} \nDuration : {dur} \nID : {video_id}")

def view_videos(video_id):

    video_id = input("Enter video id to view : ")

    if video_collections.find_one(video_id):
        print("Video found : ")
        print("Details : {video_collections.name} \n{video_collections.dur}")
    else:
        print("Video not found ! ")
    

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