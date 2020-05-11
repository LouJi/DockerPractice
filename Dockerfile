FROM python3.6

COPY ./opt/

WORKDIR /opt

ENTRYPOINT ["python", "test.py"]
