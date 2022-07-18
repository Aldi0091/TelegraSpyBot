# TelegraSpyBot

(Follow below for English)
Это мой компактный, но эффективный бот-шпион, просто чтобы испытать свои навыки

Прежде всего, вам необходимо получить свой Telegram API api_hash и api_id через 
> https://my.telegram.org/auth?to=apps

Также вам необходимо создать своего бота через BotFather и получить свой токен

Затем установите зависимости
> pip install -r requirements.txt

Вам нужно ввести имя пользователя(юзернэйм), за которым вы хотите мониторить, я указал его в скрипте здесь в одинарных кавычках ниже
> account = await client.get_entity('') # set username here without '@'

Запустите скрипт

Запустите своего бота в Telegram

Примечание: имя пользователя(юзернэйм) должно быть в ваших контактах

PS: иногда сервер telegram может забанить вас из-за слишком большого количества запросов, что я пытаюсь сейчас выяснить, как это решить.

This is my small but efficient spy bot, just to try my skills

First of all you need to obtain your Telegram API api_hash and api_id through 
> https://my.telegram.org/auth?to=apps

Also you need to create your bot through BotFather and obtain your token

Then run the requirements
> pip install -r requirements.txt

You need to put the username that you want to spy after, I have indicated it there in the scipt here in single quote below
> account = await client.get_entity('') # set username here without '@'

Run the script

Run your bot in the Telegram

Note: that the username shall be within your contacts

PS: sometimes telegram server may ban you because of too much request. That's what I am now trying to figure out how to resolve it.
