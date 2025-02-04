# Distil-bot
这是一个用于批量制作LLM问答对的项目。只需填写AI的角色、性格等设定。代码会自动将上千条问题与你设定的角色进行绑定，并输出对应的模型回复。最终合并为问答对。大大减轻人工制作数据集的消耗。

第一步安装依赖：
```bash
pip install -r requirements.txt
```
第二步打开config.json文件，里面是这样的：
```bash
{
    "api_key": "密钥",
    "api_base": "url地址",
    "ask_dir": "./data/ordinary.txt",
    "output_file": "./data/output.txt",
    "model": "你的LLM模型",
    "system_prompt": "在这里填写：AI的设定、角色人设"
}
```

其中
