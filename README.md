<h1 align="center">
    Dir-Tree
</h1>
<h4 align="center">
     Generate a directory tree based on directories
</h4>
<p align="center">
    <a href="#">
        <img src="https://img.shields.io/badge/dir tree-1.0.0-green.svg" alt="tree">
    </a>
</p>

### 示例
```
----dir\
    |----.gitignore
    |----client\
    |    |----.gitignore
    |    |----package.json
    |    |----README.md
    |    |----src\
    |    |    |----api\
    |----LICENSE
    |----README.md
    |----server\
    |    |----requirements.txt
```
### 使用

```sh
python tree.py <dir_path>
```
### 此外
```
// 如果不想调用python构建程序，可以使用已经打包好的安装程序
release > DirTree.exe
```