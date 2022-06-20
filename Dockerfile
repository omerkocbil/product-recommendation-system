FROM python:3.8
ARG PORT

WORKDIR /product-recommendation-system

COPY ./requirements.txt /product-recommendation-system/requirements.txt
COPY ./code /product-recommendation-system/code
 
RUN pip install --no-cache-dir --upgrade -r /product-recommendation-system/requirements.txt

EXPOSE $PORT
 
CMD gunicorn code.api.main:app --bind 0.0.0.0:$PORT --worker-class uvicorn.workers.UvicornWorker
