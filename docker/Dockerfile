FROM python:3.12-slim
workdir /app
copy rick_morty_REST.py /app/
RUN pip install flask && pip install requests
EXPOSE 5000
CMD ["python", "rick_morty_REST.py"]