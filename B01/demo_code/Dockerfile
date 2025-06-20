FROM jupyter/all-spark-notebook:python-3.11

USER root

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

USER $NB_UID

WORKDIR /home/jovyan/work