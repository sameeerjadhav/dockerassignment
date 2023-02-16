FROM python:3.8-alpine

WORKDIR /home/data

COPY ./Limerick.txt /home/data/Limerick.txt

COPY ./IF.txt /home/data/IF.txt

COPY ./result.txt /home/output/result.txt

COPY ./main.py .

CMD ["python","./main.py"]
