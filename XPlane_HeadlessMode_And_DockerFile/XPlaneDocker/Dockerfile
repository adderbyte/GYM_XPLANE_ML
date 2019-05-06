FROM ubuntu:18.04 as base                 
MAINTAINER adderbyte  adderbyte@icloud.com


################### Run required installation and set Work directory##################
# installation
RUN \
     apt-get update  -y && \
     apt-get install  -y software-properties-common && \
     apt-get install -y xvfb &&  \
     apt-get install -y xvfb xserver-xephyr  &&  \
     apt-get install -y vnc4server &&  \
     apt-get install -y p7zip-full   \
      && rm -rf /var/lib/apt/lists/* /var/cache/apt/*
     
# work drectory
RUN mkdir -p /work
WORKDIR /work
########################################################################################

######################################## ADD FILES ####################################
# Add xplane tar files and script
ADD XPlane11.tar.7z  /work/XPlane11.tar.7z
ADD XPlaneBashFile.sh /work/XPlaneBashFile.sh
########################################################################################

######################################## Uncompress the files ##########################
# Uncompress the xplane tar files 
RUN 7z x -so /work/XPlane11.tar.7z | tar -xf - -C /work
########################################################################################


######################################## Run in headlessmode ##########################
# run the simulation in headless mode
# CMD /work/XPlaneBashFile.sh # either use a script using this syntax
# CMD ["chmod", "+x", ".63./XPlaneBashFile.sh"] ## either use a script using this oter syntax
####### the preferred way to start the simulation in headless mode
ENTRYPOINT ["xvfb-run"] # entry point 
CMD ["--server-args=':1 -screen 0, 1024x768x16'", "/work/X-Plane\ 11/X-Plane-x86_64 > /dev/null &"] # command flags
########################################################################################

######################################## Declare port ##########################
# Declare xplane port to enable connection with gym xplane
EXPOSE 49009
########################################################################################
