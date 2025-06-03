# Docker Important Command that I learn

## Build Command
```bash
docker build -t name_image .
```
## Check Images
```bash
docker images
```
## Check runing Container
```bash
docker ps
```
## View all the Container
```bash
docker ps --all
```
## Run the image in a port
```bash
docker run -p 8000:8000 image_name
```
## To Login
```bash
docker login
```
## Push to DockerHub
```bash
docker push dockerhub_username/image_name
```

## For Cleaning
1. Remove Unused Docker Objects
### These include stopped containers, unused volumes, dangling images, and build cache.
```bash
docker system prune
```

To remove everything not currently used (containers, networks, images, build cache):
```bash
docker system prune -a
```
2. Remove All Images, Containers, Volumes, and Networks
### All containers:
```bash
docker rm $(docker ps -aq)
```
### All images:
```bash
docker rmi $(docker images -q)
```
### All volumes:
```bash
docker volume rm $(docker volume ls -q)
```
All networks (except bridge, host, and none):
```bash
docker network rm $(docker network ls | grep -vE 'bridge|host|none' | awk '{print $1}')
```