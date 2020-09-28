[![Last commit](https://img.shields.io/github/last-commit/javieroramas/file-wizard.svg?style=flat)](https://github.com/javieroramas/file_wizard/commits)[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/javieroramas/file-wizard)](https://github.com/javieroramas/file_wizard/commits) [![Github Stars](https://img.shields.io/github/stars/javieroramas/file-wizard?style=flat&logo=github)](https://github.com/javieroramas/file_wizard) [![Github Forks](https://img.shields.io/github/forks/javieroramas/file-wizard?style=flat&logo=github)](https://github.com/javieroramas/file_wizard) [![Github Watchers](https://img.shields.io/github/watchers/javieroramas/file-wizard?style=flat&logo=github)](https://github.com/javieroramas/file_wizard) [![GitHub contributors](https://img.shields.io/github/contributors/javieroramas/file-wizard)](https://github.com/javieroramas/file_wizard/graphs/contributors)
# Directory Filter

## Installation

`pip install -r requirements.txt`

## Usage

### Purge
To remove all files inside a directory with a given extension run:<br>
`python3 main.py purge [directory] [extension]`

### Extract video, audio or photo files
To extract all files within a choosen category in a directory and move them to another run:<br>
`python3 main.py extract [category] [source] [destination]`

### Extract Custom Extension
To extract all files with a given extension in a directory and move them to another run:<br>

`python3 main.py extract_ext [directory] [destinantion] [extension]`

### Enumerate video, audio or photo files
To count all files within a choosen category in a directory:<br>
`python3 main.py enumerate [category] [source]`

### Find And remove duplicate files
To find all duplicate files in a directory:<br>
`python3 main.py duplicates [directory]`

if runned like:<br>
`python3 main.py duplicates`<br>
it uses the main path as directory

Everytime that a match the program will ask you what to do:<br>
0: leave both files<br>
1: remove the first element<br>
2: remove the second element<br>

### https://github.com/hiancdtrsnm/video-diet functionalities
To run the file or folder conversion functionalities from https://github.com/hiancdtrsnm/video-diet run
`python3 main.py video-diet-file [path]`

`python3 main.py video-diet-folder [path (default the current location)] [ignore_extension (optional)] [ignore_path (optional)]`
