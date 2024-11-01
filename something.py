import requests
import time
from random import randint
from fake_useragent import UserAgent

while True:

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': 'tempCookie=true',
        'Host': 'www.tikvues.com',
        'Origin': 'https://www.tikvues.com',
        'Referer': 'https://www.tikvues.com/views/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': UserAgent().chrome
    }
    video_link = "https://www.tiktok.com/@n1kymetaa/video/7430992303038172446?is_from_webapp=1&sender_device=pc&web_id=7404519648287114782"

    video_id = video_link.split('/')[-1]
    # 
    data = {"link": video_link + f'?is_from_webapp=1&sender_device=pc&web_id={randint(1000000, 9999999)}'}
    response = requests.post('https://www.tikvues.com/api/views', headers=headers, json=data)
    res = requests.get(f'https://tiktok.livecounts.io/video/stats/{video_id}', headers={"origin": "https://tokcounter.com", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}).json()
    print(response.json(), res['viewCount'])
    time.sleep(60)
