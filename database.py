import sqlite3
import aiosqlite
from constants.constants import USER_TABLE_NAME


def create_user_table():
    con = sqlite3.connect('animangabot.db')
    cursor = con.cursor()

    cursor.execute(
        f"""CREATE TABLE IF NOT EXISTS {USER_TABLE_NAME}(
            telegram_id Integer NOT NULL Primary Key ,
            full_name TEXT NOT NULL
        )"""
    )

    con.commit()
    cursor.close()
    con.close()


def add_user(telegram_id, full_name):
    con = sqlite3.connect('animangabot.db')
    cursor = con.cursor()

    cursor.execute(
        f"""insert into {USER_TABLE_NAME}(telegram_id, full_name) values ('{telegram_id}', '{full_name}');""",
    )

    con.commit()
    cursor.close()
    con.close()


async def check_user(telegram_id):
    async with aiosqlite.connect('animangabot.db') as con:
        cursor = await con.execute(
            f"SELECT telegram_id FROM {USER_TABLE_NAME} WHERE telegram_id = '{telegram_id}'",
        )
        result = await cursor.fetchall()
        await con.commit()
        await cursor.close()
        await con.close()

    if not result:
        return False
    else:
        return result[0].__contains__(telegram_id)


async def unregister_user(telegram_id):
    async with aiosqlite.connect('animangabot.db') as con:
        cursor = await con.execute(
            f"""delete from {USER_TABLE_NAME} where telegram_id = '{telegram_id}'""",
        )
        await con.commit()
        await cursor.close()
        await con.close()
