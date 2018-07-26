FROM python:3.6-slim 

COPY requirements.txt /tmp

WORKDIR /tmp

RUN pip3 install -r requirements.txt

COPY app.py .
COPY data.py .

EXPOSE 8050

CMD python3 app.py 
