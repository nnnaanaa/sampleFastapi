# Python 2.7 のイメージをベースにする
FROM python:2.7

# 必要なパッケージをインストール
RUN pip install requests

# ワーキングディレクトリを設定
WORKDIR /app

# サーバー用の Python スクリプトをコピー
COPY server.py /app/

# クライアント用の Python スクリプトをコピー
COPY client.py /app/

# サーバーを起動
CMD ["python", "server.py"]

