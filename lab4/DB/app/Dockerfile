FROM python:3.11
RUN apt-get update && \
    apt-get install -y \
        libasound2 \
        libgconf-2-4 \
        libgtk-3-dev \
        libnotify-dev \
        libnss3 \
        libxss1 \
        xvfb

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5555
USER nonroot

CMD ["python", "app.py"]