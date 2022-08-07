"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print(f"Starting directory is: {os.getcwd()}")

    # Change to desired directory
    os.chdir('Lyrics/Lyrics/Christmas')

    # Print a list of all files in current directory
    print(f"Files in {os.getcwd()}:\n{os.listdir('')}\n")

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    # TODO: Use exception handling to avoid the crash (just pass)
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir(''):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print(f"Renaming {filename} to {new_name}")

        # TODO: Try these options one at a time
        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('')
    for directory_name, subdirectories, filenames in os.walk(''):
        print(f"Directory:{directory_name}")
        print(f"\tcontains subdirectories:{subdirectories}")
        print(f"\tand files:{filenames}")
        print(f"(Current working directory is: {os.getcwd()})")

        # TODO: add a loop to rename the files
        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)

main()
# demo_walk()