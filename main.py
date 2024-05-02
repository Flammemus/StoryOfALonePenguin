import time
from ascii_magic import AsciiArt

def textAnim(text):
    print()
    time.sleep(2)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.075)
    time.sleep(2)
    print()

def slideshow(image, text):
    print()
    print("@*================================================================================================*@")
    my_art = AsciiArt.from_image(image)
    my_art.to_terminal(columns=100)
    print("@*================================================================================================*@")

    textAnim(text)

def main():
    slideshow("images/antarktis.png", "På den øde Antarktis, finner vi en liten flokk av pengviner.")
    slideshow("images/penguinFamily.jpg", "Pingvinflokken befinner seg mellom to interessepunkt.")
    slideshow("images/lonePenguin.jpg", "Halvparten gikk mot spiseplassen, mens de den andre halvparten gikk mot havet.")
    slideshow("images/lonePenguin2.webp", "Men en pengvin tar vår oppmerksomhet. Den befinner seg i midten av flokken, usikker på hvem den skal følge")
    textAnim("Pengvinen kan velge mellom:")
    textAnim("- Spiseplassen")
    textAnim("- Havet")
    print()
    action = input("Hvor tror du pengvinen vandrer? (1/2): ")

    if action:
        textAnim("Det trodde vi også")

    textAnim("Men etter vår observasjon, vralter pengvinen mot fjellene")
    slideshow("images/mountains.jpg", "Vralter mot sin sikre død.")

main()