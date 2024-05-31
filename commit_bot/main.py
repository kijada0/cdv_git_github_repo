import os
import time

# -------------------------------------------------------------------------------- #

repo_path = "../"
file_name_to_modify = "we_are_the_best.md"
text_to_format = "# We are the best for: {} days in a row"


# -------------------------------------------------------------------------------- #

def main():
    file_list = os.listdir(repo_path)
    print(file_list)

    for counter in range(3, 50+1):
        # Update the file
        file_path = os.path.join(repo_path, file_name_to_modify)
        update_file(file_path, counter)

        # Git commit
        commit_message = "Update certificate, we are now the best for {} days in a row".format(counter)
        git_commit(commit_message)

        time.sleep(0.25)


# -------------------------------------------------------------------------------- #

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

def git_commit(commit_message):
    print("Committing changes to git")

    cmd = "git commit -a -m \"" + commit_message + "\""
    os.system("cd ..")
    os.system(cmd)
    # print(cmd)


# -------------------------------------------------------------------------------- #

if __name__ == "__main__":
    main()
