first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
#Quando usamos o f, as variaveis entre {} sao substituidas pelos seus valores, neste caso pelos nomes ada e lovelace
print(full_name)
message=f"Hello, {full_name.title()}!"
print(message)
print("\t"f"{message}")
#t faz tab
#n faz nova linha
print("\n"f"{message}")
#para tirar espaços em branco desnecessarios usar o comando .rstrip (right) .lstrip(left) .strip (dos dois lados)
favorite_language="python "
print(favorite_language)
print(favorite_language.rstrip())