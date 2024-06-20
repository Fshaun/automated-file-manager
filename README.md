                                                                        Mannatech File Grouping and Copying Script
                                                                        
This Python script automates the process of grouping Notepad files based on specific content in the file, copying grouped files to a network location, and then deleting the grouped folders.

Features

- Group Notepad Files: Scans files in a source directory and groups them into subdirectories based on the presence of specific content in the file.
- Copy Files to Network Location: Copies files from a specific group folder (e.g., ZA1) to a designated network location.
- Clean Up: Deletes the grouped folders after copying the files to the network location.
  
Requirements

-Python 3.x
-Access to the network location from the machine running the script
-Necessary permissions to read, write, and delete files in the specified directories

Setup

1. Clone or Download the Script
    Clone the repository or download the mannatech.py script file to your local machine.
   
2. Install Python
    Ensure Python 3.x is installed on your machine. You can download it from python.org.
    
3. Set Up Directories

  Create the following directories on your local machine if they do not exist:
    Source directory: C:\Users\fhulufhelo\Documents\mannatech\original
    Target directory: C:\Users\fhulufhelo\Documents\mannatech\grouped
    
Usage

Modify the Script
  -Update the source_directory, target_directory, network_directory, and target_content variables in the script as needed.
  
Run the Script

  -Open a command prompt or terminal.
  -Navigate to the directory containing mannatech.py.
  
Run the script using the command:
    python mannatech.py
    
Script Details

Variables
  -source_directory: The directory containing the original Notepad files.
  -target_directory: The directory where grouped folders will be created.
  -network_directory: The network location where files from the ZA1 folder will be copied.
  -target_content: The specific content to search for in the files to determine their grouping.
  
Functions

  -find_group_line(file_path, target_content): Reads a file and searches for the target content, returning the group name if found.
  -sanitize_directory_name(name): Sanitizes the directory name to remove invalid characters.
  -group_notepad_files(source_dir, target_dir, target_content): Groups Notepad files based on lines containing specific content.
  -copy_za1_files_to_network(target_dir, network_dir): Copies files from the ZA1 folder to the network location.
  -delete_grouped_folders(target_dir): Deletes all folders in the target directory.

Troubleshooting

  -Network Accessibility: Ensure that the network location is accessible from your machine. Try opening the network path in File Explorer to verify connectivity.
  -Permissions: Verify that you have the necessary read/write permissions for the source, target, and network directories.
  -Path Validation: Ensure that the paths specified in the script are correct and properly formatted.
  
Contact

-For further assistance, please contact the script author or your IT support team.

