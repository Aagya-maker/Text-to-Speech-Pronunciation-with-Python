 #make sure to install espeak. I ran this on my terminal beforehand - sudo apt-get install espeak

import subprocess

def pronounce_names(name_list):
    for name in name_list:
        subprocess.run(['espeak', name])

if __name__ == "__main__":
    names = ['Aagya', 'Cooks']
    pronounce_names(names)