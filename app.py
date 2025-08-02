from flask import Flask, request, jsonify
from flask_cors import CORS  # تأكد من استيراد CORS

app = Flask(__name__)
CORS(app)  # تمكين CORS لجميع المسارات

@app.route('/جمع')
def جمع_الأرقام():
    # استقبال الرقمين من الطلب
    رقم1 = request.args.get('رقم1')
    رقم2 = request.args.get('رقم2')
    
    # التحقق من وجود القيم
    if not رقم1 or not رقم2:
        return jsonify({"خطأ": "يجب إرسال رقمين في الطلب"}), 400
    
    # التحقق من أن القيم رقمية
    try:
        رقم1 = float(رقم1)
        رقم2 = float(رقم2)
    except ValueError:
        return jsonify({"خطأ": "يجب أن تكون القيم أرقاماً"}), 400
    
    # حساب النتيجة وإرجاعها
    الناتج = رقم1 + رقم2
    return jsonify({"النتيجة": الناتج})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
