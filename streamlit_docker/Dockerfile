FROM ubuntu:latest

WORKDIR /app

RUN apt-get update && apt-get install -y \
    apt-utils \
    locales \
    python3-pip \
    python3-yaml \
    && apt-get clean

RUN pip3 install --upgrade pip

RUN pip3 install streamlit

RUN pip3 snowflake-snowpark-python

COPY / ./

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
