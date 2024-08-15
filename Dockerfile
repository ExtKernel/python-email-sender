FROM python:3.12.5-bullseye
LABEL authors="exkernel"

WORKDIR /app

COPY . /app

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN python -m venv venv && \
    source venv/bin/activate && \
    pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run"]
