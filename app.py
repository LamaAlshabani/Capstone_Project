
from flask import Flask,render_template,request
# from speech_Verification import Speaker_Recognition


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/SpeakerVerification',methods=['GET','POST'])
def SpeakerVerification():
#  if request.method == 'POST': 
#         file2 = request.form['file2']
#         file1 =    request.form['file1']
      
        # result = Speaker_Recognition(file1 , file2)

        
    return render_template('SpeakerVerification.html')



@app.route('/SpeakerEmotion',methods=['GET','POST'])
def SpeakerEmotion():
#  if request.method == 'POST': 
#         file2 = request.form['file2']
#         file1 =    request.form['file1']
      
        # result = Speaker_Recognition(file1 , file2)

    return render_template('SpeakerEmotion.html')


@app.route('/SpeechEnhancment',methods=['GET','POST'])
def SpeechEnhancment():
#  if request.method == 'POST': 
#         file2 = request.form['file2']
#         file1 =    request.form['file1']
      
        # result = Speaker_Recognition(file1 , file2)

    return render_template('SpeechEnhancment.html')

if __name__ == '__main__':
	app.run(debug=True)
