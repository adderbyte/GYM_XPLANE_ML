
# We won't install debian packages, so just use the slim variant.
FROM python:3.6-slim

# Install required python packages
# Note: This way of formating the instruction allows to easily
# add/remove/comment packages


#RUN pip install --trusted-host pypi.python.org -r	requirements.txt
RUN pip install --no-cache-dir \
        numpy==1.11.3 \
        jupyter \
        scipy \
        sklearn \
        pandas \
        datetime \
        matplotlib\
	plotly\
	xlrd\
        ipywidgets \
        ;

# Use /work as the working directory
RUN mkdir -p /work
WORKDIR /work

# Include the notebook
ADD OutputDATA.xlsx  /work/OutputDATA.xlsx
ADD casestudy.ipynb /work/casestudy.ipynb

# Setup jupyter notebook as the default command
# This means that jupyter notebook is launched by default when doing `docker run`.
# Options:
#   --ip=0.0.0.0 bind on all interfaces (otherwise we cannot connect to it)
#   --allow-root force jupyter notebook to start even if we run as root inside the container
#   --NotebookApp.default_url=/notebooks/casestudy.ipynb Open the notebook by default
CMD [ "jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.default_url=/notebooks/casestudy.ipynb" ]

# Declare port 8888
EXPOSE 8888

