Summary
=======
The goal of this project is to make it very fast and simple to find an MSDS document.

GUI
=======
The plan is to accomplish this with a single window laid out as follows:
    - A filter bar will be the most prominent at top.  To find a document the user just starts typing the name of the product.
    - A list or table display with the documents that match the filter, or all documents if the filter is blank.
        - When there are new documents just added to the index they will be at the top of the list in red, meaning they need to have titles and keywords added.
        - When an item is double-clicked the document will be opened in a new window
    - When an item is selected from the list, there will be an information panel at the bottom of the window.
        - When normal items in the list are clicked, this panel will be in read-only mode and the user will have to click an edit button and probably a password before editing the document information
        - When a newly indexed items (displayed in red in the list) are clicked, or when the edit button on the read-only mode is clicked, all items in this panel become editable, and there is a delete button (requiring confirmation).

Command Line Interface
======================
To make updating items simpler, there will also be a command-line interface which can send a signal to the running program that there are new files in some directory to be indexed.

There will be a command line parameter to select the sqlite database used.

File Structure
==============
configuration.py -- allows for specific viewers to be used for specific file extensions
main.py -- used to launch the program
main.ui -- Main Window Qt user interface file
mainWindow.py -- Main Window Qt Code, generated from main.ui
setup.vbs -- script to find python or throw an error, then run setup.py with it
setup.sh -- script to find python or throw an error, then run setup.py with it
setup.py -- set up a launcher if appropriate, and auto-indexing of inserted USB drives if possible

Database Structure
==================
To prevent duplicate documents, hashes of the documents will be kept.  When there are duplicate files, they will be listed and the user will be able to resolve whatever the problem is.

The "index" of documents will be kept in an SQLite database in a user's home directory.

Installation
============
Before installing, you will first need to install python 2 (we'll use 2.7 to create the app), and the qt window toolkit
Next, run the setup script for your operating system

Configuration
=============
If you want to use a specific program to view a certain type of file, edit the configuration.py file

