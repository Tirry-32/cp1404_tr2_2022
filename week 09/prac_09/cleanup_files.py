"""
CP1404 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print(f"Starting directory is: {os.getcwd()}")

    os.chdir('Lyrics')

    print(f"Files in {os.getcwd()}:\n{os.listdir('')}\n")

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
    for directory_name, subdirectories, filenames in os.walk(''):
        print(f"Directory:{directory_name}")
        print(f"\tcontains subdirectories:{subdirectories}")
        print(f"\tand files:{filenames}")
        print(f"(Current working directory is: {os.getcwd()})")

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print(f"Renaming {filename} to {new_name}")

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name

main()
