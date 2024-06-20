import os
import shutil
import string

def find_group_line(file_path, target_content):
    """Finds a line containing the target content in the file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if target_content in line:
                parts = line.split(',')
                if len(parts) > 1:
                    # Strip quotes and use the second part "ZA1"
                    group = parts[1].strip().strip('"')
                    return group.upper()  # Use upper case for grouping
    return 'UNGROUPED'  # Default group if the target content is not found

def sanitize_directory_name(name):
    """Sanitizes the directory name to remove invalid characters."""
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    sanitized_name = ''.join(c for c in name if c in valid_chars)
    return sanitized_name

def group_notepad_files(source_dir, target_dir, target_content):
    """Groups Notepad files based on lines containing specific content."""
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for file_name in os.listdir(source_dir):
        if file_name.endswith('.txt'):  # Assuming Notepad files have .txt extension
            source_file_path = os.path.join(source_dir, file_name)
            group = find_group_line(source_file_path, target_content)
            group = sanitize_directory_name(group)
            group_dir = os.path.join(target_dir, group)

            if not os.path.exists(group_dir):
                os.makedirs(group_dir)

            target_file_path = os.path.join(group_dir, file_name)
            shutil.move(source_file_path, target_file_path)  # Move file to grouped directory
            print(f'Moved {file_name} to {group_dir}')

def copy_za1_files_to_network(target_dir, network_dir):
    """Copies files from the ZA1 folder to the network location."""
    za1_dir = os.path.join(target_dir, 'ZA1')

    # Check if the network path is accessible
    if not os.path.exists(network_dir):
        print(f'The network directory {network_dir} does not exist or is not accessible.')
        return

    if os.path.exists(za1_dir):
        for file_name in os.listdir(za1_dir):
            source_file_path = os.path.join(za1_dir, file_name)
            target_file_path = os.path.join(network_dir, file_name)
            try:
                shutil.copy(source_file_path, target_file_path)
                print(f'Copied {file_name} to {network_dir}')
            except Exception as e:
                print(f'Error copying {file_name} to {network_dir}: {e}')
    else:
        print(f'The directory {za1_dir} does not exist.')

def delete_grouped_folders(target_dir):
    """Deletes all folders in the target directory."""
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)
        if os.path.isdir(item_path):
            try:
                shutil.rmtree(item_path)
                print(f'Deleted folder {item_path}')
            except Exception as e:
                print(f'Error deleting folder {item_path}: {e}')

# Example usage
source_directory = r'C:\Users\fhulufhelo\Documents\mannatech\original'
target_directory = r'C:\Users\fhulufhelo\Documents\mannatech\grouped'
network_directory = r'\\10.10.10.221\Mannatech'
target_content = '"15","ZA1"'

group_notepad_files(source_directory, target_directory, target_content)
copy_za1_files_to_network(target_directory, network_directory)
delete_grouped_folders(target_directory)
