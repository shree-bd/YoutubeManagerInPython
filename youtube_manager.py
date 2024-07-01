import json
import time


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, vid in enumerate(videos, start=1):
        print(f"{index}. {vid['name']}, Duration: {vid['time']} ")
    print("*" * 70)


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)


def update_video_details(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to be updated: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index - 1] = {'name': name, 'time': time}
        save_data_helper(videos)
        print("Video has been updated")
        print("*" * 70)
    else:
        print("Invalid index")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to be deleted: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
        print("Video deleted")
    else:
        print("Video not found")


def main():
    videos = load_data()
    while True:
        print("\n Welcome to YouTube Manager Application | Choose an option")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video_details(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Exiting the application")
                time.sleep(1)
                print("!!!!!!!!Thank you for using YouTube Manager!!!!!")
                break
            case _:
                print("Invalid choice!!!")


if __name__ == "__main__":
    main()
