# 设置基础镜像
FROM samge/paddleocr-gpu:base

# 将工作目录设置为 /app
WORKDIR /app

# 复制当前目录中的所有文件到 /app
COPY .. .

# 安装所需的 Python 包（这里的all_proxy需要替换为你的代理或者删掉）
RUN pip install --no-cache-dir -r requirements.txt

# 声明容器监听的端口
EXPOSE 8000

# 配置gpu是否与否
ENV USE_GPU=true

# 运行应用程序
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
