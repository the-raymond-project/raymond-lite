from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def meditation_instructions():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        ).get("choices")[0].text
        return response
    result = request.args.get("result")
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()
