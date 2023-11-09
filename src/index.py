from varasto import Varasto


def main():

    print("Tervetuloa, tässä tiedot:")

    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

    print("Liian pitkä rivi Liian pitkä rivi Liian pitkä rivi Liian pitkä rivi")

if __name__ == "__main__":
    main()
