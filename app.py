import os, re
from flask import Flask, redirect, render_template, request, flash


# create and configure app
app = Flask(__name__)
app.config.from_mapping(SECRET_KEY="afvabrtkdfporgjae12541")
    

# simple wordle score calculator
@app.route("/", methods=["GET", "POST"])
def wordle_calc():
    if request.method == "POST":
        game = request.form.get("game")
        stats = request.form.get("stats")
        if not game:
            flash("ERROR - Please select game!", category="err")
            return render_template("wordle_calc.html")
        if game == "wordle":
            if not stats:
                flash("ERROR - Please choose enter stats!", category="err")
                return render_template("wordle_calc.html")
            try:
                x = re.search(r"^(STATISTICS\s([0-9][0-9]?[0-9]?)\sPlayed\s([0-9][0-9]?[0-9]?)\sWin\s%\s([0-9][0-9]?[0-9]?)\sCurrent\sStreak\s([0-9][0-9]?[0-9]?)\sMax\sStreak\sGUESS\sDISTRIBUTION\s1\s([0-9][0-9]?)\s2\s([0-9][0-9]?[0-9]?)\s3\s([0-9][0-9]?[0-9]?)\s4\s([0-9][0-9]?[0-9]?)\s5\s([0-9][0-9]?[0-9]?)\s6\s([0-9][0-9]?[0-9]?)\s)", stats)
                if x:
                    total_played = int(x.group(2))
                    ones = int(x.group(6))
                    twos = int(x.group(7))
                    threes = int(x.group(8))
                    fours = int(x.group(9))
                    fives = int(x.group(10))
                    sixes = int(x.group(11))
                    total_solved = ones + twos + threes + fours + fives +sixes

                    score = ((ones*1 + twos*2 + threes*3 + fours*4 + fives*5 + sixes*6)/total_solved)/(total_solved/total_played)
                    flash("Success!", category="success")
                    return render_template("wordle_calc.html", score=f"Your Wordle score is {score:.3f} 🥇")
                else:
                    flash("ERROR - Stats format not valid!", category="err")
                    return render_template("wordle_calc.html")
            except:
                flash("ERROR - Stats format not valid! Please check instructions.", category="err")
                return render_template("wordle_calc.html")
        elif game == "katapat":
            stats = request.form.get("stats")
            if not stats:
                flash("ERROR - Please enter stats!", category="err")
                return render_template("wordle_calc.html")
            try:
                x = re.search(r"^(STATISTIK\s\s?([0-9][0-9]?[0-9]?)\sMain\s([0-9][0-9]?[0-9]?)\s%\sMenang\s([0-9][0-9]?[0-9]?)\sKombo\sSemasa\s([0-9][0-9]?[0-9]?)\sKombo\sMaksima\sTABURAN\sTEKAAN\s\s?1\s([0-9][0-9]?)\s2\s([0-9][0-9]?[0-9]?)\s3\s([0-9][0-9]?[0-9]?)\s4\s([0-9][0-9]?[0-9]?)\s5\s([0-9][0-9]?[0-9]?)\s6\s([0-9][0-9]?[0-9]?))", stats)
                if x:
                    total_games = int(x.group(2))
                    ones = int(x.group(6))
                    twos = int(x.group(7))
                    threes = int(x.group(8))
                    fours = int(x.group(9))
                    fives = int(x.group(10))
                    sixes = int(x.group(11))
                    total_solved = ones + twos + threes + fours + fives + sixes

                    score = ((ones*1 + twos*2 + threes*3 + fours*4 + fives*5 + sixes*6)/total_solved)/(total_solved/total_games)
                    flash("Success!", category="success")
                    return render_template("wordle_calc.html", score=f"Your Katapat score is {score:.3f} 🥇")
                else:
                    flash("ERROR - Stats format not valid!", category="err")
                    return render_template("wordle_calc.html")
            except:
                flash("ERROR - Stats format not valid! Please check instructions.", category="err")
                return render_template("wordle_calc.html")
    else:
        return render_template("wordle_calc.html")


@app.route("/formula")
def formula():
    return render_template("formula.html")

@app.route("/instructions")
def instructions():
    return render_template("instructions.html")

@app.route("/links")
def links():
    return render_template("links.html")

if __name__=="__main__":
    app.debug = True
    app.run()
