
import os
# import bot lib
from pyrogram import Client,filters,enums
from pyrogram.enums import ChatAction,ChatType,ChatMemberStatus,ParseMode
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
# import conversation handler for pyrogram
from convopyro import Conversation,listen_message

# database lib
from pymongo import MongoClient

# import youtube video search lib
from youtube_search import YoutubeSearch

#url checker lib
from pyLense.Lense import Neurals

# import youtube downloader lib
from pytube import YouTube
from pytube.innertube import _default_clients

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

# admin ID's
admin_id = [1944279581,2069970688,1365625365,1433116770,5249435830]

BotTokn = "<Your Bot Api>"
apiID = 14934789
apiHash = "Your Api-Hash"

bot = Client(name="flippedCoin",api_id=apiID,api_hash=apiHash,bot_token=BotTokn)

group = InlineKeyboardButton(text="Group",url="t.me/neuralg")
channel = InlineKeyboardButton(text="Channel",url="t.me/neuralp")
markup = InlineKeyboardMarkup([[group,channel]])

@bot.on_message(filters.command("start") & filters.private)
def sendWelcome(client,msg):
    user = msg.from_user
    chatID = msg.chat.id
    #print(msg)
    welcomeText = f"""Hello {user.mention}This is youtube audio, video and thumbnail downloader bot. Send the url."""
    msg.reply_text(text=welcomeText,reply_markup=markup,parse_mode=ParseMode.HTML,quote=True)


@bot.on_message(filters.command("broadcast") & filters.private)
def broadcast(client,msg):
    user = msg.from_user
    chatID = msg.chat.id
    userID = user.id
    #print(msg)
    firstName = user.first_name
    userName = user.username
    data = {"userid":userID,"first_name":firstName,"user_name":userName}
    #bot.set_state(msg.from_user.id,Mystate.text,msg.chat.id)
    if msg.from_user.id not in admin_id:
        bot.reply_to(msg,"This command is for admins only!")
    else:
        bot.reply_to(msg,"Send me a broadcasting message:")

@bot.on_message(filters.text & filters.private)
def audioOrVideo(client,msg):
    query = msg.text
    chatID = msg.chat.id
    #print(msg)
    messageID = msg.id
    #print(messageID)
    """
    userID = msg.from_user.id
    firstName = msg.from_user.first_name
    userName = f"@{msg.from_user.username}" 
    data = {"userid":userID,"first_name":firstName,"user_name":userName}
    if users.find_one({"userid":userID}) == None:
        to_db = users.insert_one(data)"""
    
    # create three button
    audioButton = InlineKeyboardButton(text="Audio",callback_data="audio")
    videoButton = InlineKeyboardButton(text="Video",callback_data="video")
    thumnailButton = InlineKeyboardButton(text="Thumbnail",callback_data="thumbnail")
    # add the above three inline buttons together
    choose = InlineKeyboardMarkup([[audioButton,videoButton],[thumnailButton]])

    check = msg.text
    print(check)
    
    isUrl = Neurals(link=check).check()
    #print(isUrl)
    if isUrl == "Yes":
        msg.reply_text(text=msg.text,reply_markup=choose,quote=True)
        # delete the user message after sent to the bot
        bot.delete_messages(chat_id=chatID,message_ids=messageID)
    elif isUrl == "Nah":
        search = YoutubeSearch(search_terms=query,max_results=10).to_dict()
        urlSuffix = search[0]["url_suffix"]
        url = f"https://www.youtube.com{urlSuffix}"
        #print(url)
        msg.reply_text(text=url,reply_markup=choose,quote=True)
   

@bot.on_callback_query()
def downloadAudioVideo(client,query):
    #print(query)
    # this returns what the user clicked
    userClicked = query.data
    #print(userClicked)
    # get the url
    url = query.message.text.strip()
    #print(url)
    # chat id
    chatID = query.message.chat.id
    #print(chatID)
    # message id
    MessageID = query.message.id
   # print(MessageID)

    # create a folder to save the content
    downloadPath = "download"
    if not os.path.exists(downloadPath):
        os.mkdir(downloadPath)
    
    try:
        yt = YouTube(url=url)
        print(yt.title)
        if userClicked =="audio":
            # download the audio
            getAudio = yt.streams.filter(only_audio=True)[0].download(output_path=downloadPath)
            # split the file name and the extension
            base,ext = os.path.splitext(getAudio)
            # rename the file extension to .mp3
            audio = base + ".mp3"
            os.rename(getAudio,audio)
            # open the audio and send to the user
            with open(audio,"rb") as file:
                # send chat action while the file is sending
                bot.send_chat_action(chat_id=chatID,action=ChatAction.UPLOAD_AUDIO)
                audioCaption = yt.title
                bot.send_audio(chat_id=chatID,audio=file,file_name=f"{yt.title}.mp3",caption=audioCaption,reply_markup=markup)
            # delete the file from the system
            os.remove(audio)
        elif userClicked =="video":
            # download the video that have the 720 resolution
            vid = yt.streams.get_by_itag(22).download()
            #print(vid)  
            
            #getVideo = yt.streams.filter(only_video=True)[0].download()
            # open the video and send to the user
            with open(vid,"rb") as file:
                # sleep for 30sec to avoid timeout 
                #time.sleep(30.5)
                # send the chat action while sending the video
                bot.send_chat_action(chat_id=chatID,action=ChatAction.UPLOAD_VIDEO)
                # video caption
                vidCaption = yt.title
                bot.send_video(chat_id=chatID,video=file,file_name=vid,width=1920,height=1080,caption=vidCaption,reply_markup=markup)
            # delete the downloaded video from the system
            os.remove(vid) 
        elif userClicked =="thumbnail":
            thumbnail = yt.thumbnail_url
            print(f"Thumbnail url: {thumbnail}")
            bot.send_photo(chat_id=chatID,photo=thumbnail,reply_markup=markup)

    except Exception as e:
        print(e)
        bot.send_message(chat_id=chatID,text="Please send correct url and try again",reply_to_message_id=MessageID,reply_markup=markup)


print("bot is running")
bot.run()


