import requests
import json
import threading

# --- CONFIG ---
FIREBASE_API_KEY = 'AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM'
FIREBASE_LOGIN_URL = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={FIREBASE_API_KEY}"
RANK_URL = "https://us-central1-cp-multiplayer.cloudfunctions.net/SetUserRating4"

# --- ACCOUNTS (добавляй сколько хочешь) ---
ACCOUNTS = [
    {"email": "sultanabdulaev206@gmail.com", "password": "31072006"},
    {"email": "sultanabdulaev2006@gmail.com", "password": "31072006"},
    {"email": "acc4@gmail.com", "password": "pass4"},
    {"email": "acc5@gmail.com", "password": "pass5"},
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
