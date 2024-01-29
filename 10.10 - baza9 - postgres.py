import asyncio
import asyncpg

async def run():
    conn = await asyncpg.connect(user ='****_dane' , password='****',
                                 database='37970432_dane', host='serwer2348480.home.pl',)
    await conn.fetch('''CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY , name TEXT);''')
    await  conn.execute('''
    INSERT INTO users(name) VALUES($1);
    ''','JohnPau')
    await  conn.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
