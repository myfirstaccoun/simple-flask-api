from flask import Flask, request, jsonify
import threading
import asyncio
import aiohttp
import random
import os

try:
    os.system("cls")
except:
    os.system("clear")

# تشغيل سيرفر Flask
app = Flask(__name__)

@app.route('/')
def health_check():
    return "OK", 200

@app.route('/sum', methods=['GET'])
def sum_numbers():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = a + b
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def run_server():
    app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_server, daemon=True).start()

# ------------------- #
# دالة keep_alive اللي بتعمل ping لموقع خارجي
# ------------------- #
async def keep_alive():
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://google.com") as response:
                    print(f"✅ Ping Google: {response.status}")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        wait = random.randint(300, 600)
        print(f"⏳ Waiting {wait} seconds...")
        await asyncio.sleep(wait)

# ------------------- #
# Main async event loop
# ------------------- #
async def main():
    print("🚀 Flask API for adding numbers is running!")
    await keep_alive()

if __name__ == "__main__":
    asyncio.run(main())
