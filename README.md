# Extract-filenames-from-Strace-result
This python script is used to extract all file paths from the Strace result. For this, we have to save the result of Strace in a file. Then we have to put the file name with the full pathname in a "filepath" variable at the start of the script.

For Example:

root@cybermizz:~# strace anycommand 2> output.txt

Now put the filename like "output.txt" with its full pathname in "filepath" variable at the start of the python script.

root@cybermizz:~# python getLogFilePath.py

