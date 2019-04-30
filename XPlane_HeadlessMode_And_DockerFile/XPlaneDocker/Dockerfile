FROM ubuntu:18.04 as base
MAINTAINER Admatic Engineering adderbyte@icloud.com
### Stage 1 - add/remove packages ###



RUN \
     apt-get update  -y && \
     apt-get install  -y software-properties-common && \
     apt-get install -y xvfb &&  \
     apt-get install -y xvfb xserver-xephyr  &&  \
     apt-get install -y vnc4server &&  \
     apt-get install -y p7zip-full   \
      && rm -rf /var/lib/apt/lists/* /var/cache/apt/*
     

RUN mkdir -p /work
WORKDIR /work

# Include the notebook
ADD XPlane11.tar.7z  /work/XPlane11.tar.7z
ADD XPlaneBashFile.sh /work/XPlaneBashFile.sh

#RUN  7z -xvf  /work/XPlane11.tar.7z

RUN 7z x -so /work/XPlane11.tar.7z | tar -xf - -C /work

# Setup jupyter notebook as the default command
# This means that jupyter notebook is launched by default when doing `docker run`.
# Options:
#   --ip=0.0.0.0 bind on all interfaces (otherwise we cannot connect to it)
#   --allow-root force jupyter notebook to start even if we run as root inside the container
#   --NotebookApp.default_url=/notebooks/casestudy.ipynb Open the notebook by default
#CMD [ "jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.default_url=/notebooks/casestudy.ipynb" ]

#CMD /work/XPlaneBashFile.sh
#CMD ["chmod", "+x", ".63./XPlaneBashFile.sh"]
ENTRYPOINT ["xvfb-run"]
CMD ["--server-args=':1 -screen 0, 1024x768x16'", "/work/X-Plane\ 11/X-Plane-x86_64 > /dev/null &"]

#CMD /work/XPlaneBashFile.sh

#CMD ["echo", "Running"]
# Declare port 8888
EXPOSE 49009

