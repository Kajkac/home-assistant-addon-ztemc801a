FROM python:3.8-alpine

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY run.py /

CMD ["python", "-u", "run.py"]
