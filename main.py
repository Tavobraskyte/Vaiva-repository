import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('tavo_nuotrauka.jpg')
plt.imshow(img)
plt.axis('off')
plt.show()

img_array = np.array(img)
h, w, c = img_array.shape
x,y=(4060,2983)
[58,52,56]

                   #object cutting

# Pirma priskiriame img_parts reikšmes
img_part1 = img_array[0:h//2, 0:w//2]
img_part2 = img_array[:h//2, w//2:w]
img_part3 = img_array[h//2:h, 0:w//2]
img_part4 = img_array[h//2:h, w//2:w]

# Tada parodome img_part1 naudojant plt.imshow()
plt.imshow(img_part1)
plt.axis('off')  # Paslepia ašis
plt.show()
plt.title('Iškirpta viršutinė kairė dalis')

# Tada parodome img_part2 naudojant plt.imshow()
plt.imshow(img_part2)
plt.axis('off')  # Paslepia ašis
plt.show()
plt.title('Iškirpta viršutinė dešinė dalis')

# Tada parodome img_part3 naudojant plt.imshow()
plt.imshow(img_part3)
plt.axis('off')  # Paslepia ašis
plt.show()
plt.title('Iškirpta apatinė dešinė dalis')

# Tada parodome img_part4 naudojant plt.imshow()
plt.imshow(img_part4)
plt.axis('off')  # Paslepia ašis
plt.show()
plt.title('Iškirpta apatinė kairė dalis')


                 #img_part1 sukimas

# Įkeliam nuotrauką
img = Image.open('tavo_nuotrauka.jpg')

# Konvertuojam nuotrauką į masyvą
img_array = np.array(img)
h, w, c = img_array.shape

# Iškirpiame viršutinę kairę nuotraukos dalį (img_part1)
img_part1 = img_array[0:h//2, 0:w//2] # Viršutinis kairysis kampas

# Parodome originalią iškirptą nuotraukos dalį
plt.imshow(img_part1)
plt.axis('off')  # Paslepia ašis
plt.title('Iškirpta viršutinė kairė dalis')
plt.show()

# Sukame img_part1 270 laipsnių kampu
img_part1_rotated = np.rot90(img_part1, k=3)  # Sukimas 270 laipsnių

# Parodome suktą img_part1 dalį
plt.imshow(img_part1_rotated)
plt.axis('off')  # Paslepia ašis
plt.title('Sukta viršutinė kairė dalis 270 laipsniu')
plt.show()

# Sukame img_part1 180 laipsnių kampu
img_part1_rotated = np.rot90(img_part1, k=2)  # Sukimas 180 laipsnių

# Parodome suktą img_part1 dalį
plt.imshow(img_part1_rotated)
plt.axis('off')  # Paslepia ašis
plt.title('Sukta viršutinė kairė dalis  180 laipsnių')
plt.show()

# Sukame img_part1 90 laipsnių kampu
img_part1_rotated = np.rot90(img_part1, k=1)  # Sukimas 90 laipsnių

# Parodome suktą img_part1 dalį
plt.imshow(img_part1_rotated)
plt.axis('off')  # Paslepia ašis
plt.title('Sukta viršutinė kairė dalis  90 laipsnių')
plt.show()


                   #img_part2 sukimas

# Įkeliam nuotrauką
img = Image.open('tavo_nuotrauka.jpg')

# Konvertuojam nuotrauką į masyvą
img_array = np.array(img)
h, w, c = img_array.shape

# Pirma priskiriame img_part2 reikšmę
img_part2 = img_array[:h//2, w//2:w]   # Viršutinis dešinysis kampas

# Parodome originalią iškirptą nuotraukos dalį
plt.imshow(img_part2)
plt.axis('off')  # Paslepia ašis
plt.title('Iškirpta viršutinė dešinė dalis')
plt.show()

   # Sukame img_part2 270 laipsnių kampu
img_part2_rotated = np.rot90(img_part2, k=3)  # Sukimas 270 laipsnių

# Parodome suktą img_part2 dalį
plt.imshow(img_part2_rotated)
plt.axis('off')  # Paslepia ašis
plt.title('Sukta viršutinė dešinė dalis 270 laipsnių')
plt.show()

   # Sukame img_part1 180 laipsnių kampu
img_part2_rotated = np.rot90(img_part2, k=2)  # Sukimas 180 laipsnių

# Parodome suktą img_part dalį
plt.imshow(img_part2_rotated)
plt.axis('off')  # Paslepia ašis
plt.title('Sukta viršutinė dešinė dalis 180 laipsnių')
plt.show()

   # Sukame img_part1 90 laipsnių kampu
img_part2_rotated = np.rot90(img_part2, k=1)  # Sukimas 90 laipsnių

# Parodome suktą img_part dalį
plt.imshow(img_part2_rotated)
plt.axis('off')  # Paslepia ašis
plt.title('Sukta viršutinė dešinė dalis 90 laipsnių')
plt.show()

                 #part3 sukimas

# Įkeliam nuotrauką
img = Image.open('tavo_nuotrauka.jpg')

# Konvertuojam nuotrauką į masyvą
img_array = np.array(img)
h, w, c = img_array.shape

# Pirma priskiriame img_part3 reikšmę
img_part3 = img_array[h//2:h, 0:w//2]  # Apatinis dešinysis kampas

# Parodome originalią iškirptą nuotraukos dalį
plt.imshow(img_part3)
plt.axis('off')  # Paslepia ašis
plt.title('Iškirpta apatinė dešinė dalis')
plt.show()

# Sukame img_part3 270 laipsnių kampu
img_part3_rotated = np.rot90(img_part3, k=3)  # Sukimas 270 laipsnių

# Parodome suktą img_part3 dalį
plt.imshow(img_part3_rotated)
plt.axis('off')  # Paslepia ašis
plt.title('Sukta apatine dešinė dalis 270 laipsnių')
plt.show()

   # Sukame img_part3 180 laipsnių kampu
img_part3_rotated = np.rot90(img_part3, k=2)  # Sukimas 180 laipsnių

# Parodome suktą img_part3 dalį
plt.imshow(img_part3_rotated)
plt.axis('off')  # Paslepia ašis
plt.title('Sukta apatine dešinė dalis 180 laipsnių')
plt.show()

   # Sukame img_part3 90 laipsnių kampu
img_part3_rotated = np.rot90(img_part3, k=1)  # Sukimas 90 laipsnių

# Parodome suktą img_part3 dalį
plt.imshow(img_part3_rotated)
plt.axis('off')  # Paslepia ašis
plt.title('Sukta apatine dešinė dalis 90 laipsnių')
plt.show()

                 #img_part4 sukimas

# Įkeliam nuotrauką
img = Image.open('tavo_nuotrauka.jpg')

# Konvertuojam nuotrauką į masyvą
img_array = np.array(img)
h, w, c = img_array.shape

# Iškirpiame apatinę kairę nuotraukos dalį (img_part4)
img_part4 = img_array[h//2:h, w//2:w]  # Apatinis kairysis kampas

# Parodome originalią iškirptą nuotraukos dalį
plt.imshow(img_part4)
plt.axis('off')  # Paslepia ašis
plt.title('Iškirpta apatinė kairė dalis')
plt.show()

   # Sukame img_part4 270 laipsnių kampu
img_part4_rotated = np.rot90(img_part4, k=3)  # Sukimas 270 laipsnių

# Parodome suktą img_part4 dalį
plt.imshow(img_part4_rotated)
plt.axis('off')  # Paslepia ašis
plt.title('Sukta apatinė kairė dalis 270 laipsnių')
plt.show()

   # Sukame img_part4 180 laipsnių kampu
img_part4_rotated = np.rot90(img_part4, k=2)  # Sukimas 180 laipsnių

# Parodome suktą img_part4 dalį
plt.imshow(img_part4_rotated)
plt.axis('off')  # Paslepia ašis
plt.title('Sukta apatinė kairė dalis 180 laipsnių')
plt.show()

# Sukame img_part4 90 laipsnių kampu
img_part4_rotated = np.rot90(img_part4, k=1)  # Sukimas 90 laipsnių

# Parodome suktą img_part4 dalį
plt.imshow(img_part4_rotated)
plt.axis('off')  # Paslepia ašis
plt.title('Sukta apatinė kairė dalis 90 laipsnių')
plt.show()

            #supjaustytu ir pasuktu daliu sujungimas atgal
final_image = np.vstack([
    np.hstack([img_part1_rotated, img_part2_rotated]),
    np.hstack([img_part3_rotated, img_part4_rotated])
])
plt.imshow(final_image)
plt.axis('off')
plt.show()

