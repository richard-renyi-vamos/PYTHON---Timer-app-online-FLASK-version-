from flask import Flask, render_template_string, request
import time

app = Flask(__name__)

HTML = '''
<!doctype html>
<title>Python Timer</title>
<h2>⏰ Timer</h2>
<form method="post">
    Time in seconds: <input type="text" name="seconds">
    <input type="submit" value="Start">
</form>
{% if remaining %}
    <h3>Time started for {{ remaining }} seconds!</h3>
    <script>
        let timeLeft = {{ remaining }};
        const timer = setInterval(() => {
            document.body.innerHTML = '<h2>⏰ Time left: ' + timeLeft + ' sec</h2>';
            timeLeft--;
            if (timeLeft < 0) {
                clearInterval(timer);
                document.body.innerHTML = '<h2>⏱️ Time\'s up!</h2>';
            }
        }, 1000);
    </script>
{% endif %}
'''

@app.route('/', methods=["GET", "POST"])
def timer():
    remaining = None
    if request.method == "POST":
        try:
            remaining = int(request.form["seconds"])
        except:
            remaining = 0
    return render_template_string(HTML, remaining=remaining)

if __name__ == "__main__":
    app.run(debug=True)
