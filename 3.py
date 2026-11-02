skaits = {}

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        limenis = rinda.split()[2]

        if limenis in skaits:
            skaits[limenis] += 1
        else:
            skaits[limenis] = 1

print("Limenu kopsavilkums")

sakartots = sorted(skaits.items(), key=lambda x: x[1], reverse=True)

for limenis, skaits in sakartots:
    print(limenis, skaits)
