# KishuKernel

1. pip install
2. kishu-kernel install
3. jupuyter lab

kishuのビルド方法
cd kishu
pip install .
cd ..
python -c "from kishu import init_kishu"
kishuに入ってやらないとこうなる
```
> # matsumotoryutaro @ matsumotonoMacBook-Air in ~/programs/KishuKernel/kishu on git:main o .venv [20:03:29] C:1
$ python -c "from kishu import init_kishu"
(.venv)
# matsumotoryutaro @ matsumotonoMacBook-Air in ~/programs/KishuKernel/kishu on git:main o .venv [20:03:38]
$ cd ..
(.venv)
# matsumotoryutaro @ matsumotonoMacBook-Air in ~/programs/KishuKernel on git:main o .venv [20:03:53]
$ python -c "from kishu import init_kishu"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: cannot import name 'init_kishu' from 'kishu' (unknown location)
(.venv)
```
