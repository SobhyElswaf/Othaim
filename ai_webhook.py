from flask import Flask, request, jsonify
from openai import OpenAI  # ✨ خد بالك من استيراد OpenAI الجديد

app = Flask(__name__)

client = OpenAI(api_key="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")

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
        print(f"❗ Error Occurred: {e}")
        return jsonify({"error": str(e)}), 500
