To deploy docker container for snowchain locally:
Download docker from https://docs.docker.com/desktop/setup/install/mac-install/
In terminal run:
> docker build -t snowchain .
> docker run -p 80:80 snowchain
In browser launch "http://localhost:80"