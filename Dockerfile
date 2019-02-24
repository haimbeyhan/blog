FROM ubuntu:18.04
RUN mkdir /app
COPY blog.py requirements.txt /app/
COPY templates /app/templates
WORKDIR /app
RUN apt-get update && apt install python3-pip -y --no-install-recommends
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
