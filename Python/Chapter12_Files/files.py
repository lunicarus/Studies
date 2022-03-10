import pathlib as pl
# path = "/home/lucas/Documentos/Studies"
# print()
# desafio = pl.Path.home() / "DESAFIO.txt"
# sus = pl.Path.home() / "sus.txt"
# home = pl.Path.home()
# print(f"\n{desafio}\n")
# Todo Review Exercises chapter 12.2
# home = pl.Path.home()
# my_folder = home / "sus.txt"
# print(my_folder.is_file())
# print(my_folder.name)

new_dir = pl.Path.home() / "new_directory"
nested_dir = new_dir / "false_directory"
new_dir.mkdir(exist_ok=True) # Creates Path if it doesn't exists
# nested_dir.mkdir(parents=True) #Creates Path and all parents if necessary

# file_path = nested_dir / "new_file"
# print(file_path.parent)

# file_path.parent.mkdir() # todo already created
# file_path.touch() # todo already created
for path in nested_dir.iterdir(): #glob(*.txt) would find only the .txt documents.
    print(path)
