FROM python:3.10-bullseye

RUN mkdir "/custom"
ENV PYTHONPATH=/custom/assistant/

COPY assistant/ /custom/assistant/
COPY secrets/ /custom/secrets/

COPY requirements.txt /custom/requirements.txt
COPY main.py /custom/main.py

WORKDIR /custom
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]
