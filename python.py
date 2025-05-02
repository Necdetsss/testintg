import requests

user_token = "MTI5Mzk2MTA0MTgzMDYwODk1OQ.GstVUN.UNc6ic_lK_mAKi7oXBbidjeReqidHqd6wBJpyY"
target_user_id = "816337817805389834"
message = "Selam, bu bir test mesajıdır."

# Mesaj göndermek için önce kanal oluşturulmalı (DM kanalı)
headers = {
    "Authorization": user_token,
    "Content-Type": "application/json"
}

# 1. DM Kanalı oluştur
r = requests.post(
    "https://discord.com/api/v9/users/@me/channels",
    headers=headers,
    json={"recipient_id": target_user_id}
)

if r.status_code == 200:
    dm_channel = r.json()["id"]

    # 2. DM Mesajı gönder
    r2 = requests.post(
        f"https://discord.com/api/v9/channels/{dm_channel}/messages",
        headers=headers,
        json={"content": message}
    )

    if r2.status_code == 200:
        print("Mesaj gönderildi.")
    else:
        print("Mesaj gönderilemedi:", r2.text)
else:
    print("DM kanalı oluşturulamadı:", r.text)
