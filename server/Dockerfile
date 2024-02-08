# ベースイメージを指定
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# 必要なファイルをコピー
COPY . /usr/src/app/server

# 作業ディレクトリを設定
WORKDIR /usr/src/app/server

# requirements.txtからパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# FastAPIのポートをエクスポート
EXPOSE 5000

# イメージ内でコマンドを実行（FastAPIサーバーを起動）
CMD ["uvicorn", "server:app", "--port", "5000", "--reload"]
