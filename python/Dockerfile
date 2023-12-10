FROM python:3.9
LABEL authors="watanabemiku"

ENV WORK_DIR /work
WORKDIR ${WORK_DIR}

RUN pip install -U \
        setuptools \
        pip && \
    pip install pipenv
RUN apt update -y
RUN apt-get install tk -y
COPY ./src ${WORK_DIR}/src
COPY ./DevGPT ${WORK_DIR}/DevGPT
COPY ./requirements.txt ${WORK_DIR}/requirements.txt

RUN pip install -r requirements.txt
WORKDIR ${WORK_DIR}/src

ENTRYPOINT ["python","-m", "main"]