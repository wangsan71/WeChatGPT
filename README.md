<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="WeChatGPT_0"></a>WeChatGPT</h1>
<h2 class="code-line" data-line-start=1 data-line-end=2 ><a id="httpswwwmodbprodb614349_1"></a>原文地址为：<a href="https://www.modb.pro/db/614349">https://www.modb.pro/db/614349</a></h2>
<p class="has-line-data" data-line-start="2" data-line-end="4">这是一个使用Python编写的接口程序，专门为微信而设计的聊天机器人，使用了chat-gpt模型。<br>
该程序已经升级，现在支持窗口控制和图形用户界面。</p>
<h2 class="code-line" data-line-start=4 data-line-end=5 ><a id="_4"></a>使用说明：</h2>
<ul>
<li class="has-line-data" data-line-start="5" data-line-end="6">Python 版本需要在 3.7~3.10 之间（3.10 未经测试，不确定是否可用）。</li>
<li class="has-line-data" data-line-start="6" data-line-end="7">需要安装 wxauto、openai, time 和 PyQt5（如果想使用图形用户界面）。</li>
<li class="has-line-data" data-line-start="7" data-line-end="8">需要安装微信客户端。</li>
<li class="has-line-data" data-line-start="8" data-line-end="9">安装库代码如下:</li>
</ul>
<pre><code class="has-line-data" data-line-start="10" data-line-end="15">pip install wxauto
pip install openai
pip install PyQt5
pip install time
</code></pre>
<h2 class="code-line" data-line-start=15 data-line-end=16 ><a id="_15"></a>准备使用</h2>
<p class="has-line-data" data-line-start="16" data-line-end="17">在使用之前，请在 WeChatGPT_Groups.py 和 WeChatGPT_YourSelf.py 中填入以下信息：</p>
<pre><code class="has-line-data" data-line-start="18" data-line-end="22">openai.api_key = &quot;#你的OpenAI API密钥&quot;
who = '#群组名称'
nickname='# 识别出是在和ChatGPT对话即可，最好使用&quot;@[微信名称]&quot;进行识别'
</code></pre>
<p class="has-line-data" data-line-start="22" data-line-end="23">填写完毕后，可以点击 <a href="http://WeChatBotStarter.py">WeChatBotStarter.py</a> 启动程序，也可以分别点击 WeChatGPT_Groups.py 和 WeChatGPT_YourSelf.py 使用程序。</p>
<h2 class="code-line" data-line-start=23 data-line-end=24 ><a id="_23"></a>反馈问题</h2>
<p class="has-line-data" data-line-start="24" data-line-end="27">主要邮箱1: <a href="mailto:thomassan1031@gmail.com">thomassan1031@gmail.com</a><br>
主要邮箱2: <a href="mailto:1101600045@qq.com">1101600045@qq.com</a><br>
副邮箱: <a href="mailto:thomas6668@163.com">thomas6668@163.com</a></p>
