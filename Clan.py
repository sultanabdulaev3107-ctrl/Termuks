import requests
import json
import threading

# --- CONFIG ---
FIREBASE_API_KEY = 'AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM'
FIREBASE_LOGIN_URL = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={FIREBASE_API_KEY}"
RANK_URL = "https://us-central1-cp-multiplayer.cloudfunctions.net/SetUserRating4"

# --- ACCOUNTS (добавляй сколько хочешь) ---
ACCOUNTS = [
    {"email": "sultanabdulaev2006@gmail.com", "password": "31072006"},
    {"email": "den_isaev_95@mail.ru", "password": "Zaebali1995"},
    {"email": "kingcpmcpm1@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm2@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm3@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm4@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm5@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm6@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm7@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm88@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm9@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm10@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm11@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm12@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm13@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm14@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm15@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm16@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm17@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm188@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm19@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm20@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm21@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm22@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm23@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm24@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm25@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm26@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm27@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm28@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm29@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm30@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm31@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm32@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm33@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm34@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm35@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm36@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm37@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm388@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm39@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm40@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm41@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm42@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm43@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm44@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm45@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm46@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm47@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm48@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm49@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm50@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm51@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm52@gmail.com", "password": "666666"},
]


def login(email, password):
    payload = {
        "clientType": "CLIENT_TYPE_ANDROID",
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 12)",
        "Content-Type": "application/json"
    }

    try:
        r = requests.post(FIREBASE_LOGIN_URL, headers=headers, json=payload)
        data = r.json()

        if r.status_code == 200 and "idToken" in data:
            return data["idToken"]
    except:
        pass

    return None


def set_rank(token):
    rating_data = {k: 100000 for k in [
        "cars", "car_fix", "car_collided", "car_exchange", "car_trade", "car_wash",
        "slicer_cut", "drift_max", "drift", "cargo", "delivery", "taxi", "levels",
        "gifts", "fuel", "offroad", "speed_banner", "reactions", "police", "run",
        "real_estate", "t_distance", "treasure", "block_post", "push_ups",
        "burnt_tire", "passanger_distance"
    ]}

    rating_data["time"] = 10000000000
    rating_data["race_win"] = 3000

    payload = {
        "data": json.dumps({"RatingData": rating_data})
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "okhttp/3.12.13"
    }

    try:
        r = requests.post(RANK_URL, headers=headers, json=payload)
        return r.status_code == 200
    except:
        return False


def process_account(acc):
    email = acc["email"]
    password = acc["password"]

    token = login(email, password)

    if not token:
        print(f"❌ {email}")
        return

    success = set_rank(token)

    if success:
        print(f"✅ {email}")
    else:
        print(f"❌ {email}")


def main():
    print("\n=== KING RANK MULTI THREAD BOT ===\n")

    threads = []

    for acc in ACCOUNTS:
        t = threading.Thread(target=process_account, args=(acc,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nDONE.")


if __name__ == "__main__":
    main()
