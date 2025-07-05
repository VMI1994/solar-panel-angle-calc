FROM python
RUN apt update && DEBIAN_FRONTEND=noninteractive apt upgrade -y
RUN apt install -y python3-pip python3-requests
RUN pip install requests
COPY . .
CMD ["python3", "solar.py"]
