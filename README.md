# usage-detail
## 概要  
Single Page Applicationで構築したクレジットカードの会員情報を取得するためのアプリ。  
当リポジトリはFlaskのBackend for Frontendになります。  
利用する際には以下の環境設定をした前提に行ってください。  
  
## 環境設定
### Pythonのインストール
当リポジトリはPython3.7.4の環境で動いているため、以下のURLからanacondaをダウンロードし、インストールしてください。  
[anaconda3のダウンロード](https://repo.anaconda.com/archive/Anaconda3-2019.10-Windows-x86_64.exe)  
  
### Gitのインストール
Githubから当リポジトリを利用する際にはローカル環境にGitをインストールする必要があります。  
[Gitのダウンロード](https://github.com/git-for-windows/git/releases/download/v2.25.0.windows.1/Git-2.25.0-64-bit.exe)  

### TortoiseGitのインストール
Gitのコマンドを覚えるのが面倒である場合は以下のアプリをインストールして利用してください。SVNと同じ間隔で利用できます。  
[TortoiseGitのダウンロード](https://github.com/git-for-windows/git/releases/download/v2.25.0.windows.1/Git-2.25.0-64-bit.exe)  

### Gitのリモートリポジトリの初期取得
リモートリポジトリをGit Cloneコマンドで取得して下さい。  
`git clone https://github.com/junTaniguchi/usage-detail.git`  

### Gitの同期  
リモートリポジトリ上の最新の資材をローカルへ持ってくる際は以下のコマンドかコンテキストメニューのTortoiseGitから「Git同期」-> 「プル」から取得してください。  
`git pull origin master`  

### Gitの更新  
更新した場合は以下のコマンドかコンテキストメニューのTortoiseGitから「Gitコミット -> master」からコミットしてください。  
`git add .`  
`git commit origin master`  

## アプリ稼働方法
コマンドプロンプトにて当リポジトリまでcdで移動し、以下のコマンドを実行してください。  
`python index.py`  
  
## メインページのURL  
上記コマンドでアプリが稼働したあとは以下のURLでメインのページを確認することができます。  
http://localhost:5000/

