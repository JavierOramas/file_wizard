# Directory Filter

## Installation

`pip install -r requirements.txt`

## Usage

### Purge

To remove all files inside a directory with a given extension run:<br>
`python3 script.py purge [directory] [extension]`

### Extract video, audio or photo files
To extract all files within a choosen category in a directory and move them to another run:<br>
`python3 script.py extract [category] [source] [destination]`

### Extract Custom Extension
To extract all files with a given extension in a directory and move them to another run:<br>

`python3 script.py extract_custom [directory] [destinantion] [extension]`

### Enumerate video, audio or photo files
To count all files within a choosen category in a directory:<br>
`python3 script.py enumerate [category] [source]`

### Find And remove duplicate files
To find all duplicate files in a directory:<br>
`python3 script.py duplicates [directory]`

if runned like:<br>
`python3 script.py duplicates`<br>
it uses the script path as directory

Everytime that a match the program will ask you what to do:<br>

0: leave both files<br>
1: remove the first element<br>
2: remove the second element<br>