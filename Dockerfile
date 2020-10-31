FROM python:3-slim-buster
LABEL MAINTAINER="jnmcfly"
COPY requirements.txt /app/req.txt
COPY main.py /app/main.py
WORKDIR /app/
RUN pip install --no-cache-dir -r req.txt
CMD /usr/local/bin/python /app/main.py