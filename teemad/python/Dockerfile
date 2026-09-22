FROM python:3.12-slim

COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install --no-cache-dir -r /tmp/requirements.txt

# Ajutised Jupyteri ja Matplotlibi failid jäävad konteinerisse.
ENV HOME=/tmp
WORKDIR /workspace
USER 1000:1000
EXPOSE 8888

CMD ["python", "-m", "jupyterlab", "--no-browser", "--ServerApp.ip=0.0.0.0", "--ServerApp.port=8888", "--ServerApp.port_retries=0", "--ServerApp.root_dir=/workspace"]
