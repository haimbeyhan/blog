FROM flask:latest
RUN mkdir /app
COPY blog.py /app/app.py
COPY templates /app/templates
WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["app.py"]
