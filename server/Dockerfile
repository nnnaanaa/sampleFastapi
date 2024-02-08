FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY . ./

RUN pip3 install --upgrade pip
RUN pip3 install fastapi
RUN pip3 install "uvicorn[standard]"
RUN pip3 install requests

EXPOSE 5000

ENTRYPOINT ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
