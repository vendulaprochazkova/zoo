rok = 2025
text = "vesele vanoce"
cislo = 51054601

#fstring
print(f"ahoj, {text} {rok}")

#oddelovactisicu
print(f"{cislo:, }")

#ukol 1
jmeno = input("zadejte sve jmeno")
vek = input("zadejte svuj svek")

print(f"ahoj, jmenuji se {jmeno} a je mi {vek} let.")

#ukol 2
cislo1 = float(input("zadej 1 desetine cislo"))
cislo2 = float(input("zadej 2. cislo"))
soucet = cislo1/cislo2
rozdil = cislo1-cislo2
soucin = cislo1*cislo2
podil = cislo1/cislo2 if cislo2 != 0 else "nedefinovano (deleni nulou)"
print
print
print
print
