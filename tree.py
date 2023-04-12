from pathlib import Path
import sys
tree_str = ''
black_name = ['.idea', 'node_modules', '.git']

def generate_tree(pathname, n=0, deep=3):
    if n > deep:
        return
    global tree_str
    if pathname.is_file():
        tree_str += '    |' * n + '-' * 4 + pathname.name + '\n'
    elif pathname.is_dir():
        if str(pathname)[str(pathname).rfind('\\')+1:] in black_name:
            return
        tree_str += '    |' * n + '-' * 4 + \
            str(pathname.relative_to(pathname.parent)) + '\\' + '\n'
        for cp in pathname.iterdir():
            generate_tree(cp, n + 1, deep)


generate_tree(Path(sys.argv[1]), deep=3)
print(tree_str)
    