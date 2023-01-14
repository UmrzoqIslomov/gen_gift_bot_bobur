from django.shortcuts import render

from tg_bot.Globals import TEXTS
from tg_bot.buttons import btns, inline_btn
from tg_bot.models import *


# Create your views here.


def start(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = User.objects.filter(user_id=user.id).first()

    if not tglog:
        tglog = Log()
        tglog.user_id = user.id
        tglog.message = {"state": 0}
        tglog.save()

    log = tglog.messages

    if not tg_user:
        tg_user = User()
        tg_user.user_id = user.id
        tg_user.name = user.name
        tg_user.username = user.username
        tg_user.save()
        log['state'] = 0
        update.message.reply_text(TEXTS['START'], reply_markup=btns("lang"))

    else:
        if log['state'] >= 10:
            log.clear()
            log['state'] = 10
            update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
        else:
            log['state'] = 0
            update.message.reply_text(TEXTS['START'], reply_markup=btns("lang"))

    tglog.messages = log
    tglog.save()


def message_handler(update, context, ):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = User.objects.filter(user_id=user.id).first()
    log = tglog.messages
    state = log.get('state', 0)
    print(log, state)

    msg = update.message.text
    user = update.message.from_user
    tg_user = User.objects.get(user_id=user.id)
    tglog = Log.objects.filter(user_id=user.id).first()
    msg = update.message.text
    log = tglog.messages
    state = log.get('state', 0)

    if state == 0:
        log['state'] = 1
        if msg == "🇺🇿Uz":
            print("uz")
            tg_user.lang = 1
            tg_user.save()
        elif msg == "🇷🇺Ru":
            print("A")
            tg_user.lang = 2
            tg_user.save()
        else:
            update.message.reply_text(TEXTS['START'], reply_markup=btns("lang"))
            return 0
        update.message.reply_text(TEXTS['NAME'][tg_user.lang])
        tglog.messages = log
        tglog.save()
        return 0

    if log['state'] == 1:
        if msg.isalpha():
            log['name'] = msg
            log['state'] = 2
            update.message.reply_text(TEXTS["CONTACT"][tg_user.lang], reply_markup=btns('contact', lang=tg_user.lang))
        else:
            update.message.reply_text(TEXTS['ERROR1'][tg_user.lang])

    elif log['state'] == 2:
        update.message.reply_text(TEXTS['CONTACT2'][tg_user.lang])
        print(msg)
    # if msg == TEXTS['Back'][1] or msg == TEXTS['Back'][2]:
    #     if log['state'] == 17:
    #         log['state'] = 16
    #         update.message.reply_text(TEXTS['Year'][tg_user.lang], reply_markup=btns('age', lang=tg_user.lang))
    #         tglog.messages = log
    #         tglog.save()
    #         return 0
    #     elif log['state'] == 16:
    #         log['state'] = 15
    #         update.message.reply_text(TEXTS['Pul'][tg_user.lang], reply_markup=btns('cash', lang=tg_user.lang))
    #         tglog.messages = log
    #         tglog.save()
    #         return 0
    #     elif log['state'] == 15:
    #         log['state'] = 14
    #         update.message.reply_text(TEXTS['Interest'][tg_user.lang], reply_markup=btns('interests', lang=tg_user.lang))
    #         tglog.messages = log
    #         tglog.save()
    #         return 0
    #     elif log['state'] == 14:
    #         log['state'] = 13
    #         update.message.reply_text(TEXTS['Holat'][tg_user.lang], reply_markup=btns('situation', lang=tg_user.lang))
    #         tglog.messages = log
    #         tglog.save()
    #         return 0
    #     elif log['state'] == 13:
    #         log['state'] = 12
    #         update.message.reply_text(TEXTS['Human'][tg_user.lang], reply_markup=btns('human', lang=tg_user.lang))
    #         tglog.messages = log
    #         tglog.save()
    #         return 0
    #     elif log['state'] == 12:
    #         log['state'] = 11
    #         update.message.reply_text(TEXTS['SOVGA'][tg_user.lang], reply_markup=btns("ctg", lang=tg_user.lang))
    #         tglog.messages = log
    #         tglog.save()
    #         return 0
    #     elif log['state'] == 11:
    #         log['state'] = 10
    #         update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
    #         tglog.messages = log
    #         tglog.save()
    #         return 0

    if msg == TEXTS['Back'][1] or msg == TEXTS['Back'][2]:
        if log['state'] == 17:
            log['state'] = 16
            update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
            tglog.messages = log
            tglog.save()
            return 0
        elif log['state'] == 16:
            log['state'] = 15
            update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
            tglog.messages = log
            tglog.save()
            return 0
        elif log['state'] == 15:
            log['state'] = 14
            update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
            tglog.messages = log
            tglog.save()
            return 0
        elif log['state'] == 14:
            log['state'] = 13
            update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
            tglog.messages = log
            tglog.save()
            return 0
        elif log['state'] == 13:
            log['state'] = 12
            update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
            tglog.messages = log
            tglog.save()
            return 0
        elif log['state'] == 12:
            log['state'] = 11
            update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
            tglog.messages = log
            tglog.save()
            return 0
        elif log['state'] == 11:
            log['state'] = 10
            update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
            tglog.messages = log
            tglog.save()
            return 0

    if msg == TEXTS['SOVGA'][1] or msg == TEXTS['SOVGA'][2]:
        log['state'] = 11
        update.message.reply_text(TEXTS['SOVGA'][tg_user.lang], reply_markup=btns("ctg", lang=tg_user.lang))
        print("ctg ciqti")

    elif log['state'] == 11:
        log['state'] = 12
        log['ctg'] = msg
        l = "uz" if tg_user.lang == 1 else "ru"
        d = {
            f"name_{l}": msg
        }
        print("human ciqti")
        ctg = Category.objects.filter(**d).first()
        if not ctg:
            update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
            return 0
        update.message.reply_text(TEXTS['Human'][tg_user.lang], reply_markup=btns('human', ctg=ctg, lang=tg_user.lang))

    elif log['state'] == 12:
        log['state'] = 13
        log['human'] = msg
        l = "uz" if tg_user.lang == 1 else "ru"
        d = {
            f"name_{l}": msg
        }
        human = Human.objects.filter(**d).first()
        if not human:
            update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
            return 0
        update.message.reply_text(TEXTS['Holat'][tg_user.lang],
                                  reply_markup=btns('situation', human=human, lang=tg_user.lang))
        print("situation ciqti")

    elif log['state'] == 13:
        log['state'] = 14
        log['situation'] = msg
        print("interest ciqti", msg)
        l = "uz" if tg_user.lang == 1 else "ru"
        d = {
            f"name_{l}": msg
        }
        situation = Situation.objects.get(**d)
        if not situation:
            update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
            return 0
        # situation = Interests.objects.filter(situation=stt)
        update.message.reply_text(TEXTS['Interest'][tg_user.lang],
                                  reply_markup=btns('interests', situation=situation, lang=tg_user.lang))
        print("interest buttoni ciqti")

    elif log['state'] == 14:
        log['state'] = 15
        log['interests'] = msg
        print("cash ciqti", msg)
        l = "uz" if tg_user.lang == 1 else "ru"
        d = {
            f"name_{l}": msg
        }
        interests = Interests.objects.get(**d)
        if not interests:
            update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
            return 0
        update.message.reply_text(TEXTS['Pul'][tg_user.lang],
                                  reply_markup=btns('cash', interests=interests, lang=tg_user.lang))
        print("cash buttoni ciqti")

    elif log['state'] == 15:
        log['state'] = 16
        log['cash'] = msg
        print("age ciqti", msg)
        l = "uz" if tg_user.lang == 1 else "ru"
        d = {
            f"name_{l}": msg
        }
        cash = Cash.objects.get(**d)
        if not cash:
            update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
            return 0
        update.message.reply_text(TEXTS['Year'][tg_user.lang], reply_markup=btns('age', cash=cash, lang=tg_user.lang))
        print("age buttoni ciqti")

    elif log['state'] == 16:
        log['state'] = 17
        log['age'] = msg
        l = "uz" if tg_user.lang == 1 else "ru"
        d = {
            f"name_{l}": msg
        }
        age = Agee.objects.filter(**d).first()
        if not age:
            update.message.reply_text(TEXTS['ERROR'][tg_user.lang])
            return 0
        update.message.reply_text(TEXTS['Gift'][tg_user.lang],
                                  reply_markup=btns(type='product', age=msg, lang=tg_user.lang))

    elif log['state'] == 17:
        log['state'] = 17
        log['product'] = msg
        print("kirdi")
        log["nta"] = 1
        l = "uz" if tg_user.lang == 1 else "ru"
        d = {
            f"name_{l}": msg
        }
        product = Product.objects.filter(**d).first()
        update.message.reply_text(TEXTS['Gift'][tg_user.lang], reply_markup=btns("prod"))

        print(product)
        Name = f"Name: {getattr(product, f'name_{l}')}\n" if getattr(product, f'name_{l}') else ""
        Description = f"Description: {getattr(product, f'description_{l}')}\n" if getattr(product,
                                                                                          f'description_{l}') else ""
        context.bot.send_photo(
            photo=open(f'{product.img.path}', 'rb'),
            caption=f"{Name}{Description}",
            chat_id=user.id,
            # reply_markup=inline_btn('prod', nta=log['nta']),
        )

    tglog.messages = log
    tglog.save()


def contact_handler(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = User.objects.filter(user_id=user.id).first()
    log = tglog.messages

    contact = update.message.contact
    log['contact'] = contact.phone_number

    print(log, contact)
    if log['state'] == 2:
        tg_user.name = log['name']
        tg_user.phone = log['contact']
        tg_user.save()
        log.clear()
        log['state'] = 10
        update.message.reply_text(TEXTS['MENU1'][tg_user.lang], reply_markup=btns('menu', lang=tg_user.lang))
        print('number')
    tglog.messages = log
    tglog.save()
