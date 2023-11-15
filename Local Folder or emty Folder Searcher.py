import os

def find_empty_folders(directory):
    empty_folders = []

    for root, dirs, files in os.walk(directory):
        if not dirs and not files:
            empty_folders.append(root)

    return empty_folders

def main():
    # Specify the directory you want to search (in this case, the C drive)
    search_directory = r"C:\Users\style"

    empty_folders = find_empty_folders(search_directory)

    if empty_folders:
        print("Empty folders found:")
        for folder in empty_folders:
            print(folder)
    else:
        print("No empty folders found.")

if __name__ == "__main__":
    main()
