FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip --version

RUN pip install requests packaging

COPY check_versions.py .

RUN python check_versions.py

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]