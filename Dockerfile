FROM python:3.9-slim


COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY src/ /app/


WORKDIR /app/



CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5050", "app:app"]
