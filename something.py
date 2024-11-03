import requests
import time
from random import randint, choice
from fake_useragent import UserAgent

# Initialize the UserAgent generator
ua = UserAgent()

# Loop to continuously send requests
while True:
    # Generate a random User-Agent
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
        'User-Agent': ua.random  # Generate a random User-Agent for each iteration
    }
    
    video_link = "https://www.tiktok.com/@n1kymetaa/video/7425816353287769386?is_from_webapp=1&sender_device=pc&web_id=7404519648287114782"
    video_id = video_link.split('/')[-1]
    
    data = {
        "link": video_link + f'?is_from_webapp=1&sender_device=pc&web_id={randint(1000000, 9999999)}'
    }
    
    # Send POST request to simulate a view
    response = requests.post('https://www.tikvues.com/api/views', headers=headers, json=data)
    
    # Fetch current view count
    res = requests.get(
        f'https://tiktok.livecounts.io/video/stats/{video_id}', 
        headers={
            "origin": "https://tokcounter.com",
            "user-agent": ua.random  # Generate a random User-Agent for each view count request
        }
    ).json()
    
    # Print the response and view count
    print(response.json(), res['viewCount'])
    
    # Pause before the next request
    time.sleep(2)
