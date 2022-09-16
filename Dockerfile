FROM python:3.9

COPY . /opt/services/web_app/src
WORKDIR /opt/services/web_app/src

# Install reqs
RUN echo 'deb http://deb.debian.org/debian testing main' >> /etc/apt/sources.list
COPY install-packages.sh .
RUN chmod 755 ./install-packages.sh

# populate "ocbcinst.ini" as this is where ODBC driver config sits
RUN echo "[FreeTDS]\n\
Description = FreeTDS unixODBC Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini

RUN pip install -r requirements.txt
