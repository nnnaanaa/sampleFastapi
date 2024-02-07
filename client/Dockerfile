# Python 2.7 のイメージをベースにする
FROM python:2.7

# 必要なパッケージをインストール
RUN pip install requests

# ワーキングディレクトリを設定
WORKDIR /usr/src/app

# サーバーを起動
CMD ["python", "client.py"]