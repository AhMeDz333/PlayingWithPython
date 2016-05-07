## CleanProject

CleanProject is a python script which given an android project directory path, finds all the unused resource files and kills them *in liam neeson's voice*

It also gives you the option of passing regex as system params to exclude drawables that match one of those regex.

The output is written into a file, the content is: 
* Detected resource path.
* Files whiteListed (used) with it's path. and size.
* Files excluded (matches a regex) with it's name.
* Total files deleted.
* Total size freed. 

It actually helps shrink the app package size a really big deal.

##Usage
python CleanProject.py 'directory_path' regex1 regex2 ... regexN
Example:

```python
python CleanProject.py /home/user/MyAndroidProject poster_[0-9]+ user.*
```

##Requirements
Python 2.7 or Python 3.0

##Rest of the files
Those are just my solutions to online challenges found at [PythonChallenge](http://www.pythonchallenge.com/), some cool stuff there!
