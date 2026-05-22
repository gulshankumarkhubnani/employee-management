FROM python:3.11-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.11-slim AS runner
WORKDIR /app
RUN groupadd -g 10001 appuser && useradd -u 10001 -g appuser -s /bin/bash -m appuser
COPY --from=builder /root/.local /home/appuser/.local
COPY app/ ./app/

ENV PATH=/home/appuser/.local/bin:$PATH
ENV PYTHONUMBUFFERED=1

EXPOSE 8000
USER appuser
CMD ["uvicorn", "app.main:app","--host", "0.0.0.0", "--port", "8000"]
