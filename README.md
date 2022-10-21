# Python SAST SCA Pipeline

## Build Dockerfile
```bash
docker build -t we45_gaia -f Dockerfile .
```

## Run Dockerfile
```bash
docker run -d -p 8081:8080 -v $PWD:/data we45_gaia:latest
```
