FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY . ./

RUN pip3 install --upgrade pip
RUN pip3 install requests

# サーバーを起動
CMD ["python", "client.py"]
