import shutil
from pathlib import Path

base_path = Path('ops_example')
base_path2 = Path('ops_example/D')

# base_path.mkdir()

path_b = base_path/'A'/'B'
# path_b.mkdir(parents=True)
path_d = base_path/'A'/'D'

for filename in ('ex1.txt','ex2.txt','ex3.txt' ):
    with open(path_b / filename, 'w', encoding='utf-8') as stream:
        stream.write(f"cos tam{filename}")

shutil.move(path_b,path_d)

ex1 = path_d /('ex1.txt')
ex1.rename(ex1.parents/'nowa_nazwa.log')

