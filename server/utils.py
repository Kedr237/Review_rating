import os
import pickle


def set_cur_dir() -> None: # Changes directory to current
  os.chdir(os.path.dirname(os.path.abspath(__file__)))

def hide_tf_warnings() -> None: # Hides tensorflow warnings
  os.environ['TF_CPP_MIN_LOG_LEVEL']='3'

def load_pkl(path: str): # Loads pickle file
  with open(path, 'rb') as f:
    return pickle.load(f)