"""
CP1404 Practical
Sort files based on extension
"""
import os


def main():
    """Move files into folders with the same name as their extension."""
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        print(f"{extension}/{filename}")
        os.rename(filename, f"{extension}/{filename}")


main()