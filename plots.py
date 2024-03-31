import matplotlib.pyplot as plt
import numpy as np
genre = ["Ambient", "Atmospheric Black", "Black", "Brutal Death", "Death", 
         "Deathcore", "Doom", "Folk", "Gothic", " Grindcore", "Groove", "Hardrock", 
         "Hardcore (Punk)", "Heavy", "Metalcore","Power", "Sludge Metal", "Trash", " Speed", "Stoner"]
samples = [154, 211, 2597, 301, 2309, 178, 856, 232, 278, 483, 593, 393, 172, 1952, 407, 459, 383, 2196, 200, 336]
    #plot diagram 
plt.bar(range(len(genre)), samples, width=0.5)
plt.xticks(rotation=90)

plt.title("Samples per Subgenre")
plt.ylabel("Number of samples")
plt.xticks(range(len(genre)), genre)

plt.show()