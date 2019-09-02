import pip

def install(package):
    pip.main(['install', package])

if __name__ == '__main__':
    answer=input('what do you want to install?')
    install(answer)
#file name   ^
