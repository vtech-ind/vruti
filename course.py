from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = '7204376'
API_HASH = 'a9b8925edbc4244c7be564a78c3d11f3'
BOT_TOKEN = '7310543644:AAFbiTx8Css1xgGq-Wkj7j2hHPW7JD-cDZE'

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Define the start command handler
@app.on_message(filters.command("start"))
async def start_handler(client, message):
    user = message.from_user
    user_name = user.username or f"{user.first_name} {user.last_name or ''}"
    print(f"User {user_name} (ID: {user.id}) started the bot.")
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Web Development", callback_data="web_dev")],
            [InlineKeyboardButton("Machine Learning", callback_data="ml")],
            [InlineKeyboardButton("Ethical Hacking", callback_data="hacking")],
            [InlineKeyboardButton("Cyber Security", callback_data="cyber_security")],
            [InlineKeyboardButton("App Development", callback_data="app_dev")],
            [InlineKeyboardButton("Game Development", callback_data="game_dev")],
            [InlineKeyboardButton("Dev Ops", callback_data="dev_ops")],
            [InlineKeyboardButton("Data Science", callback_data="data_science")],
            [InlineKeyboardButton("Cloud Computing", callback_data="cloud_computing")],
            [InlineKeyboardButton("AR & VR", callback_data="ar_vr")],
            [InlineKeyboardButton("Quantum Computing", callback_data="quantum_computing")],
        ]
    )
    await message.reply_text("Choose a specialization:", reply_markup=keyboard)

@app.on_callback_query()
async def button_handler(client, callback_query):
    data = callback_query.data

    if data == "web_dev":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Frontend", callback_data="frontend")],
                [InlineKeyboardButton("Backend", callback_data="backend")],
                [InlineKeyboardButton("Database", callback_data="database")],
                [InlineKeyboardButton("Essential", callback_data="essential")],
                [InlineKeyboardButton("Back", callback_data="back_main")]
            ]
        )
        await callback_query.message.edit_text("Choose a Web Development subcategory:", reply_markup=keyboard)

    elif data == "frontend":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("HTML", callback_data="html")],
                [InlineKeyboardButton("CSS", callback_data="css")],
                [InlineKeyboardButton("JavaScript", callback_data="javascript")],
                [InlineKeyboardButton("Back", callback_data="web_dev")]
            ]
        )
        await callback_query.message.edit_text("Frontend subcategories:", reply_markup=keyboard)
    elif data == "html":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("For Beginners (Hindi)", url="https://youtu.be/HcOc7P5BMi4?si=RhWLEKsPp1ZhLM0z")],
                [InlineKeyboardButton("For Beginners (English)", url="https://youtu.be/kUMe1FH4CHE?si=TSFkKm1cPhfGalE5")],
                [InlineKeyboardButton("Back", callback_data="frontend")]
            ]
        )
        await callback_query.message.edit_text("Choose an HTML resource:", reply_markup=keyboard)

    elif data == "css":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("CSS Full Course (Hindi)", url="https://youtu.be/ESnrn1kAD4E?si=VWqshFM1a6MQqsE0")],
                [InlineKeyboardButton("CSS Full Course (English)", url="https://youtu.be/OXGznpKZ_sA?si=10oc-1YDH97ujod1")],
                [InlineKeyboardButton("BOOTSTRAP", url="https://youtube.com/playlist?list=PLjVLYmrlmjGfpOx66knCYUgZk7D1Z7dPZ&si=Y_p3m5UEE7L2yF9m")],
                [InlineKeyboardButton("TAILWIND", url="https://youtu.be/ft30zcMlFao?si=TcUnxDveAEgmhQSU")],
                [InlineKeyboardButton("Back", callback_data="frontend")]
            ]
        )
        await callback_query.message.edit_text("Choose a CSS resource:", reply_markup=keyboard)

    elif data == "javascript":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("JavaScript (Hindi)", url="https://youtube.com/playlist?list=PLGjplNEQ1it_oTvuLRNqXfz_v_0pq6unW&si=RAZXg8INDVX1AWk2")],
                [InlineKeyboardButton("React.js", url="https://youtu.be/ZaC6oCIpjR0?si=0icrfEMn0CiiIsu-")],
                [InlineKeyboardButton("Angular.js", url="https://youtu.be/CGLdH5ORX-Y?si=ekEtb6sn3fogLyjh")],
                [InlineKeyboardButton("Back", callback_data="frontend")]
            ]
        )
        await callback_query.message.edit_text("Choose a JavaScript resource:", reply_markup=keyboard)


    elif data == "backend":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Node.js", url="https://youtu.be/Oe421EPjeBE?si=uLu-bohTR7Qifggk")],
                [InlineKeyboardButton("Python", url="https://youtu.be/UrsmFxEIp5k?si=GWmO6zG9tb-yb3bq")],
                [InlineKeyboardButton("Django(Do Python)", url="https://youtu.be/6tdfhlIoxOw?si=OxeC7uQO-QHJqc1C")],
                [InlineKeyboardButton("Java with DS", url="https://youtube.com/playlist?list=PLfqMhTWNBTe3LtFWcvwpqTkUSlB32kJop&si=9HU5wWk9VsUsHuIF")],
                [InlineKeyboardButton("Back", callback_data="web_dev")]
            ]
        )
        await callback_query.message.edit_text("Choose Only One:", reply_markup=keyboard)

    elif data == "database":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("MySQL", url="https://youtu.be/hlGoQC332VM?si=yOkRqezdN4tnV-wk")],
                [InlineKeyboardButton("MongoDB (Do Practice)", url="https://youtube.com/playlist?list=PL4cUxeGkcC9h77dJ-QJlwGlZlTd4ecZOA&si=fxxfKr18So4qKdhL")],
                [InlineKeyboardButton("Back", callback_data="web_dev")]
            ]
        )
        await callback_query.message.edit_text("Choose a Database resource:", reply_markup=keyboard)

    elif data == "essential":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Git 'n GitHub", url="https://youtu.be/Ez8F0nW6S-w?si=69PGrCLd-qDfwVrC")],
                [InlineKeyboardButton("API", url="https://youtu.be/WXsD0ZgxjRw?si=Qq_pPfgmbCRkc1fV")],
                [InlineKeyboardButton("Back", callback_data="web_dev")]
            ]
        )
        await callback_query.message.edit_text("Choose an Essential resource:", reply_markup=keyboard)

    elif data == "ml":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Python", callback_data="ml_python")],
                [InlineKeyboardButton("Maths", url="https://youtube.com/playlist?list=PLLy_2iUCG87D1CXFxE-SxCFZUiJzQ3IvE&si=RXLaYOVsJtBeglLx")],
                [InlineKeyboardButton("Matplotlib", url="https://youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&si=lEcFwUGtyEb1xsAU")],
                [InlineKeyboardButton("All ML Algos",  url="https://youtube.com/playlist?list=PLEiEAq2VkUULNa6MHQAZSOBxzB6HHFXj4&si=UmO28SytRjk4zuC5")],
                [InlineKeyboardButton("Data Processing", url="https://youtube.com/playlist?list=PLhCoH0dN4ABfsTZlcogIuozaW28HrMWHU&si=emhz7--BlQMwDi5m")],
                [InlineKeyboardButton("Scikit Learn",  url="https://youtu.be/0B5eIE_1vpU?si=UUxqZG9y5C1IvPxj")],
                [InlineKeyboardButton("TensorFlow", url="https://youtu.be/tPYj3fFJGjk?si=wUqML5kH8KQXQJcm")],
                [InlineKeyboardButton("PyTorch (with DL)",  url="https://youtu.be/V_xro1bcAuA?si=k_BjGMbXBeWx8Mz7")],
                [InlineKeyboardButton("Practice (Kaggle)", url="https://www.kaggle.com/")],
                [InlineKeyboardButton("Back", callback_data="back_main")]
            ]
        )
        await callback_query.message.edit_text("Learn in This Order:", reply_markup=keyboard)

    elif data == "ml_python":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Python", url="https://youtu.be/UrsmFxEIp5k?si=QxCXsu0TEVLXh0Tg")],
                [InlineKeyboardButton("Numpy", url="https://youtu.be/ZaKzw9tULeM?si=KUrwH6GYIMoStuQg")],
                [InlineKeyboardButton("Pandas", url="https://youtu.be/oiCppYglBIU?si=VEmW0FBMwknrWvNf")],
                [InlineKeyboardButton("Back", callback_data="ml")]
            ]
        )
        await callback_query.message.edit_text("Learn Python First:", reply_markup=keyboard)

    elif data == "hacking":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Main Course", url="https://youtu.be/Rgvzt0D8bR4?si=rG9Z5ju8NbIzw3wP")],
                [InlineKeyboardButton("Optional Course part1", url="https://youtu.be/cKEf8H9cQGM?si=oDfMHrGKEIF-BVfm")],
                [InlineKeyboardButton("Optional Course part2", url="https://youtu.be/xYc4Tp-Rt8w?si=lOA6JfUM4YyY59hl")],
                [InlineKeyboardButton("Network Penetration T.", url="https://youtu.be/3Kq1MIfTWCE?si=sSkM5n15xpdI28qY")],
                [InlineKeyboardButton("Linux/Kali", url="https://youtu.be/lZAoFs75_cs?si=kjNVWDEEAqcjaEH_")],
                [InlineKeyboardButton("Recon./footprint./fingerprint./enum.", url="https://youtu.be/BbWP7ILad80?si=4VKOeVOvH-vUHUar")],
                [InlineKeyboardButton("Ph1shing", url="https://youtu.be/u9dBGWVwMMA?si=5jeyJwqxc5CsMLqh")],
                [InlineKeyboardButton("Web App Vulnerabilities", url="https://youtu.be/F5KJVuii0Yw?si=OpYrXgpLIGtaHWNZ")],
                [InlineKeyboardButton("Cryptography n Network Sec.", url="https://youtube.com/playlist?list=PLBlnK6fEyqRgJU3EsOYDTW7m6SUmW6kII&si=U6I5EeAG1UiM8Hqx")],
                [InlineKeyboardButton("Other Things", callback_data="otherhacking")],
                [InlineKeyboardButton("Back", callback_data="back_main")]
            ]
        )
        await callback_query.message.edit_text("Learn Python First:", reply_markup=keyboard)
    elif data =="otherhacking":
        await callback_query.answer("Learn Other TOOLS for hacking which is not in course \n\n Other Advanced Topics like:\nReverse Engg.,APTs,Zero-Day Exploits,Red Teaming",show_alert=True)

    elif data == "back_main":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Web Development", callback_data="web_dev")],
                [InlineKeyboardButton("Machine Learning", callback_data="ml")],
                [InlineKeyboardButton("Ethical Hacking", callback_data="hacking")],
                [InlineKeyboardButton("Cyber Security", callback_data="cyber_security")],
                [InlineKeyboardButton("App Development", callback_data="app_dev")],
                [InlineKeyboardButton("Game Development", callback_data="game_dev")],
                [InlineKeyboardButton("Dev Ops", callback_data="dev_ops")],
                [InlineKeyboardButton("Data Science", callback_data="data_science")],
                [InlineKeyboardButton("Cloud Computing", callback_data="cloud_computing")],
                [InlineKeyboardButton("AR & VR", callback_data="ar_vr")],
                [InlineKeyboardButton("Quantum Computing", callback_data="quantum_computing")],
            ]
        )
        await callback_query.message.edit_text("Choose a specialization:", reply_markup=keyboard)
    else:
         
        await callback_query.answer("WORK IN PROGRESS⚒️",show_alert=True)
        

if __name__ == "__main__":
    app.run()
