FROM python:3.10-bullseye

RUN mkdir "/custom"
ENV PYTHONPATH=/custom/assistant/

COPY assistant/ /custom/assistant/
COPY secrets/ /custom/secrets/

COPY requirements.txt /datadogs/requirements.txt
COPY main.py /datadogs/main.py

WORKDIR /datadogs
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]
