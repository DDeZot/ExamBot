import json
import codecs
from typing import Final

exams_path = 'telegram_bot\\databases\\'
CPP_EXAM: Final = json.load(fp=codecs.open(exams_path + 'cpp_exam\\cpp.json', 'r', 'utf_8_sig'))
MATH_EXAM: Final = json.load(fp=codecs.open(exams_path + 'math_exam\\math.json', 'r', 'utf_8_sig'))
#PYTHON_EXAM: Final = json.load(fp=codecs.open(exams_path + 'python_exam\\python.json', 'r', 'utf_8_sig'))
