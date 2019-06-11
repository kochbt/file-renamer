# file-renamer
File Renamer is a tool in the form of an executable python file used to automate the process of renaming files in a directory. Specifically, File Renamer was created to handle a situation where the user exports a large number of log files which were automatically numbered [filename].1, [filename].2, etc. Upon opening each file the user is prompted to select the program they want to use to open the filetype of .1, .2, etc. File Renamer changes every file within it's directory (except for itself) to a sequentially numbered file that ends in the extension ".txt" so each file will automatically open in the desired text editor.

TO USE:
Place the Rename.py file in the directory that holds the files to be renumbered
Double click on Rename.py OR open Rename.py in IDLE and select Run > Run Module
The files in the folder will be automatically renamed

NOTE:
Rename.py can be customized to hard code in the directory to be renamed or to change the new names of the files
