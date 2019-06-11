import os

def main():
    i=0
    path = os.getcwd()
    #folder = os.path.basename(path)
    for filename in os.listdir():
        if filename=='rename.py':
            continue
        newName ="mscm_server.log_" +str(i)+".txt"
        src =path+ "\\" + filename
        dst =path+ "\\" + newName
        os.rename(src, dst)
        i += 1

if __name__ == '__main__':

    main()
