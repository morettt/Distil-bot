# ChatGPT数据蒸馏工具

这是一个帮助你从LLM模型中获取问答对的开源项目。

## 安装步骤

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置文件设置

打开并编辑 `config.json` 文件:

```json
{
    "api_key": "密钥",
    "api_base": "url地址", 
    "ask_dir": "./data/ordinary.txt",
    "output_file": "./data/output.txt",
    "model": "你的LLM模型",
    "system_prompt": "在这里填写：AI的设定、角色人设"
}
```

配置说明:
- `api_key`: LLM API的访问密钥
- `api_base`: API的服务器地址
- `model`: 选择的语言模型名称
- `system_prompt`: AI的角色设定和行为规则

### 3. 获取API配置

获取API配置的途径:
1. 淘宝搜索"API" - 有商家提供各类模型的API服务
2. 专业API平台 - 如智增增(https://gpt.zhizengzeng.com)等平台

注意事项:
- 确保准确填写 api_key、api_base 和 model 这三个关键配置
- system_prompt 用于定制AI的回答风格和行为模式

### 4. 运行程序

```bash
python distil.py
```

运行后程序会自动在 data 文件夹下生成问答数据，数据会实时保存，无需担心额度用尽导致数据丢失。
