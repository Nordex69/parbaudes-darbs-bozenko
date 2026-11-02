Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> skaits = {}
... 
... with open("sistema.log", encoding="utf-8") as f:
...     for rinda in f:
...         limenis = rinda.split()[2]
... 
...         if limenis in skaits:
...             skaits[limenis] += 1
...         else:
...             skaits[limenis] = 1
... 
... print("Limenu kopsavilkums")
... 
... sakartots = sorted(skaits.items(), key=lambda x: x[1], reverse=True)
... 
... for limenis, skaits in sakartots:
