# Imports
import os

# Variables
# TODO: destination_directory_path should be passed as argument or from config file
destination_directory_path_helper = "C:\\Users\Vincent\Desktop\\Moved"
destination_directory_path = destination_directory_path_helper + "\\"
# The whitelist to ignore
# TODO: Whitelist should be passed from argument or from config file
desktop_whitelist = ["Game_Related.lnk", "Nvidia.lnk", "PyCharm.lnk","Steam.lnk","WoW.lnk","WinDirStrat.lnk","DesktopCleaner.lnk","Battlefield4.lnk"]
desktop_whitelist.append(os.path.basename(destination_directory_path_helper))


# Functions
def show_result():
    print("---------------------------------")
    print("Files moved: " + str(files_moved))
    print("Files preserved: " + str(files_preserved))
    print ("The following files have been preserved: ")
    print(desktop_whitelist)
    input("Press enter to exit...")

# 1: Path to the Desktop
# 2: List of whitelisted filenames
# 3: Destination path to move the files to, if not in whitelist
def move_to_dir(desktop_location, desktop_whitelist):
    # Counters to initialize
    # TODO: A directory with 10 files in it is also count as '1' file...
    global files_moved, files_preserved
    files_moved = 0
    files_preserved = 0

    # Check if the destination directory already exists
    if not (os.path.exists(destination_directory_path_helper) == True):
        # Create destination dir, since it does not exist yet
        print("Creating directory '" + destination_directory_path_helper +  "'")
        os.mkdir(destination_directory_path_helper)

    # Add all files on the desktop to a list
    desktop_files = os.listdir(desktop_location)
    # Loop through all the files on the desktop
    for desktop_file in desktop_files:
        if any(desktop_file in whitelist_file for whitelist_file in desktop_whitelist):
            # Files are are in the whitelist
            # Lets not do anything, just print it out
            print("IGNORE: '" + desktop_file  + "' is found in the whitelist.")
            files_preserved += 1
        else:
            # Files here are not in the whitelist
            print("MOVING: '" + desktop_file  + "' is NOT found in the whitelist.")
            os.renames(desktop_location + desktop_file, destination_directory_path + desktop_file)
            files_moved += 1



# Function calls
move_to_dir("C:\\Users\Public\Desktop\\", desktop_whitelist)
move_to_dir("C:\\Users\Vincent\Desktop\\", desktop_whitelist)

# Show the result
show_result()


