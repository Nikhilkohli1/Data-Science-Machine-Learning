FROM continuumio/anaconda3:4.4.0
MAINTAINER Nikhil Kohli

COPY . /Streamlit Webapp

EXPOSE 8501

WORKDIR /Streamlit Webapp

RUN pip install -r requirements.txt

CMD streamlit run app.py