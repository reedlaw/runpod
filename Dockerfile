FROM python:3.10-slim

WORKDIR /
RUN pip install --no-cache-dir runpod
RUN pip install spacy
RUN python -m spacy download en_core_web_lg
COPY rp_handler.py /

# Start the container
CMD ["python3", "-u", "rp_handler.py"]