import webbrowser
import random



# Numbers
def numbers():
    global url
    url = 'https://github.com/purcellconsult/Master-Python-3-Course-/blob/master/1_numbers_in_python.py'
    return 'Review Numbers and built in data types.'

# Flow Control
def flow():
    global url
    url = 'https://github.com/purcellconsult/Master-Python-3-Course-/blob/master/2_control_and_repeat.py'
    return 'Review control and flow, if, else, for and while loops.'

# String Processing
def sprocessing():
    global url
    url = 'https://github.com/purcellconsult/Master-Python-3-Course-/blob/master/3_string_processing.py'
    return 'Review string processing and manipulation.'

# Data Structures
def data_structure():
    global url
    url = 'https://github.com/purcellconsult/Master-Python-3-Course-/blob/master/4_a_gentle_intro_to_data_structures.py'
    return 'Review the four built-in data structures and how to work with them.'

# Functions and Functional Programming
def functions():
    global url
    url = 'https://github.com/purcellconsult/Master-Python-3-Course-/blob/master/5_functions_and_functional_programming.py'
    return 'Review functions and functional programming like lambda and map.'

# Sockets
def sockets():
    global url
    url = 'https://www.youtube.com/watch?v=2P8s_KV51rM'
    return 'Review the basics of sockets and wow to use them.'

# Multiprocessing
def multiprocessing():
    global url
    url = 'https://www.youtube.com/playlist?list=PLeo1K3hjS3uub3PRhdoCTY8BxMKSW7RjN'
    return 'Review multithreading, multiprocessing and what locks are'

# Decorators
def decorator():
    global url
    url = 'https://realpython.com/primer-on-python-decorators/'
    return 'Review decorators.'

# Generators
def generators():
    global url
    url = 'https://realpython.com/introduction-to-python-generators/'
    return 'Review Generators.'

# JSON
def json():
    global url
    url = 'https://realpython.com/python-json/'
    return 'Review JSON, how to manipulate, navigate and find sources for acquisition.'

# Docker
def docker():
    global url
    url = 'https://djangostars.com/blog/what-is-docker-and-how-to-use-it-with-python/'
    return 'Review docker and how to implement it.'

# VIM
def vim():
    global url
    url = 'https://danielmiessler.com/study/vim/'
    return 'Review how to work with VIM and the hotkeys to navigate.'

study_list = [numbers, flow, sprocessing, data_structure, functions, sockets,
              multiprocessing, decorator, generators, json, docker, vim]

p = random.choice(study_list)()
print(p)
webbrowser.open_new_tab(url)
