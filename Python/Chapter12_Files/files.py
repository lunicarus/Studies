import pathlib as pl
# path = "/home/lucas/Documentos/Studies"
# print()
# desafio = pl.Path.home() / "DESAFIO.txt"
# sus = pl.Path.home() / "sus.txt"
# home = pl.Path.home()
# print(f"\n{desafio}\n")
    # && Review Exercises chapter 12.2
    # home = pl.Path.home()
    # my_folder = home / "sus.txt"
    # print(my_folder.is_file())
    # print(my_folder.name)

new_dir = pl.Path.home() / "new_directory"
nested_dir = new_dir / "false_directory"
new_dir.mkdir(exist_ok=True) #Creates Path if it doesn't exists
nested_dir.mkdir(parents=True,exist_ok=True) #Creates Path and all parents if necessary

file_path = nested_dir / "new_file.txt"

file_path.parent.mkdir(exist_ok=True) #? already created
file_path.touch() #Creates a file, similar to .mkdir()
# for path in nested_dir.iterdir(): #glob(*.txt) would find only the .txt documents.
#     print(path)
    
# source =  pl.Path.home() / "/home/luni/Documents/Studies/NewSpace.txt"
# destination = nested_dir / "NewSpace.txt"
# # source.touch()
# source.replace(destination)
arquive = file_path.open(mode="r", encoding="utf-8")
with open(file_path,mode="r", encoding="utf-8") as file:
    text = file.read()

print(text)