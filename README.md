## ocr api
一个简易的ocr识别图片中数字的api接口 + 简易的token校验。

### 当前环境依赖说明

```text
python=3.11.9

paddlepaddle==2.5.2
paddleocr==2.7.3
```

注意这里用`paddlepaddle==2.5.2`版本。<br>
如果想要使用其他的paddlepaddle版本，需要自行测试。<br>
不然可能遇到这样的问题：在本地能正常运行高版本（例如`paddlepaddle==2.6.1`），但docker打包后出现版本兼容问题。


### 使用说明

    - 复制`config-dev.json`文件为`config.json`并填写自定义的`access_token`；
    - 配置`http-client.env.json`后在`test_main.http`中进行接口调试，其中`access_token`的值跟config.json中的一致；

### docker方式运行

[点击这里查看docker说明](docker/README.md)


### 本地源码运行

- 安装依赖
```shell
pip install -r requirements.txt
```

- 运行

```shell
python main.py
```

或者：

```shell
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```