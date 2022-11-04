#jak stworzyć nowy plik:

f = open("nowyplik.txt","a",encoding="utf-8")
f.write("to jest pierwsza linia\n")
f.close()

f = open("nowyplik.txt","r",encoding="utf-8")
print(f.read())
f.close()

class FileManager:

    def __init__(self,filename,mode,encod):
        self.filename = filename
        self.mode = mode
        self.encod = encod
        self.file = None

    def __enter__(self):
        self.file = open(self.filename,self.mode,encoding=self.encod)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager('testowy.txt','w','utf-8') as f:
    f.write('testowy tekst....')


print(f.closed)

with FileManager('nowyplik.txt','r','utf-8') as f:
    g = f.read()

print(g)




