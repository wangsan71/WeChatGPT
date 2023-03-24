#WeChatGPT
<p class="has-line-data" data-line-start="0" data-line-end="3">原文地址为：<a href="https://www.modb.pro/db/614349">https://www.modb.pro/db/614349</a><br>
这是一个使用Python编写的接口程序，专门为微信而设计的聊天机器人，使用了chat-gpt模型。<br>
该程序已经升级，现在支持窗口控制和图形用户界面。</p>
<p class="has-line-data" data-line-start="4" data-line-end="9">使用说明：<br>
Python 版本需要在 3.7~3.10 之间（3.10 未经测试，不确定是否可用）。<br>
需要安装 wxauto、openai 和 PyQt5（如果想使用图形用户界面）。<br>
需要安装微信客户端。<br>
安装库代码如下:</p>
<pre><code class="has-line-data" data-line-start="10" data-line-end="14">pip install wxauto
pip install openai
pip install PyQt5
</code></pre>
<p class="has-line-data" data-line-start="14" data-line-end="15">在使用之前，请在 WeChatGPT_Groups.py 和 WeChatGPT_YourSelf.py 中填入以下信息：</p>
<pre><code class="has-line-data" data-line-start="16" data-line-end="20">openai.api_key = &quot;#你的OpenAI API密钥&quot;
who = '#群组名称'
nickname='# 识别出是在和ChatGPT对话即可，最好使用&quot;@[微信名称]&quot;进行识别'
</code></pre>
<p class="has-line-data" data-line-start="20" data-line-end="21">填写完毕后，可以点击 <a href="http://WeChatBotStarter.py">WeChatBotStarter.py</a> 启动程序，也可以分别点击 WeChatGPT_Groups.py 和 WeChatGPT_YourSelf.py 使用程序。</p>
