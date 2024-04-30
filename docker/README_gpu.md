
## ocr的api-docker镜像 - gpu版

### 构建api的基础依赖镜像包，减少后续的构建耗时，其中`--build-arg`是可选的
```shell
docker build . -t samge/paddleocr-gpu:base -f docker/gpu/Dockerfile_base --build-arg PROXY=http://192.168.3.169:7890
```

### 构建api正式包
```shell
docker build . -t samge/paddleocr-gpu -f docker/gpu/Dockerfile
```

### 上传
```shell
docker push samge/paddleocr-gpu:base

docker push samge/paddleocr-gpu
```

### 运行docker镜像
如果 `ACCESS_TOKEN` 环境变量跟 `config.json` 同时配置，优先读取环境变量`ACCESS_TOKEN`的值

`方式1：以配置 ACCESS_TOKEN 环境变量方式运行
```shell
docker run -d \
--name paddleocr \
-e ACCESS_TOKEN=xxx \
-p 8234:8000 \
-v ~/.paddleocr:/root/.paddleocr \
--pull=always \
--restart always \
--gpus=all \
samge/paddleocr-gpu:latest
```

`方式2：以config.json`映射方式运行
这里的`/home/samge/docker_data/paddleocr/config.json`需要替换为使用者的本地映射路径。
```shell
docker run -d \
--name paddleocr \
-v /home/samge/docker_data/paddleocr/config.json:/app/config.json \
-p 8234:8000 \
-v ~/.paddleocr:/root/.paddleocr \
--pull=always \
--restart always \
--gpus=all \
samge/paddleocr-gpu:latest
```