FROM python:3.6-alpine

WORKDIR /app
COPY ./requirements.txt ./ 
COPY ./server.py ./ 
COPY ./do_db_stuff.py ./ 
RUN python -m pip install -r ./requirements.txt
RUN date -R > ./version.txt

CMD ["python", "-m", "http.server", "8000"]
