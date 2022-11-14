# spike.py

spike.pyは作業用のフォルダを作成するためのPythonで作成したシェルコマンドです

使い方は以下になります

~~~shell
~/bin/spike.py 作業名
~~~

引数で指定した作業名に、連番のプレフィックスを付けた作業フォルダを作成し、そのフォルダをVsCodeでオープンします

作業フォルダは、`~/spike`配下に作成します

`~/spike`になにもなければ、01のプレフィックスのついて作業フォルダを作成します

`~/spike`が以下のような場合は、連番の最後に1プラスした13をプレフィックスとして使用します

~~~shell
$ ls ~/spike
01_xxx
02_xxx
09_xxx
12_xxx
~~~~

そのため、以下を実行すると

~~~shell
$ ~/bin/spike.py spike_command
creating 13_spike_command ...
$ ls
01_xxx
02_xxx
09_xxx
12_xxx
13_spike_command
~~~

## インストール方法

以下を実行すると、`~/bin`に`spike.py`をコピーし、実行権限を付与します。

~~~shell
make
~~~
