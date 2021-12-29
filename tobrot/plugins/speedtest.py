from speedtest import Speedtest
import logging
from tobrot.helper_funcs.display_progress import humanbytes

torlog = logging.getLogger(__name__)

async def get_speed(self, message):
    imspd = await message.reply("`Running Speed Test...`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    path = (result['share'])
    string_speed = f'''
<code>📡 Sᴇʀᴠᴇʀ :</code>
╠ <b>🗳️ Nᴀᴍᴇ:</b> <code>{result['server']['name']}</code>
╠ <b>🌍 Cᴏᴜɴᴛʀʏ:</b> <code>{result['server']['country']}, {result['server']['cc']}</code>
╠ <b>🩸 Sᴘᴏɴsᴏʀ:</b> <code>{result['server']['sponsor']}</code>
╚ <b>⚙️ ɪsᴘ:</b> <code>{result['client']['isp']}</code>

<code>📊 Sᴘᴇᴇᴅ Tᴇsᴛ Results :</code>
╠ <b>📈 Uᴘʟᴏᴀᴅ:</b> <code>{humanbytes(result['upload'] / 8)}</code>
╠ <b>📉 Dᴏᴡɴʟᴏᴀᴅ:</b>  <code>{humanbytes(result['download'] / 8)}</code>
╠ <b>📌 Pɪɴɢ:</b> <code>{result['ping']} ms</code>
╚ <b>💡 Isᴘ ʀᴀᴛɪɴɢ:</b> <code>{result['client']['isprating']}</code>
'''
    await imspd.delete()
    await message.reply(string_speed, parse_mode="HTML")
    torlog.info(f'Server Speed result:-\nDL: {humanbytes(result["download"] / 8)}/s UL: {humanbytes(result["upload"] / 8)}/s')

