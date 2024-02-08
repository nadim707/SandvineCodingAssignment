FROM python:3.10-slim
#LABEL Maintainer="nadim.warsi"

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app

CMD ["python3", "http_stats.py"]
