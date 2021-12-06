# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-buster

EXPOSE 8080

WORKDIR /app
ADD . /app
ENV DEBUG=False
ENV HOST=0.0.0.0
ENV PORT=8080

ENV APP_LANG=en
ENV X_API_KEY=123qwe
ENV FLASK_APP=server.py



RUN python3 -m pip install gunicorn
RUN python3 -m pip install -r requirements.txt


ENV TZ=Europe/Istanbul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Disable CipherString in OPENSSL Config

RUN sed -i "s/CipherString = DEFAULT@SECLEVEL=2/#CipherString = DEFAULT@SECLEVEL=2/g" /etc/ssl/openssl.cnf


#CMD ["python3","server.py"]

CMD ["gunicorn", "-w","4", "server:app"]