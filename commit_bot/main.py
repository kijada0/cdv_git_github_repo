import os

# -------------------------------------------------------------------------------- #

repo_path = "../"
file_name_to_modify = "we_are_the_best.md"
text_to_format = "# We are the best for: {} days in a row"


# -------------------------------------------------------------------------------- #

def main():
    file_list = os.listdir(repo_path)
    print(file_list)

    # Update the file
    counter = 2
    file_path = os.path.join(repo_path, file_name_to_modify)
    update_file(file_path, counter)


def update_file(file_name, counter):
    print("Updating file: ", file_name)

    # Check if the file exists
    if not os.path.exists(file_name):
        print("File does not exist")
        return

    # Read the file
    with open(file_name, "r") as file:
        file_content = file.readlines()

    # Update the last line
    last_line = text_to_format.format(counter)
    file_content[-1] = last_line

    # Write the file
    with open(file_name, "w") as file:
        file.writelines(file_content)


# -------------------------------------------------------------------------------- #

if __name__ == "__main__":
    main()
