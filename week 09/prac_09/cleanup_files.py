"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print(f"Starting directory is: {os.getcwd()}")

    os.chdir('Lyrics/Lyrics/Christmas')

    print(f"Files in {os.getcwd()}:\n{os.listdir('')}\n")

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    for filename in os.listdir(''):
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print(f"Renaming {filename} to {new_name}")

        shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('')
    for directory_name, subdirectories, filenames in os.walk(''):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print(f"(Current working directory is: {os.getcwd()})")

        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)

main()
# demo_walk()