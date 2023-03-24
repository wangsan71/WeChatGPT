import openai
from wxauto import *
import time

def wx_group_chat():
    openai.api_key = ""  
    model_engine = "text-davinci-003"
    who = ''
    nickname=''  # 需要识别出是在和ChatGPT对话即可

    wx=WeChat()
    wx.ChatWith(who)
    wx.SendMsg('Starting work')
    while True:
        msgobject1 = wx.GetLastMessage
        speaker1, msgcontent1, speakerid1= msgobject1
        time.sleep(0.5)
        msgobject2=wx.GetLastMessage
        speaker2, msgcontent2, speakerid2 = msgobject2
        if msgcontent1 != msgcontent2 and (nickname in msgcontent2):
            msgcontent2=msgcontent2.replace(nickname,'')
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=msgcontent2,
                max_tokens=500,
                n=1,
                frequency_penalty=0.5,
                presence_penalty=0,
                stop=None,
                top_p=1,
                temperature=0.8,
            )
            ret = completions.choices[0].text
            wx.SendMsg(ret)
