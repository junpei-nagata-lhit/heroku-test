# Heroku 使い方

## 概要
Herokuでは、dynoというコンテナが起動して処理が実行される。<br/>
そのため、コンテナが利用できるファイルは連携されているGitレポジトリに存在するものとなる。<br/>
また、コンテナが停止すると処理して作成されたデータもなくなるので、外部に保存する必要がある。<br/>
（HerokuはWebアプリのデプロイ用に使用し、外部のDBサーバーと連携してデータを保持するイメージ）


## Herokuの実行の流れ
1. コンテナ起動
2. Gitレポジトリをクローン (ただし、.gitはないので厳密にはcloneしているわけではなさそう)
3. 処理
4. 停止; データがなくなる


## 0. Heroku プロジェクトの作成
ブラウザ上で、Herokuのプロジェクトを作成<br/>
（プロジェクト名はHerokuユーザー全体で共通。簡単にしすぎたりしない、テスト時には連番を振る、testと明記する、等した方がいい気がする）

## 1. Heroku Git, GitHub 連携
作成したプロジェクトにGitレポジトリを連携

## 2. Gitレポジトリにファイルをプッシュ
Python の場合には以下を配置 (タスクスケジューラ的な簡易な仕様を目的)

* requirements.txt<br/>
    pipでインストールするパッケージ名を列挙<br/>
    e.g.) pydrive

* 実行ファイル

`Procfile`はHeroku Schedulerでは不要<br/>
dynosを起動したい場合、<br/>
起動するdynos(プロセスコンテナ)を列挙<br/>
e.g.) worker: python src/write_test.py

## 3. Heroku Scheduler の設定
Heroku Scheduler add on をHerokuのプロジェクトに追加し、<br/>
実行ファイルを実行する任意のタスクを設定
