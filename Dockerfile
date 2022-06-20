FROM python:3.8

WORKDIR /product-recommendation-system

COPY ./requirements.txt /product-recommendation-system/requirements.txt
COPY ./Procfile /product-recommendation-system/Procfile
 
RUN pip install --no-cache-dir --upgrade -r /product-recommendation-system/requirements.txt
 
COPY ./code /product-recommendation-system/code
 
CMD gunicorn code.api.main:app --bind 0.0.0.0:5000 --preload
