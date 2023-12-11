FROM python:3.9

ENV WORK_DIR /work
WORKDIR ${WORK_DIR}

RUN pip install -U \
        setuptools \
        pip && \
    pip install pipenv
RUN apt update -y
RUN apt-get install tk unzip -y
COPY ./src ${WORK_DIR}/src
COPY ./requirements.txt ${WORK_DIR}/requirements.txt

RUN pip install -r requirements.txt
WORKDIR ${WORK_DIR}/src

ENTRYPOINT ["python","-m", "main"]