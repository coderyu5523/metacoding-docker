FROM python:3.7-alpine

WORKDIR /app
COPY app.py .
RUN pip install flask

EXPOSE 5000
CMD ["python", "app.py"]
