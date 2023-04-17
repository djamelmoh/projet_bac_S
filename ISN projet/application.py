from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)
@app.route('/')
def accueil():return render_template('accueil.html')

tableau = [''] * 8

@app.route('/<page>', methods=['POST','GET'])
def page(page): 
	if request.method == 'POST' : 
		choix = request.form['choix']
		question = request.form['question']
		tableau[int(question)] = choix
		print (tableau)
			
	if page == 'qcm9.html' :
		score = calculerscore() 
		return render_template('qcm9.html', points=score)

	return render_template(page)
	
	
def calculerscore () : 
	score = 0
	for i in range(0,len(tableau)) : 
		if tableau[i] == réponse[i] :
			score += 1 
	return score
	
	
réponse = ['2','2','3','3','2','1','1','2']




if __name__ == "__main__":    app.run(host='localhost', port=3000, debug=True)