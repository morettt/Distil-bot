## 基本介绍
搞了一堆问题,跟LLM的角色设定配合,直接批量生成自定义的问答对,省得手动做数据集。输出好的数据适合用于改变模型性格特征、回复风格等。

代码用了多线程,默认开6个线程。1500个问题16分钟就能跑完。要是你服务器够猛,开到10-20个线程的话,3-4分钟就搞定了。

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

配置说明:
- `api_key`: 这里填写你的API的密钥
- `api_base`: 这里是API的url地址，直连的中转的都行
- `model`: 大模型llm的名称，例如：gpt-3.5-turbo、gpt-4o
- `system_prompt`: AI的角色设定和行为规则。例如：你是一个性格活泼可爱的AI，你叫的名字叫侦琉。



你需要有LLM的API账户，不过考虑很多人都没有，所以我推荐去淘宝上面搜："API"三个字。会有很多的商家卖的，什么模型都有。他们会给你一个key（密钥）以及url地址。你只需要把这些密钥、url地址，以及最后的LLM模型填写到config.json文件里面就行了。

当然，也有很多的模型淘宝上面是找不到的，所以也可以去一些专门卖各种llm模型的API的店里面充钱买。例如这个这个网站：https://gpt.zhizengzeng.com 

PS：为了证明我没有收他们家的广告费，我吐槽几句。为啥必须得50起充啊？没有自定义金额啊？还有怎么有些模型的API处理速度那么慢啊？

编辑界面模型复制都复制不了，还得让我手打，眼睛都要看花了，交互做的什么啊？懂不懂用户心理？最近流输出有BUG，我提交问题给客服，他说没有出问题。然后我就拿他们官网的示例代码运行演示，然后直接报错了，官方自己给的代码报错了，这还不是bug？

然后客服就不理我了。呵呵。有意思的是第二天这个bug处理好了

这点值得表扬~


如果你们来找我打钱宣传的话，这些就都不重要了。我会把这些内容都改成夸你们的，比心❤️

总之无所谓你去哪里搞这些配置内容，api_key、api_base、model这三个填写进去就行了。最后system_prompt这个是关于你的AI的人设的，在这里填写你AI的设定，AI会基于你的设定来输出对应的风格回复。

## 最后：运行程序
```bash
python distil.py
```

运行后傻傻的等待数据输出就行了。会在data文件夹里面输出一个output.txt文件。里面会生成源源不断的问答对，一边输出一边保存，所以不用担心额度不够内容全部消失了。
