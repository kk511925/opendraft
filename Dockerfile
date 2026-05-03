FROM python:3.10-slim

WORKDIR /app

# 安装生成 PDF/图片 所需的全部系统库（避免再次缺包）
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    libffi-dev \
    libcairo2 \
    libpangoft2-1.0-0 \
    libharfbuzz-subset0 \
    fonts-liberation \
    libxml2 \
    libxslt1.1 \
    && rm -rf /var/lib/apt/lists/*

# 安装 Python 依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir fastapi uvicorn

# 复制项目代码
COPY . .

EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
