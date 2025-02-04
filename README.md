
## 第一步：安装依赖
```bash
pip install -r requirements.txt
```

## 第二步：配置文件设置
打开config.json文件，里面是这样的：
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


你需要有LLM的API账户，不过考虑很多人都没有，所以我推荐去淘宝上面搜："API"三个字。会有很多的商家卖的，什么模型都有。他们会给你一个key（密钥）以及中转url地址。你只需要把这些密钥、url地址，以及最后的LLM模型填写到config.json文件里面就行了。

当然，也有很多的模型淘宝上面是找不到的，所以也可以去一些专门卖各种llm模型的API的店里面充钱买。例如这个智增增这个网站：https://gpt.zhizengzeng.com 

PS：为了证明我没有收他们家的广告费，我吐槽几句。为啥必须得50起充啊？没有自定义金额啊？还有怎么有些模型的API处理速度那么慢啊？编辑界面模型复制都复制不了，还得让我手打，眼睛都要看花了，交互做的什么啊？懂不懂用户心理？

总之无所谓你去哪里搞这些配置内容，api_key、api_base、model这三个填写进去就行了。最后system_prompt这个是关于你的AI的人设的，在这里填写你AI的设定，AI会基于你的设定来输出对应的内容。

## 第三步：运行程序
```bash
python distil.py
```

最后傻傻的等待数据输出就行了。会在data文件夹里面输出源源不断的问答对。一边输出一边保存的，所以不用担心额度不够了全部消失了。
