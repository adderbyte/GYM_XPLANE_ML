-----------------------
##### Headless Plane Mode
-----------------------

In this section, the aim is to document how to run:
  * X-Plane in a Headless mode (Without the Xserver or the graphics interface). This will enable deploying xplane on servers without dedicate user interface (for example on  Amazon cloud -- bearing in mind each version deployed must have its own licence).
  * It is also preferable to run with XServer or the graphics interface for the first time to ensure everything is working as intended. Afterwards in order to deploy agent algorithm on large scale there should be no need for the GUI or XServer. Headless mode will save a lot in computation cost and time.
  * Investigate Docker set up for running xplane

--------
##### Headless Mode (UNIX OR LINUX DISTRO)
------
Assumes that XPlane has been installed.
 
 1. Install  [XVFB](https://www.x.org/archive/X11R7.6/doc/man/man1/Xvfb.1.xhtml) 
 2. Put bash file in XPlane folder.
 3. change directory to the XPlane folder
 3. Run Bash file
