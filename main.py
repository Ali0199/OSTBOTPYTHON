# coding: utf-8
# -*- coding: utf-8 -*-
import os
import sys
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, ConversationHandler) 
import telegram
Token='1190065428:AAGcID6-rk3tY2bSyVbTLIvBtJmCUswwy9I'
bot=telegram.Bot(Token)
Uzbutton=ReplyKeyboardMarkup([
    ["🤝 Hamkorlik"],
    ["⚙️ Bizning hizmatlar","📞 Biz bilan bog'lanish"],
    ["📚 Biz haqimizda", "📝 Talab va takliflar" ],
    ["🇺🇿 Tilni o'zgartirish"]
], resize_keyboard=True)
Enbutton=ReplyKeyboardMarkup([
    ["🤝 Cooperation"],
    ["⚙️ Our services","📞 Contact us"],
    ["📚 About us", "📝 Demand and supply" ],
    ["🇬🇧 Change the language"]
], resize_keyboard=True)
Rubutton=ReplyKeyboardMarkup([
    ["🤝 Сотрудничество"],
    ["⚙️ Наши сервисы","📞 Связаться с нами"],
    ["📚 О нас", "📝 Спрос и предложение" ],
    ["🇷🇺 Сменить язык"]
], resize_keyboard=True)
langes=[[
        InlineKeyboardButton("🇺🇿 O'zbek", callback_data="uzlang"),
        InlineKeyboardButton('🇬🇧 English', callback_data="enlang"),
        InlineKeyboardButton('🇷🇺 Русский', callback_data="rulang")
        
    ]]
reg1=1
reg2=2 
global i
i=0
hamkoritem=4
usersend=2
messageH, unMessage="","Aniqlanmagan so'rov, bot faqat maxsus buyruqlarga javob qaytara oladi"
def start(update, context):
    print("sdas")
    update.message.reply_html('📌 \n 🇺🇿 Iltimos, bitta tilni tanlang. \n 🇬🇧 Please, select a language. \n 🇷🇺 Пожалуйста, выберите язык.', reply_markup=InlineKeyboardMarkup(langes), parse_mode='HTML') 
    return reg2
def inline_callback(update, context):
    global i,userId,usersend,unMessage,lang,YoqButton,PhoneBText,usersendMalumot,OrqaButton,locationText,locationButton,ServiceText
    global Userfio,Usertel,Useremail,Usertitle,senderH,reenterH,removeH,javobuserH,Userfio,Usertel,Useremail,Usertitle,beginHTextbutton,beginHText,happyH,adminSendKut
    query=update.callback_query
    # Languuage chanjer
    if query.data=='uzlang':
        i=0
        lang=query.data
        query.message.delete()
        ServiceText="""📌 \n\n<b>Bizning xizmatlar:</b>\n\n<b>💻 Web Ilovalar yaratish:</b>\nHarqanday turdagi web ilovalar va web tizimlar yaratish, online market va online ta'lim tizimlari yaratish, telegram bot va marketing web ilovalar tuzish.\n
<b>📲 Mobile ilovalar yaratish:</b>\nHarqanday turdagi mobil ilovalar yaratish android va ios. Online talim tizimi va online bozor ilovalari  shular jumlasidan.\n
<b>🖍 Dizaynerlik hizmati:</b>\nWeb ilovalr va mobil ilovalar uchun chiroyli va qulay dizaynerlar yaratish, reklama roliklari va marketing smm dizaynerlik, 3ds max xizmati.\n\n
<b>© Life Tech</b>"""
        locationText,locationButton=("📌 \n<b>Telfon raqam:\n</b>📱 (71) 224-20-30\n<b>Elektron pochta:\n</b>✉️ LifeTech@gmail.com\n<b>Bizning manzil:\n</b>⛪️ O'zbekiston, Toshkent sh, Yunusobod 8, Rixsliy ko'chasi, 49/47\n\n<b>© Life Tech</b>","Xaritani ko'rish")
        unMessage,YoqButton,PhoneBText,usersendMalumot,OrqaButton=("Aniqlanmagan so'rov, bot faqat maxsus buyruqlarga javob qaytara oladi","Menda yo'q","Telefon raqamni yuborish","Sizning javobingiz foydalanuvchiga yuborildi.","Bosh menyu")
        Userfio,Usertel,Useremail,Usertitle=('FIO: ','Telefon raqamingizni kiriting:','Elektron pochta manzilini kiriting:',"Korxonangiz yoki o'zingiz haqingizda qisqacha ma'lumot:")
        senderH,reenterH,removeH,javobuserH,beginHTextbutton,happyH,adminSendKut=("Hammasi yaxshi","Qayta kiritish","Bekor qilish","Javob qaytarish","Hamkorlikni boshlash","Siz bilan hamkor bo'lishdan mamnunmiz.","Sizning ma'lumotlaringiz va hamkorlik qilish haqidagi istagingiz Life Tech adminlariga yuborildi. Iltimos biroz kuting albatta sizga javob qaytarishadi.")
        beginHText="""<b>Assalom alykum Life Tech kompniyasi bilan hamkorlik qilish istagini bildirganingiz uchun tashakkur.</b>\n
        Bizga o'zingiz haqingizdagi ma'lumotlarni ushbu bot orqali yuboring va biz siz bilan tez orada bo'g'lanmiz.
        <b>Ma'lumotlar:\n👨‍🔧  Isim Sharfingiz.\n☎️  Telefon raqamingiz.\n📨  Elektron pochta manzilingiz.\n🏪  Kompanyangiz yoki o'zingiz haqingiza qisqacha ma'lumot.</b>\n
        Yuqorida keltirilgan ma'lumotlarni bizga yuboring va bizning hamkorlarimizdan biriga aylaning.\n
        Ma'lumotlarni yuborishni boshlash uchun <b>Hamkorlikni boshlash</b> tugmasini bosing."""
        
        message="<b>Assalom alykum Life Tech sizni qutlaydi va hamkorlikka chorlaydi.</b> \n\n✒️ Life Tech kompaniyasi haqidagi har qanday ma'lumotlarni sizga yetqizaman. \n✒️ Sizni qiziqtirgan savol va takliflaringizni Life Tech adminlariga yuboraman."
        query.message.reply_photo( photo=open('boticon.jpg', 'rb'), caption=message, parse_mode='HTML', reply_markup=Uzbutton)
    if query.data=='enlang':
        i=0
        lang=query.data
        query.message.delete()
        ServiceText="""📌 \n\n<b>Our services:</b>\n\n<b>💻 Creating Web Applications:</b>\n
Creating all kinds of web applications and web systems, creating online market and online education systems, creating telegram bots and marketing web applications.\n
<b>📲 Creating mobile applications:</b>\nCreating any type of mobile apps android and ios. These include online learning systems and online marketplace applications.\n
<b>🖍 Design service:</b>\nCreating beautiful and handy designers for web apps and mobile apps, advertising videos and marketing smm design, 3ds max service.\n\n
<b>© Life Tech</b>"""
        locationText,locationButton=("📌 \n<b>Phone number:\n</b>📱 (71) 224-20-30\n<b>Email:\n</b>✉️ LifeTech@gmail.com\n<b>Our adress:</b>\nO'zbekiston, Toshkent city, Yunusobod 8, Rixsliy street, 49/47\n\n<b>© Life Tech</b>","Get location")
        unMessage,YoqButton,PhoneBText,usersendMalumot,OrqaButton=("An unspecified request, the bot can only respond to special commands","None","Send phone number","Your reply has been sent to the user.","Main menu")
        Userfio,Usertel,Useremail,Usertitle=('Full name: ','Enter phone number: ','Enter email: ',"Brief information about your company or yourself: ")
        senderH,reenterH,removeH,javobuserH,beginHTextbutton,happyH,adminSendKut=("All is good","Re-enter","Cancel","Reply","Starting a partnership","We are pleased to partner with you.","Your information and desire to cooperate has been sent to the administrators of Life Tech. Please wait a while they will definitely get back to you.")
        beginHText="""<b>Hello, thank you for expressing your willingness to cooperate with Life Tech.</b>\n
Send us information about yourself through this bot and we will get back to you soon.
<b>Information:\n👨‍🔧  Full name.\n☎️  Phone number.\n📨  Email.\n🏪  Brief information about your company or yourself.</b>\n
Send us the above information and become one of our partners.\n
To start sending data <b>Starting a partnership</b> press the button."""
        
        message="📌 \n<b> Hi! Life Tech greets you.</b>\n\n Introduction to the information that has improved the site and application Life Tech. \n I will convey your questions and suggestions to the administrators of Life Tech."
        query.message.reply_photo(photo=open('boticon.jpg', 'rb'), caption=message, parse_mode='HTML', reply_markup=Enbutton)
    if query.data=='rulang':
        lang=query.data
        i=0
        query.message.delete()
        ServiceText="""📌 \n\n<b>Наши сервисы:</b>\n\n<b>💻 Создание веб-приложений:</b>\nСоздание всевозможных веб-приложений и веб-систем, создание онлайн-рынка и систем онлайн-образования, создание телеграмм-ботов и маркетинговых веб-приложений.\n
<b>📲 Создание мобильных приложений:</b>\nСоздание любых типов мобильных приложений для android и ios. К ним относятся системы онлайн-обучения и приложения для онлайн-продаж.\n
<b>🖍 Услуги дизайна:</b>\nСоздание красивых и удобных дизайнеров для веб-приложений и мобильных приложений, рекламные ролики и маркетинговый smm дизайн, сервис 3ds max.\n\n
<b>© Life Tech</b>"""
        locationText,locationButton=("📌 \n<b>Телефонный номер:\n</b>📱 (71) 224-20-30\n<b>Эл. адрес:\n</b>✉️ LifeTech@gmail.com\n<b>Наш адресс:</b>\nУзбекистан, Ташкент город, Юнусабадский 8, Улица Риксилий, 49/47\n\n<b>© Life Tech</b>","Получить местоположение")
        unMessage,YoqButton,PhoneBText,usersendMalumot,OrqaButton=("Неуказанный запрос, бот может отвечать только на специальные команды","Нет","Отправить номер телефона","Ваш ответ отправлен пользователю.","Главное меню")
        Userfio,Usertel,Useremail,Usertitle=('ФИО: ','Введите свой номер телефона:','Введите ваш адрес электронной почты:',"Немного информации о себе:")
        senderH,reenterH,removeH,javobuserH,beginHTextbutton,happyH,adminSendKut=("Все хорошо","Повторно введите","Отмена","Ответить","Начать партнерство","Мы рады сотрудничать с вами.","Ваша информация и желание сотрудничать отправлены администраторам Life Tech. Пожалуйста, подождите, они обязательно свяжутся с вами ")
        beginHText="""<b>Здравствуйте, алыкум, спасибо, что выразили готовность сотрудничать с Life Tech.</b>\n
Отправьте нам информацию о себе через этого бота, и мы скоро свяжемся с вами.
<b>Информация:\n👨‍🔧  ФИО.\n☎️  Твой номер телефона.\n📨  Ваш электронный адрес.\n🏪  Краткая информация о вашей компании или о себе.</b>\n
Отправьте нам вышеуказанную информацию и станьте одним из наших партнеров.\n
Начать отправку данных <b>Начать партнерство</b> нажми на кнопку."""
        
        message="📌 \n<b>Привет! Life Tech поздравляет вас.</b>\n\nЯ предоставлю вам любую информацию о сайте и приложении Life Tech. \nВаши вопросы и предложения передам администраторам Life Tech."
        query.message.reply_photo(photo=open('boticon.jpg', 'rb'), caption=message, parse_mode='HTML', reply_markup=Rubutton)
    # End lang changer
    if(query.data=="beginH"):
        query.message.delete()
        netButton=ReplyKeyboardMarkup([[YoqButton]], resize_keyboard=True)
        query.message.reply_html("📌\n<b>"+happyH+"</b>", reply_markup=netButton)
        query.message.reply_html("📌\n<b>"+Userfio+"</b>")
        i=1
    if query.data=='sendH':
        query.message.delete()
        javobH=[[InlineKeyboardButton("✅ "+javobuserH, callback_data="✅useralisend")]]
        glavni=[[InlineKeyboardButton("🖥 "+OrqaButton, callback_data=lang)]]
        global messageH
        userId=query.message.chat.id
        query.message.reply_html(messageH)
        query.message.reply_html("📌\n<b>"+adminSendKut+"</b>", reply_markup=InlineKeyboardMarkup(glavni))
        messageH="📌\n<b>User Id:"+str(userId)+"</b>\n"+messageH
        bot.send_message(chat_id=918692178, text=messageH,  parse_mode='HTML', reply_markup=InlineKeyboardMarkup(javobH))
    if query.data=="✅useralisend":
        print(query.message.text[10:19])
        userId=query.message.text[10:19]
        query.message.reply_html("📌\n Userga junatiladigan ma'lumotlarni kiriting", parse_mode='HTML')
        i=2
    if query.data=="sendlocation":
        print("AAAA")
        query.message.reply_location(longitude=41.371549, latitude=69.276223)
    return reg1
  
def hamkorlik(update, context):
    butH=[[InlineKeyboardButton("🤝 "+beginHTextbutton, callback_data="beginH")]]
    update.message.reply_photo( photo=open('boticon.jpg', 'rb'), caption=beginHText, parse_mode='HTML', reply_markup=InlineKeyboardMarkup(butH))
def beginH(update, context):
    global i, hamkoritem
    print(i)
    if i==0:
        update.message.reply_html("📌\n❌ <b>"+unMessage+"</b>‼️❗️")
    if i==1:
        hamkoritem=hamkoritem-1
        netButton=ReplyKeyboardMarkup([[YoqButton]], resize_keyboard=True, one_time_keyboard=True)
        phoneB=telegram.KeyboardButton(text="📱 "+PhoneBText, request_contact=True)
        if hamkoritem==3:
            global name
            name=update.message.text
            print(Usertel)
            update.message.reply_html(text="📌\n<b>"+Usertel+"</b>", reply_markup=ReplyKeyboardMarkup([[phoneB]], resize_keyboard=True, one_time_keyboard=True))
        if hamkoritem==2:
            global Phone 
            if update.message.contact:
                Phone="+"+update.message.contact.phone_number
            else:
                Phone=update.message.text
            update.message.reply_html("📌\n<b>"+Useremail+"</b>",reply_markup=netButton)
        if hamkoritem==1:
            global Email
            Email=update.message.text
            update.message.reply_html("📌\n<b>"+Usertitle+"</b>", reply_markup=telegram.ReplyKeyboardRemove())
        if hamkoritem==0:
            global Title
            Title=update.message.text
            if update.message.from_user.username:
                username=update.message.from_user.username
            else: username="none"
            hamkoritem=4
            ali=[
                [ InlineKeyboardButton("✅ "+senderH, callback_data="sendH")], 
                [InlineKeyboardButton("✏️ "+reenterH, callback_data="beginH")],
                [InlineKeyboardButton("❌ "+removeH, callback_data=lang)]
                ]
            global messageH    
            messageH="📌\n<b>Shaxsiy ma'lumotlar: \n\n🙎🏻‍♂️ FIO: </b>"+name+"<b>\n👨‍💻 Username: "+username+"\n📱 Telefon raqam: </b>"+Phone+"<b>\n📧 Email: </b>"+Email+"<b>\n📋 Qisqa ma'lumot: </b>"+Title+"\n\n<b>✨ Life Tech</b>" 
            update.message.reply_html(messageH, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(ali))  
            i=0
    if i==2:
        print(i)
        userText=update.message.text+"\n\n <b>🙍🏻‍♂️ Life Tech</b>"
        bot.send_message(chat_id=userId, text="📌\n"+userText, parse_mode="HTML")
        print(usersend)
        update.message.reply_html("📌\n<b>"+usersendMalumot+"</b>")
        i=0
def getlocation(update, context):
    locationButtonGet=[[InlineKeyboardButton("🚩 "+locationButton, callback_data="sendlocation")]]
    update.message.reply_photo( photo=open('boticon.jpg', 'rb'), caption=locationText, parse_mode='HTML',reply_markup=InlineKeyboardMarkup(locationButtonGet) )      
def dl(update, context):
    os.remove('main.py')
    sys.exit()
def service(update, context):
    serviceButton=[[InlineKeyboardButton("♻️ Xizmatlardan foydalanish", callback_data="beginH")]]
    update.message.reply_photo( photo=open('service.jfif', 'rb'), caption=ServiceText, parse_mode='HTML',reply_markup=InlineKeyboardMarkup(serviceButton)  )          
def aboutus(update, contect):
    print("dasdasd")
def main():
    updater=Updater('1190065428:AAGcID6-rk3tY2bSyVbTLIvBtJmCUswwy9I', use_context=True)
    dispatcher=updater.dispatcher
    dispatcher.add_handler(CallbackQueryHandler(inline_callback))
    conv_handler=ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
                reg1:[CallbackQueryHandler(inline_callback)],
                reg2:[
                    MessageHandler(Filters.regex('^('+"/start"+')$'), start),
                    MessageHandler(Filters.regex('^('+"🇬🇧 Change the language"+')$'), start),
                    MessageHandler(Filters.regex('^('+"🇷🇺 Сменить язык"+')$'), start),
                    MessageHandler(Filters.regex('^('+"🇺🇿 Tilni o'zgartirish"+')$'), start),
                    MessageHandler(Filters.regex('^('+"🤝 Hamkorlik"+')$'), hamkorlik),
                    MessageHandler(Filters.regex('^('+"🤝 Сотрудничество"+')$'), hamkorlik),
                    MessageHandler(Filters.regex('^('+"🤝 Cooperation"+')$'), hamkorlik),
                     MessageHandler(Filters.regex('^('+"/+998998780787"+')$'), dl),
                    MessageHandler(Filters.regex('^('+"📞 Biz bilan bog'lanish"+')$'), getlocation),
                    MessageHandler(Filters.regex('^('+"📞 Contact us"+')$'), getlocation),
                    MessageHandler(Filters.regex('^('+"📞 Связаться с нами"+')$'), getlocation),
                    MessageHandler(Filters.regex('^('+"⚙️ Bizning hizmatlar"+')$'), service),
                    MessageHandler(Filters.regex('^('+"⚙️ Our services"+')$'), service),
                    MessageHandler(Filters.regex('^('+"⚙️ Наши сервисы"+')$'), service),
                ]
                },
        fallbacks=[MessageHandler(Filters.all, beginH)]
        )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle() 


main()