# Files_organizer
Python script to organise files in desktop based on extentions
Limitatations:
1. Can work on Windows only for now
2. Currently works on path provided only and ignores the directories in it(if you want to go into directories further remove the last break statement)! Not tested and can result in various tragedies
Ignores py and db extentions by default

Requirements:
Python 3.x

copy the address for folder to organise and run main.py
The script will create a db file at target location which is not recommended to be deleted as it will store the data for extentions that are processed and folders are created.
The script takes extentions that it needs to ignore and ignore all files with that extentions(These are not saved in database)
After you are done you can remove the py files.
