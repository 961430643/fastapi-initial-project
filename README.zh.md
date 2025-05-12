<!--张振锟-->
# FastAPI 初始项目

## 简介

这是一个基于 [FastAPI](https://fastapi.tiangolo.com/) 框架的初始项目模板，旨在帮助开发者快速启动基于 Python 的 Web 应用程序。该项目采用模块化设计，支持快速开发、扩展和部署。

---

## 功能特性

- 🚀 **快速启动**：包含最小化的 FastAPI 项目结构。
- 🛠️ **可扩展**：模块化代码结构，易于扩展新功能。
- 📦 **依赖管理**：使用 `requirements.txt` 或 `poetry` 管理依赖。
- 🔐 **安全性**：内置支持环境变量管理（`.env` 文件）。
- 🗃️ **数据库支持**：支持多种数据库（如 SQLite、PostgreSQL）。
- 🌐 **API 文档**：自动生成交互式 API 文档（Swagger UI 和 ReDoc）。

---

## 环境要求

在开始之前，请确保您的开发环境满足以下要求：

- Python 版本：`>=3.8`
- 推荐操作系统：Windows、MacOS、Linux
- 包管理工具：`pip` 或 `poetry`

---

## 安装步骤

### 1. 克隆项目代码

```bash
git clone https://github.com/zzk-zuishuai/fastapi-initial-project.git
cd fastapi-initial-project
```

### 2. 创建虚拟环境

使用 `venv` 创建虚拟环境并激活：

```bash
python -m venv venv
# 激活虚拟环境 (Linux/MacOS)
source venv/bin/activate
# 激活虚拟环境 (Windows)
venv\Scripts\activate
```

### 3. 安装项目依赖

```bash
pip install -r requirements.txt
```

---

## 使用说明

### 运行开发服务器

在开发模式下运行服务器：

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

服务器启动后，您可以访问以下地址：

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 数据库迁移

如果项目使用了数据库，请确保运行迁移脚本：

```bash
alembic upgrade head
```

---

## 部署指南

以下是生产环境的部署步骤示例：

### 1. 使用 Gunicorn 部署

```bash
gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000
```

### 2. 配置 Nginx 反向代理

以下是 Nginx 配置示例：

```nginx
server {
    listen 80;
    server_name your_domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 3. 使用 Docker 部署（可选）

创建一个 `Dockerfile`：

```dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

构建并运行 Docker 镜像：

```bash
docker build -t fastapi-app .
docker run -d -p 8000:8000 fastapi-app
```

---

## 目录结构

以下是项目的主要目录结构：

```plaintext
fastapi-initial-project/
├── app/
│   ├── main.py          # FastAPI 应用入口
│   ├── routers/         # 路由模块
│   ├── models/          # 数据模型
│   ├── schemas/         # 数据验证模型
│   └── utils/           # 工具函数
├── tests/               # 测试代码
├── requirements.txt     # 项目依赖
├── Dockerfile           # Docker 配置
└── README.md            # 项目说明文档
```
<!--张振锟-->

<!-- by 2205308010338蒙思勇 -->
# FATSAPI 项目

这是一个基于 "FastAPI" 和 "Vue.js" 的任务管理工具，旨在帮助用户高效地管理任务。项目适合用来学习和实践全栈开发，尤其是 FastAPI 和 Vue.js 的结合使用。

## ✨ 项目特点

- 📝 "任务管理"：支持添加、编辑、删除任务，帮助用户清晰地规划和管理日常任务。
- ✅ "任务状态管理"：可以勾选任务为已完成状态，方便用户跟踪任务进度。
- 💾 "数据存储"：
  - 前端：支持浏览器 LocalStorage 存储任务数据，便于快速体验。
  - 后端：使用数据库（如 MySQL）存储任务数据，确保数据持久化。
- 🎨 "响应式设计" ：界面适配手机和 PC，提供良好的用户体验。
- 🔗 "API 支持"  ：后端提供 RESTful API，方便与其他系统集成。

## 🚀 快速开始

### 克隆项目

```bash
https://github.com/cxkmsy/fastapi-initial-project.git
cd fastapi-initial-project
```

### 后端部分

1. **安装依赖**：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

2. **配置数据库**：
   - 确保 MySQL 或其他数据库已安装并运行。
   - 修改 `app/config.py` 文件中的数据库配置。

3. **初始化数据库**：
   ```bash
   python -c "from app.schemas.schema import index; index()"
   ```

4. **运行后端服务**：
   ```bash
   uvicorn app.main:app --reload
   ```
   后端服务将运行在 `http://127.0.0.1:8000`。

### 前端部分

1. **安装依赖**：
   ```bash
   cd frontend
   npm install
   ```

2. **启动前端服务**：
   ```bash
   npm run dev
   ```
   前端服务将运行在 `http://localhost:5173`。

## 📮 API 文档

后端提供了自动生成的 API 文档，可以通过以下地址访问：
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`


## 📦 项目结构

```
fastapi-initial-project/
├── app/                  # 后端代码目录
│   ├── controllers/      # 控制器模块，处理业务逻辑
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── projects.py   # 项目相关的业务逻辑
│   │   ├── users.py      # 用户相关的业务逻辑
│   ├── helpers/          # 辅助工具模块
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── auth.py       # 认证相关的工具函数
│   │   ├── hashing.py    # 哈希处理工具（如密码加密）
│   ├── middlewares/      # 中间件模块
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── auth.py       # 认证中间件
│   ├── models/           # 数据库模型定义
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── projects.py   # 项目模型
│   │   ├── users.py      # 用户模型
│   ├── routers/          # 路由模块
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── index.py      # 路由加载入口
│   │   ├── projects.py   # 项目相关的路由
│   │   ├── users.py      # 用户相关的路由
│   ├── schemas/          # 数据验证和序列化模块
│   │   ├── __init__.py   # 包初始化文件
│   │   ├── projects.py   # 项目相关的 Pydantic 模型
│   │   ├── schema.py     # 数据库初始化脚本
│   │   ├── users.py      # 用户相关的 Pydantic 模型
│   ├── __init__.py       # 包初始化文件
│   ├── config.py         # 配置文件（如数据库连接配置）
│   ├── database.py       # 数据库连接和初始化
│
├── .gitignore            # Git 忽略文件配置
├── LICENSE               # 项目许可证
├── main.py               # FastAPI 应用主入口
├── README.md             # 英文版项目说明文档
├── README.zh.md          # 中文版项目说明文档
├── requirements.txt      # Python 依赖列表
├── terms.md              # 项目条款或说明
├── ai_usage_screenshots  # AI 使用截图目录
```

## 📸 项目功能与截图

### 1. 添加任务
用户可以通过输入任务名称和描述来添加新任务。

![添加任务界面]

### 2. 查看任务列表
任务列表展示所有任务，包括未完成和已完成的任务。

![任务列表界面]

### 3. 编辑任务
支持对已有任务进行修改，包括任务名称和描述。

![编辑任务界面]

### 4. 删除任务
用户可以删除不需要的任务。

![删除任务界面]

### 5. 勾选已完成任务
通过勾选任务，标记任务为已完成状态。

![勾选任务界面]
<!-- by 2205308010338蒙思勇 -->

