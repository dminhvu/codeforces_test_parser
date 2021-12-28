# Codeforces test parser for C/C++
### Installation
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
* Use ```python prepare.py [contest_id] [problem_id1] [problem_id2] ...``` to download sample test cases.
For example: ```python prepare.py 1620 A B C D E``` to download problem A, B, C, D, and E.

* Use ```python run.py [problem_id]``` to test (only one problem at a time).
For example: ```python run.py A``` for testing problem A.

If you find this repository useful, please give it a star :star:!
