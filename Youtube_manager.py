import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file, indent=4)

def list_all_videos(videos):
    print("\n" + "*" * 70)
    if not videos:
        print("No videos found.")
    else:
        for index, video in enumerate(videos, start=1):
            print(f"{index}. Name: {video['name']}, Duration: {video['time']}")
    print("*" * 70 + "\n")

def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video duration: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print("Video added successfully!")

def update_videos(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter the video number you want to update: "))
        if 1 <= index <= len(videos):
            new_name = input("Enter the new video name: ")
            new_time = input("Enter the new video duration: ")
            videos[index - 1]['name'] = new_name
            videos[index - 1]['time'] = new_time
            save_data_helper(videos)
            print("Video updated successfully!")
        else:
            print("Invalid video number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_videos(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter the video number you want to delete: "))
        if 1 <= index <= len(videos):
            deleted = videos.pop(index - 1)
            save_data_helper(videos)
            print(f"Deleted video: {deleted['name']}")
        else:
            print("Invalid video number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    videos = load_data()

    while True:
        print("\nYouTube Manager | Choose an option")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_videos(videos)
            case "4":
                delete_videos(videos)
            case "5":
                print("Exiting YouTube Manager. Goodbye!")
                break
            case _:
                print("Invalid command. Please choose a valid option.")

if __name__ == "__main__":
    main()