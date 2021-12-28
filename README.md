# Codeforces Test Parser for C/C++ on Windows

### Installation
* Run ```pip install beautifulsoup4 requests psutil``` in your terminal.
* Clone this repository!
* Change ```workspace_folder``` in ```run.py``` to the folder where your source files are placed in.
* Please make some changes in ```run.py``` to make it suitable for your folder structure. Below is mine.

### Folder structure
```
Codeforces
    |   ...
    |   1620A.cpp
    |   1620B.cpp
    |   ...
codeforces_test_parser
    |---samples
    |      |---[contest_id] # e.g. 1620
    |           |---A
    |               |   input0.txt
    |               |   output0.txt
    |               |   ...
    |           |---B
    |           |---...
    |   prepare.py
    |   run.py
```

### Usage
* Use ```.\prepare [contest_id] [problem_id1] [problem_id2] ...``` to download sample test cases.
For example: ```.\prepare 1620 A B C D E``` to download problem A, B, C, D, and E from Educational Codeforces Round 119 (contest id is 1620).

* Use ```.\run [problem_id]``` to run sample test case (only one problem at a time).
For example: ```.\run A``` for testing problem A.

* In case your default application for ```.py``` files is not Python, e.g. PyCharm, VSCode, etc. Please use ```python prepare.py``` instead of ```.\prepare``` and ```python run.py``` instead of ```.\run```.

If you find this repository useful, please give it a star :star:!
