from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

client = openai.OpenAI(api_key="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")  # ← تأكد إن المفتاح مظبوط هنا

@app.route('/ask_ai', methods=['POST'])
def ask_ai():
    try:
        data = request.get_json(force=True)
        question = data.get("question", "")
        if not question:
            return jsonify({"error": "No question provided"}), 400
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "أنت مساعد ذكي لمساعدة مستخدمي أودو."},
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message.content
        return jsonify({"answer": answer})
    except Exception as e:
        print(f"❗ Error Occurred: {e}")  # <<< هنا نطبع الخطأ في اللوج
        return jsonify({"error": str(e)}), 500
