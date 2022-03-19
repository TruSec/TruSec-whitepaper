import os
import shutil


def delete_directory_contents(self, folder):
    """

    :param folder: Directory that is being deleted.

    """
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print("Failed to delete %s. Reason: %s" % (file_path, e))


def get_dir_filelist_based_on_extension(dir_relative_to_root, extension):
    """

    :param dir_relative_to_root: A relative directory as seen from the root dir of this project.
    :param extension: The file extension that is used/searched in this function.

    """
    selected_filenames = []
    # TODO: assert directory exists
    for filename in os.listdir(dir_relative_to_root):
        if filename.endswith(extension):
            selected_filenames.append(filename)
    return selected_filenames


def create_dir_relative_to_root_if_not_exists(dir_relative_to_root):
    """

    :param dir_relative_to_root: A relative directory as seen from the root dir of this project.

    """
    if not os.path.exists(dir_relative_to_root):
        os.makedirs(dir_relative_to_root)


def delete_dir_relative_to_root_if_not_exists(dir_relative_to_root):
    """

    :param dir_relative_to_root: A relative directory as seen from the root dir of this project.

    """
    if os.path.exists(dir_relative_to_root):
        # Remove directory and its content.
        shutil.rmtree(dir_relative_to_root)


def dir_relative_to_root_exists(dir_relative_to_root):
    """

    :param dir_relative_to_root: A relative directory as seen from the root dir of this project.

    """
    if not os.path.exists(dir_relative_to_root):
        return False
    elif os.path.exists(dir_relative_to_root):
        return True
    else:
        raise Exception(
            "Directory relative to root: {dir_relative_to_root} did not exist, nor did it exist."
        )
