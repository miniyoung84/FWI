#Copyright 2018 <Min Choi>
#Developed by Min Choi, Ashmita Sarma, Nick Eickhoff, and Lokesh Nasaka
#Written by Min Choi, Nick Eickhoff, Katie Amundson, and Rowen Guncheon"

import discord
import asyncio
import os
import csv
import sys
import random
import requests
import fileinput
from discord.ext.commands import Bot
from discord.ext import commands
import urllib3
import time
import datetime
from lxml import html
from discord.utils import get

Client=discord.Client()
bot_prefix=">"
client = commands.Bot(command_prefix=bot_prefix)

alphabet=['A','B','C','D','E','F','G','H','I','J','K','QUIT']

@client.event
async def on_ready():
    print("FWI Test Bot Running")
    await client.change_presence(game=discord.Game(name=">FWI"))

@client.event
async def on_message(message):
    if "whips and nae naes" in message.content.lower():
        time.sleep(2)
        await client.send_message(message.channel,"You'll always outshine me in how low the bar can go")
    await client.process_commands(message)
        

class Question:
    def __init__(self,content):
        self.Answers=[]
        self.content=content
    def addAnswer(self, answer):
        self.Answers.append(answer)
    def ask(self):
        return self.__content

class Answer:
    def __init__(self,content, T, I, R):
        self.__content=content
        self.T=T
        self.I=I
        self.R=R
    def getBigBuckEl_BurritoLoco(self):
        jukerGang = {
        "Tumblr": self.__T,
        "Reddit": self.__R,
        "Instagram": self.__T
        }
        return jukerGang
    def getContent(self):
        return self.__content

@client.command(pass_context=True)
async def clear(ctx, number):
    if ctx.message.author.server_permissions.administrator:
        mgs = []
        number = int(number) #Converting the amount of messages to delete to an integer
        async for x in client.logs_from(ctx.message.channel, limit = number):
            mgs.append(x)
        await client.delete_messages(mgs)
    else:
        await client.say("Cannot Use This Command At This Time")

@client.command(pass_context=True)
async def FWI(ctx):
    if "unified" in str(ctx.message.channel):
        await client.say("Cannot take the FWI Test here! Use a test-room")
        return
    await client.say("Note: This test is not to be confused with the traditional political spectrum, although we think this will be indicative of the political spectrum decades in the future.")
    await client.say("Developed by Min Choi, Ashmita Sarma, Nick Eickhoff, and Lokesh Nasaka")
    await client.say("Written by Min Choi, Nick Eickhoff, Katie Amundson, and Rowen Guncheon")
    T=0
    I=0
    R=0
    q2=Question('What is your favorite social networking site?')
    a10=Answer("Facebook or Twitter", 0, 1, 0)
    Question.addAnswer(q2,a10)
    a11=Answer("Tumblr", 2, 0, 0)
    Question.addAnswer(q2, a11)
    a12=Answer("Reddit", 0, 0, 2)
    Question.addAnswer(q2, a12)
    a13=Answer("Instagram", 0, 2, 0)
    Question.addAnswer(q2, a13)
    a14=Answer("4chan or 8chan", 0, 0, 3)
    Question.addAnswer(q2, a14)
    a15=Answer("Snapchat", 0, 2, 0)
    Question.addAnswer(q2, a15)
    a16=Answer("Other", 0, 0, 0)
    Question.addAnswer(q2, a16)
    embed3 = discord.Embed(title=(str(1)+') '+q2.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q2.Answers:
            embed3.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed3)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q2.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q3=Question('Do you use Snapchat on a regular basis?')
    a17=Answer("Yes", 0, 2, 0)
    Question.addAnswer(q3, a17)
    a18=Answer("No", 0, 0, 1)
    Question.addAnswer(q3, a18)
    embed4 = discord.Embed(title=(str(2)+') '+q3.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q3.Answers:
            embed4.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed4)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q3.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q4=Question('Do you use Tumblr on a regular basis?')
    a19=Answer("Yes", 2, 0, 0)
    Question.addAnswer(q4, a19)
    a20=Answer("No", 0, 0, 0)
    Question.addAnswer(q4, a20)
    embed5 = discord.Embed(title=(str(3)+') '+q4.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q4.Answers:
            embed5.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed5)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q4.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q5=Question('Do you use Pinterest on a regular basis?')
    a21=Answer("Yes", 1, 0, 0)
    Question.addAnswer(q5, a21)
    a22=Answer("No", 0, 0, 0)
    Question.addAnswer(q5, a22)
    embed6 = discord.Embed(title=(str(4)+') '+q5.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q5.Answers:
            embed6.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed6)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q5.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q6=Question('Do you use Instagram on a regular basis?')
    a23=Answer("Yes", 0, 2, 0)
    Question.addAnswer(q6, a23)
    a24=Answer("No", 0, 0, 1)
    Question.addAnswer(q6, a24)
    embed7 = discord.Embed(title=(str(5)+') '+q6.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q6.Answers:
            embed7.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed7)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q6.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q7=Question('Do you frequently read and leave ratings for YouTube comments?')
    a25=Answer("Yes", 0, 0, 1)
    Question.addAnswer(q7, a25)
    a26=Answer("No", 0, 1, 0)
    Question.addAnswer(q7, a26)
    embed8 = discord.Embed(title=(str(6)+') '+q7.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q7.Answers:
            embed8.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed8)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q7.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q8=Question('Do you use Reddit on a regular basis?')
    a27=Answer("Yes", 0, 0, 2)
    Question.addAnswer(q8, a27)
    a28=Answer("No", 0, 0, 0)
    Question.addAnswer(q8, a28)
    embed9 = discord.Embed(title=(str(7)+') '+q8.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q8.Answers:
            embed9.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed9)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q8.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q9=Question('Do you use 4chan or other anonymous forums on a regular basis?')
    a29=Answer("Yes", 0, 0, 3)
    Question.addAnswer(q9, a29)
    a30=Answer("No", 0, 0, 0)
    Question.addAnswer(q9, a30)
    embed10 = discord.Embed(title=(str(8)+') '+q9.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q9.Answers:
            embed10.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed10)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q9.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q10=Question('Do you identify with most people in your generation?')
    a31=Answer("Yes", 0, 2, 0)
    Question.addAnswer(q10, a31)
    a32=Answer("No", 1, 0, 1)
    Question.addAnswer(q10, a32)
    embed11 = discord.Embed(title=(str(9)+') '+q10.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q10.Answers:
            embed11.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed11)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q10.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q11=Question('Do you use, watch or read Buzzfeed on a regular basis?')
    a33=Answer("Yes", 1, 1, 0)
    Question.addAnswer(q11, a33)
    a34=Answer("No", 0, 0, 1)
    Question.addAnswer(q11, a34)
    embed12 = discord.Embed(title=(str(10)+') '+q11.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q11.Answers:
            embed12.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed12)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q11.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q12=Question('Are people these days too sensitive and easily offended?')
    a35=Answer("Yes", 0, 0, 1)
    Question.addAnswer(q12, a35)
    a36=Answer("No", 1, 0, 0)
    Question.addAnswer(q12, a36)
    embed13 = discord.Embed(title=(str(11)+') '+q12.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q12.Answers:
            embed13.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed13)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q12.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q13=Question('What is your stance on the Black Lives Matter Movement?')
    a37=Answer("Full-Support their ideas and methods of purpose", 2, 0, 0)
    Question.addAnswer(q13, a37)
    a38=Answer("Support, but not all their methods of protest", 0, 1, 0)
    Question.addAnswer(q13, a38)
    a39=Answer("Neutral/Unfamiliar", 0, 0, 1)
    Question.addAnswer(q13, a39)
    a40=Answer("Against, All Lives Matter", 0, 0, 2)
    Question.addAnswer(q13, a40)
    a41=Answer("Against, what the movement stands for is wrong", 0, 0, 2)
    Question.addAnswer(q13, a41)
    embed14 = discord.Embed(title=(str(12)+') '+q13.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q13.Answers:
            embed14.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed14)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q13.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q14=Question(' Is changing the race of existing characters in fiction wrong?')
    a42=Answer("Yes, always", 0, 1, 0)
    Question.addAnswer(q14, a42)
    a43=Answer("Yes, but only when it's whitewashing", 2, 0, 0)
    Question.addAnswer(q14, a43)
    a44=Answer("Yes, but only when it's done for the sake of diversity", 0, 0, 2)
    Question.addAnswer(q14, a44)
    a45=Answer("No", 0, 1, 0)
    Question.addAnswer(q14, a45)
    embed15 = discord.Embed(title=(str(13)+') '+q14.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q14.Answers:
            embed15.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed15)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q14.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q15=Question('Do you believe you are smarter than the general public?')
    a46=Answer("Yes", 1, 0, 1)
    Question.addAnswer(q15, a46)
    a47=Answer("No", 0, 2, 0)
    Question.addAnswer(q15, a47)
    embed16 = discord.Embed(title=(str(14)+') '+q15.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q15.Answers:
            embed16.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed16)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q15.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q16=Question('Is Reverse Racism (racism against whites) real?')
    a48=Answer("Yes, this is an overlooked and important issue", 0, 0, 2)
    Question.addAnswer(q16, a48)
    a49=Answer("Yes, but it is not as significant as racism against non-whites", 0, 1, 0)
    Question.addAnswer(q16, a49)
    a50=Answer("No", 2, 0, 0)
    Question.addAnswer(q16, a50)
    embed17 = discord.Embed(title=(str(15)+') '+q16.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q16.Answers:
            embed17.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed17)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q16.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q17=Question('Is it racist to have low numbers of non-whites in a workplace?')
    a51=Answer("Yes, exclusion is inherently racist", 2, 0, 0)
    Question.addAnswer(q17, a51)
    a52=Answer("Yes, but only for some jobs", 0, 1, 0)
    Question.addAnswer(q17, a52)
    a53=Answer("No, the best workers must get each position. Race does not matter", 0, 0, 2)
    Question.addAnswer(q17, a53)
    embed18 = discord.Embed(title=(str(16)+') '+q17.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q17.Answers:
            embed18.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed18)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q17.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q18=Question('Do you support affirmative action (specifically for race)?')
    a54=Answer("Yes, this helps the underprivileged", 1, 0, 0)
    Question.addAnswer(q18, a54)
    a55=Answer("No, this is unfair", 0, 0, 1)
    Question.addAnswer(q18, a55)
    embed19 = discord.Embed(title=(str(17)+') '+q18.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q18.Answers:
            embed19.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed19)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q18.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q19=Question('What brand is your phone? Why?')
    a56=Answer("Android Phone (Samsung, Google Pixel, LG, Moto, etc), because it's superior to iPhones", 0, 0, 1)
    Question.addAnswer(q19, a56)
    a57=Answer("Android Phone, but no particular preference", 0, 1, 0)
    Question.addAnswer(q19, a57)
    a58=Answer("iPhone, but no particular preference", 0, 1, 0)
    Question.addAnswer(q19, a58)
    a59=Answer("iPhone because it's superior to Android", 1, 0, 0)
    Question.addAnswer(q19, a59)
    a60=Answer("Other", 0, 0, 0)
    Question.addAnswer(q19, a60)
    embed20 = discord.Embed(title=(str(18)+') '+q19.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q19.Answers:
            embed20.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed20)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q19.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q20=Question('What is Gamergate?')
    a61=Answer("A horrible event that resulted in the attack of female gamers and gaming developers", 3, 0, 0)
    Question.addAnswer(q20, a61)
    a62=Answer("An overreaction between two sides over something that wasn't a big deal", 0, 0, 1)
    Question.addAnswer(q20, a62)
    a63=Answer("An issue on corruption among journalists in the gaming industry", 0, 0, 2)
    Question.addAnswer(q20, a63)
    a64=Answer("Feminists twisting an issue to pursue their own agenda", 0, 0, 2)
    Question.addAnswer(q20, a64)
    a65=Answer("I have no idea", 0, 2, 0)
    Question.addAnswer(q20, a65)
    embed21 = discord.Embed(title=(str(19)+') '+q20.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q20.Answers:
            embed21.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed21)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q20.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q21=Question('Is Candy Crush a "real" video game?')
    a66=Answer("Yes", 1, 0, 0)
    Question.addAnswer(q21, a66)
    a67=Answer("No", 0, 0, 1)
    Question.addAnswer(q21, a67)
    a68=Answer("I'm not familiar with Candy Crush", 0, 0, 0)
    Question.addAnswer(q21, a68)
    embed22 = discord.Embed(title=(str(20)+') '+q21.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q21.Answers:
            embed22.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed22)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q21.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q22=Question('Do you use Twitch on a regular basis?')
    a69=Answer("Yes", 0, 0, 1)
    Question.addAnswer(q22, a69)
    a70=Answer("No, I don't like Twitch", 1, 0, 0)
    Question.addAnswer(q22, a70)
    a71=Answer("I don't know what Twitch is", 0, 2, 0)
    Question.addAnswer(q22, a71)
    embed23 = discord.Embed(title=(str(21)+') '+q22.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q22.Answers:
            embed23.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed23)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q22.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q23=Question('How many genders are there?')
    a72=Answer("0 or 1", 0, 0, 0)
    Question.addAnswer(q23, a72)
    a73=Answer("2", 0, 0, 2)
    Question.addAnswer(q23, a73)
    a74=Answer("3-26", 2, 0, 0)
    Question.addAnswer(q23, a74)
    a75=Answer("27+", 3, 0, 0)
    Question.addAnswer(q23, a75)
    embed24 = discord.Embed(title=(str(22)+') '+q23.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q23.Answers:
            embed24.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed24)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q23.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q24=Question('Is gender just a social construct?')
    a76=Answer("Yes", 1, 0, 0)
    Question.addAnswer(q24, a76)
    a77=Answer("No ", 0, 0, 1)
    Question.addAnswer(q24, a77)
    a78=Answer("Partially", 0, 1, 0)
    Question.addAnswer(q24, a78)
    embed25 = discord.Embed(title=(str(23)+') '+q24.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q24.Answers:
            embed25.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed25)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q24.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q25=Question('Should someone that has female genitalia, and is born as the sex female be able to use male (he/him/his) pronouns?')
    a79=Answer("Yes, sex and genitalia are an innaccurate way of defining gender", 2, 0, 0)
    Question.addAnswer(q25, a79)
    a80=Answer("No", 0, 0, 2)
    Question.addAnswer(q25, a80)
    a81=Answer("Yes, I do not agree with this, but people are free to do what they want", 0, 2, 0)
    Question.addAnswer(q25, a81)
    embed26 = discord.Embed(title=(str(24)+') '+q25.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q25.Answers:
            embed26.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed26)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q25.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q26=Question('Should producers and writers include more gay characters in their works?')
    a82=Answer("Yes, representation must be improved", 1, 0, 0)
    Question.addAnswer(q26, a82)
    a83=Answer("Yes, gay characters are better than straight characters", 2, 0, 0)
    Question.addAnswer(q26, a83)
    a84=Answer("No, representation is important, but the current amount is good", 0, 1, 0)
    Question.addAnswer(q26, a84)
    a85=Answer("No, do not include gay characters for the sake of diversity", 0, 0, 2)
    Question.addAnswer(q26, a85)
    a86=Answer("No, being gay is wrong", 0, 0, 0)
    Question.addAnswer(q26, a86)
    embed27 = discord.Embed(title=(str(25)+') '+q26.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q26.Answers:
            embed27.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed27)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q26.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q27=Question('Is Modern Feminism out of control and is no longer necessary as women have already achieved equality?')
    a87=Answer("Yes, women have achieved equality and now feminists are trying to obtain an advantage over men", 0, 0, 2)
    Question.addAnswer(q27, a87)
    a88=Answer("Yes, women and men are equal", 0, 0, 1)
    Question.addAnswer(q27, a88)
    a89=Answer("No, but feminists frequently overreact", 0, 1, 0)
    Question.addAnswer(q27, a89)
    a90=Answer("No, but we are close to equality", 0, 1, 0)
    Question.addAnswer(q27, a90)
    a91=Answer("No, women face injustice and disadvantages in our society", 2, 0, 0)
    Question.addAnswer(q27, a91)
    embed28 = discord.Embed(title=(str(26)+') '+q27.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q27.Answers:
            embed28.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed28)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q27.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q28=Question('How many cents do women make for every $1 (100 cents) that men make in the workplace?')
    a92=Answer("80 or less", 2, 0, 0)
    Question.addAnswer(q28, a92)
    a93=Answer("80-90", 0, 0, 0)
    Question.addAnswer(q28, a93)
    a94=Answer("91-100", 0, 0, 2)
    Question.addAnswer(q28, a94)
    a95=Answer("101+", 0, 0, 3)
    Question.addAnswer(q28, a95)
    a96=Answer("I don't know", 0, 1, 0)
    Question.addAnswer(q28, a96)
    embed29 = discord.Embed(title=(str(27)+') '+q28.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q28.Answers:
            embed29.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed29)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q28.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q29=Question('There are proven statistics that women are paid less than men on average, but why is this the case?')
    a97=Answer("Sexism", 1, 0, 0)
    Question.addAnswer(q29, a97)
    a98=Answer("I don't know", 0, 1, 0)
    Question.addAnswer(q29, a98)
    a99=Answer("Women get pregnant", 0, 0, 2)
    Question.addAnswer(q29, a99)
    a100=Answer("Women work less dangerous jobs", 0, 0, 2)
    Question.addAnswer(q29, a100)
    a101=Answer("Women just have worse jobs than men which justifies this gap", 0, 0, 2)
    Question.addAnswer(q29, a101)
    a102=Answer("Systemic Oppression", 3, 0, 0)
    Question.addAnswer(q29, a102)
    a103=Answer("There aren't proven statistics", 0, 0, 2)
    Question.addAnswer(q29, a103)
    a104=Answer("Other", 0, 1, 0)
    Question.addAnswer(q29, a104)
    embed30 = discord.Embed(title=(str(28)+') '+q29.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q29.Answers:
            embed30.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed30)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q29.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q30=Question('What is your assessment of the effects of the #MeToo movement?')
    a105=Answer("Empowerment towards victims and a positive change in our culture", 2, 0, 0)
    Question.addAnswer(q30, a105)
    a106=Answer("Exposes perpetrators of sexual assault/harassment", 1, 1, 0)
    Question.addAnswer(q30, a106)
    a107=Answer("Benefits for victims, but with harmful sideful effects", 0, 1, 1)
    Question.addAnswer(q30, a107)
    a108=Answer("It created a dangerous precedent that will ruin lives without due process", 0, 0, 2)
    Question.addAnswer(q30, a108)
    a109=Answer("I don't know what #MeToo is", 0, 1, 0)
    Question.addAnswer(q30, a109)
    embed31 = discord.Embed(title=(str(29)+') '+q30.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q30.Answers:
            embed31.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed31)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q30.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q31=Question('Did you actively participate in the Womens March and other protests with similar intentions?')
    a110=Answer("Yes", 1, 0, 0)
    Question.addAnswer(q31, a110)
    a111=Answer("No", 0, 0, 0)
    Question.addAnswer(q31, a111)
    a112=Answer("Partially (No you didn't)", 0, 1, 0)
    Question.addAnswer(q31, a112)
    embed32 = discord.Embed(title=(str(30)+') '+q31.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q31.Answers:
            embed32.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed32)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q31.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q32=Question('What is your opinion on people who ask for more awareness of female abusers, female rapists, and male victims on posts/videos/stories about female victims?')
    a113=Answer("This is an important and underlooked issue", 0, 0, 2)
    Question.addAnswer(q32, a113)
    a114=Answer("They should make their own posts", 2, 0, 0)
    Question.addAnswer(q32, a114)
    a115=Answer("They do not care about victims, and only want to undermine other important causes", 2, 0, 0)
    Question.addAnswer(q32, a115)
    a116=Answer("I agree with what they stand for, as long as they remain sensitive", 0, 1, 0)
    Question.addAnswer(q32, a116)
    embed33 = discord.Embed(title=(str(31)+') '+q32.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q32.Answers:
            embed33.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed33)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q32.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q33=Question('Is white male privilege real?')
    a117=Answer("Yes", 2, 0, 0)
    Question.addAnswer(q33, a117)
    a118=Answer("No", 0, 0, 2)
    Question.addAnswer(q33, a118)
    embed34 = discord.Embed(title=(str(32)+') '+q33.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q33.Answers:
            embed34.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed34)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q33.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q34=Question('Do "Black" and "Muslim" culture contain sexist ideas that modern American feminists should criticize more? ')
    a119=Answer("Yes", 0, 0, 1)
    Question.addAnswer(q34, a119)
    a120=Answer("No", 1, 0, 0)
    Question.addAnswer(q34, a120)
    embed35 = discord.Embed(title=(str(33)+') '+q34.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q34.Answers:
            embed35.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed35)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q34.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q35=Question('Are Batman and Superman boring characters?')
    a121=Answer("They are both interesting", 0, 2, 0)
    Question.addAnswer(q35, a121)
    a122=Answer("They are both boring", 2, 0, 0)
    Question.addAnswer(q35, a122)
    a123=Answer("Only Batman is boring", 0, 1, 0)
    Question.addAnswer(q35, a123)
    a124=Answer("Only Superman is boring", 0, 0, 2)
    Question.addAnswer(q35, a124)
    a125=Answer("I'm not familiar with these characters", 0, 0, 0)
    Question.addAnswer(q35, a125)
    embed36 = discord.Embed(title=(str(34)+') '+q35.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q35.Answers:
            embed36.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed36)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q35.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q36=Question('What is your opinion on Rick and Morty fans?')
    a126=Answer("Most of them are good, except a few cringey people who give it a bad image", 0, 0, 2)
    Question.addAnswer(q36, a126)
    a127=Answer("I have no opinion", 0, 2, 0)
    Question.addAnswer(q36, a127)
    a128=Answer("They are a good fanbase that enjoy a show that is better than most other shows", 1, 0, 1)
    Question.addAnswer(q36, a128)
    a129=Answer("They're annoying", 0, 0, 0)
    Question.addAnswer(q36, a129)
    embed37 = discord.Embed(title=(str(35)+') '+q36.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q36.Answers:
            embed37.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed37)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q36.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q37=Question('Which of the following movies is the best?')
    a130=Answer("Frozen", 0, 2, 0)
    Question.addAnswer(q37, a130)
    a131=Answer("Big Hero 6", 0, 0, 2)
    Question.addAnswer(q37, a131)
    a132=Answer("Brave", 2, 0, 0)
    Question.addAnswer(q37, a132)
    a133=Answer("Tangled", 1, 1, 0)
    Question.addAnswer(q37, a133)
    embed38 = discord.Embed(title=(str(36)+') '+q37.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q37.Answers:
            embed38.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed38)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q37.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q38=Question('Which of the following movies is the best?')
    a134=Answer("Black Panther", 2, 0, 0)
    Question.addAnswer(q38, a134)
    a135=Answer("Wonder Woman", 1, 0, 0)
    Question.addAnswer(q38, a135)
    a136=Answer("Thor: Ragnarok", 0, 2, 0)
    Question.addAnswer(q38, a136)
    a137=Answer("Spiderman: Homecoming", 0, 1, 1)
    Question.addAnswer(q38, a137)
    a138=Answer("Guardians of the Galaxy Vol 2", 0, 0, 1)
    Question.addAnswer(q38, a138)
    a139=Answer("The Dark Knight", 0, 0, 2)
    Question.addAnswer(q38, a139)
    embed39 = discord.Embed(title=(str(37)+') '+q38.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q38.Answers:
            embed39.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed39)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q38.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q39=Question('Is Rey from Star Wars a good character?')
    a140=Answer("Yes", 1, 0, 0)
    Question.addAnswer(q39, a140)
    a141=Answer("Neutral", 0, 1, 0)
    Question.addAnswer(q39, a141)
    a142=Answer("No, because she's a Mary Sue", 0, 0, 2)
    Question.addAnswer(q39, a142)
    a143=Answer("I'm not familiar", 0, 1, 0)
    Question.addAnswer(q39, a143)
    a144=Answer("No", 0, 0, 2)
    Question.addAnswer(q39, a144)
    embed40 = discord.Embed(title=(str(38)+') '+q39.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q39.Answers:
            embed40.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed40)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q39.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q40=Question('What is your opinion on remaking old male-driven movies with female casts?')
    a145=Answer("It's a good thing, promotes inclusion", 2, 0, 0)
    Question.addAnswer(q40, a145)
    a146=Answer("It's a bad thing, they should come up with original ideas for women", 0, 0, 2)
    Question.addAnswer(q40, a146)
    embed41 = discord.Embed(title=(str(39)+') '+q40.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q40.Answers:
            embed41.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed41)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q40.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q41=Question('Were you ever a fan of BTS, Justin Bieber, One Direction, EXO, Taylor Swift, or Ariana Grande?')
    a147=Answer("Yes", 0, 3, 0)
    Question.addAnswer(q41, a147)
    a148=Answer("No", 1, 0, 1)
    Question.addAnswer(q41, a148)
    embed42 = discord.Embed(title=(str(40)+') '+q41.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q41.Answers:
            embed42.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed42)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q41.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q42=Question('What is your opinion on The Big Bang Theory?')
    a149=Answer("It's a good show", 0, 2, 0)
    Question.addAnswer(q42, a149)
    a150=Answer("It's bad", 2, 0, 2)
    Question.addAnswer(q42, a150)
    a151=Answer("No Opinion", 0, 0, 0)
    Question.addAnswer(q42, a151)
    embed43 = discord.Embed(title=(str(41)+') '+q42.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q42.Answers:
            embed43.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed43)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q42.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q43=Question('Select the best music artist from these options')
    a152=Answer("Pink Floyd", 0, 0, 2)
    Question.addAnswer(q43, a152)
    a153=Answer("Dua Lipa", 0, 2, 0)
    Question.addAnswer(q43, a153)
    a154=Answer("Janelle Monae", 2, 0, 0)
    Question.addAnswer(q43, a154)
    a155=Answer("Shawn Mendes", 0, 2, 0)
    Question.addAnswer(q43, a155)
    a156=Answer("Camila Cabello", 0, 2, 0)
    Question.addAnswer(q43, a156)
    embed44 = discord.Embed(title=(str(42)+') '+q43.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q43.Answers:
            embed44.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed44)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q43.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q44=Question('What is your favorite genre of music?')
    a157=Answer("Pop", 0, 2, 0)
    Question.addAnswer(q44, a157)
    a158=Answer("R&B", 0, 2, 0)
    Question.addAnswer(q44, a158)
    a159=Answer("Rap", 0, 0, 0)
    Question.addAnswer(q44, a159)
    a160=Answer("Country", 0, 1, 1)
    Question.addAnswer(q44, a160)
    a161=Answer("Rock", 0, 0, 2)
    Question.addAnswer(q44, a161)
    a162=Answer("EDM", 0, 0, 2)
    Question.addAnswer(q44, a162)
    a163=Answer("Alternative", 1, 0, 0)
    Question.addAnswer(q44, a163)
    a164=Answer("Alternative Rock", 0, 0, 1)
    Question.addAnswer(q44, a164)
    a165=Answer("Other", 1, 0, 1)
    Question.addAnswer(q44, a165)
    embed45 = discord.Embed(title=(str(43)+') '+q44.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q44.Answers:
            embed45.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed45)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q44.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q45=Question('Which of the following is the best video game?')
    a166=Answer("Fallout New Vegas", 0, 0, 2)
    Question.addAnswer(q45, a166)
    a167=Answer("Call of Duty: Black Ops 3", 0, 1, 0)
    Question.addAnswer(q45, a167)
    a168=Answer("Civilization V", 0, 0, 2)
    Question.addAnswer(q45, a168)
    a169=Answer("Battlefront II (The one with Rey)", 2, 0, 0)
    Question.addAnswer(q45, a169)
    a170=Answer("The Sims", 0, 2, 0)
    Question.addAnswer(q45, a170)
    embed46 = discord.Embed(title=(str(44)+') '+q45.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q45.Answers:
            embed46.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed46)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q45.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q46=Question('Is Nickelback a terrible band?')
    a171=Answer("Yes", 0, 0, 1)
    Question.addAnswer(q46, a171)
    a172=Answer("No", 0, 1, 0)
    Question.addAnswer(q46, a172)
    a173=Answer("I've never listened to Nickelback", 0, 0, 0)
    Question.addAnswer(q46, a173)
    embed47 = discord.Embed(title=(str(45)+') '+q46.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q46.Answers:
            embed47.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed47)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q46.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q47=Question('Was it wrong for Lexa from "The 100" to be killed off considering she is a lesbian character?  ')
    a174=Answer("Yes, this is damaging for inclusion of LGBTQ+ characters", 3, 0, 0)
    Question.addAnswer(q47, a174)
    a175=Answer("No, characters die all the time in the series. Her sexual orientation isn't relevant", 0, 0, 0)
    Question.addAnswer(q47, a175)
    a176=Answer("I am not familiar with the 100", 0, 0, 0)
    Question.addAnswer(q47, a176)
    embed48 = discord.Embed(title=(str(46)+') '+q47.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q47.Answers:
            embed48.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed48)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q47.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q48=Question('Is Doctor Who casting a woman as The Doctor for the first time a good thing?')
    a177=Answer("Yes", 1, 0, 0)
    Question.addAnswer(q48, a177)
    a178=Answer("No, if they want to promote diversity they should create original characters", 0, 0, 1)
    Question.addAnswer(q48, a178)
    a179=Answer("I am not familiar with Doctor Who", 0, 2, 0)
    Question.addAnswer(q48, a179)
    embed49 = discord.Embed(title=(str(47)+') '+q48.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q48.Answers:
            embed49.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
            i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed49)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q48.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    q49=Question("What is your opinion on the Bechdel Test?")
    a180=Answer("It's a good test to determine if women are well represented", 1, 0, 0)
    Question.addAnswer(q49,a180)
    a181=Answer("Its requirements are not sufficient enough for proper representation of women", 2, 0, 0)
    Question.addAnswer(q49,a181)
    a182=Answer("The test is not sufficient because it only covers two genders", 3, 0, 0)
    Question.addAnswer(q49,a182)
    a183=Answer("The test is flawed, just because something fails it doesn't mean it failed to represent women well", 0, 0, 1)
    Question.addAnswer(q49,a183)
    a184=Answer("I don't know what the Bechdel Test is", 0, 2, 0)
    Question.addAnswer(q49,a184)
    embed50 = discord.Embed(title=(str(48)+') '+q49.content+' for '+str(ctx.message.author)))
    i=0
    for juke in q49.Answers:
        embed50.add_field(name=(alphabet[i]+')'),value=Answer.getContent(juke))
        i+=1
    found=False
    while(found==False): 
            await client.say(embed=embed50)
            msg = await client.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            answer=msg.content.upper()
            try:
                    ooferGang=alphabet.index(answer)
                    if (ooferGang==len(alphabet)-1): 
                            await client.say('Test Ended.')
                            return
                    Klobuchar=q49.Answers[ooferGang]
                    T+=Klobuchar.T
                    I+=Klobuchar.I
                    R+=Klobuchar.R
                    found=True
            except:
                    await client.say('Not a valid answer!')
                    found=False
    tp=T/80
    ip=I/53
    rp=R/83
    embed100=discord.Embed(title="")
    if (tp>rp and tp>ip):
        embed100=discord.Embed(title="Result: Tumblr Party", color = 0x1F618D)
        try:
            user = ctx.message.author
            role = get(ctx.message.server.roles,name="Tumblr")
            await client.add_roles(user,role)
        except:
            pass
        user = ctx.message.author
        role = get(ctx.message.server.roles,name="Instagram")
        await client.remove_roles(user,role)
        print("I tried sir")
        print(str(role))
        try:
            user = ctx.message.author
            role = get(ctx.message.server.roles,name="Reddit")
            await client.remove_roles(user,role)
        except:
            pass
    elif (rp>ip):
        await client.say("Party: Reddit")
        embed100=discord.Embed(title="Result: Reddit Party", color = 0xFF0000)
        try:
            user = ctx.message.author
            role = get(ctx.message.server.roles,name="Reddit")
            await client.add_roles(user,role)
        except:
            pass
        try:
            user = ctx.message.author
            role = get(ctx.message.server.roles,name="Instagram")
            await client.remove_roles(user,role)
        except:
            pass
        try:
            user = ctx.message.author
            role = get(ctx.message.server.roles,name="Tumblr")
            await client.remove_roles(user,role)
        except:
            pass
    else:
        await client.say("Party: Instagram")
        embed100=discord.Embed(title="Result: Instagram Party", color = 0x800080)
        try:
            user = ctx.message.author
            role = get(ctx.message.server.roles,name="Instagram")
            await client.add_roles(user,role)
        except:
            pass
        try:
            user = ctx.message.author
            role = get(ctx.message.server.roles,name="Tumblr")
            await client.remove_roles(user,role)
        except:
            pass
        try:
            user = ctx.message.author
            role = get(ctx.message.server.roles,name="Reddit")
            await client.remove_roles(user,role)
        except:
            pass
    myScore=tp-rp
    ip=ip/10
    if (myScore>0):
        myScore=myScore-ip
        myScore*=100
        myScore=round(myScore)
        if myScore<1:
            myScore=1
        embed100.add_field(name="You are "+str(myScore)+" point(s) to the left.", value="User: "+str(ctx.message.author))
    elif (myScore<0):
        myScore*=-1
        myScore=myScore-ip
        myScore*=100
        myScore=round(myScore)
        if myScore<1:
            myScore=1
        await client.say("You are "+str(myScore)+" points to the right.")
        embed100.add_field(name="You are "+str(myScore)+" point(s) to the right", value="User: "+str(ctx.message.author))
    else:
        embed100.add_field(name="You are exactly in the middle", value="User: "+str(ctx.message.author))
    await client.say(embed=embed100)
    channel=client.get_channel('495103978103767040')
    await client.send_message(channel,embed=embed100)
    user = ctx.message.author
    role = get(ctx.message.server.roles,name="First World Ideologist")
    await client.add_roles(user,role)
    

client.run("****")
