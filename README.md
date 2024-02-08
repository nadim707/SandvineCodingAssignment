# Http Stats Parser
> A python program to get HTTP stats present in wireshark pcap file 

Http Stats Parser runs in a dockerized environment, takes the wireshark network trace (.pcap) file as input and parses it and returns total Http flows, total Http bytes transmitted as well as provides the top hostname which contributes to maximum data bytes/traffic among all hostnames

## Installing / Getting started

A quick introduction of the minimal setup you need to get this Http parser up and running with Docker.

### Directory and File Structure

- [files]
  - [pcap_files]
    - [capture.pcap]
  - [http_stats.py]
- [http_parser]
  - [Dockerfile]
  - [requirements.txt]


### Initial Configuration

We need to have Docker Daemon setup on the machine. Check by running the following command.

```shell
docker version
```

Once Docker is setup, run the following commands in order to create a Docker image and then start Docker Container

```shell
#  run from the directory containing Dockerfile
docker build -t http_parser . # docker build -t http_parser <directory of Dockerfile>
```
 
```shell
#  with -e option, provide the pcap file path as commandline argument
#  with -v option, provide the absolute path of <files> directory which contains the python script as well as pcaps files which mounts this directory insde the app directory of docker image
docker run -e filename="./pcap_files/capture.pcap" -v /Users/fci/Desktop/assignment/files:/app --name http_analyser http_parser
```