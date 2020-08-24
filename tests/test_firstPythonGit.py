import sys
sys.path.insert(1,'G:\\jenkins_git\\my_proj\\Python_Projects\\src')
from firstPythonGit import hello_world

def test_hello_world():
	assert hello_world() == "Hello World"