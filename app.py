import os
from flask import Flask, render_template, request, send_from_directory
from flask_uploads import UploadSet, configure_uploads, DATA
from werkzeug.utils import secure_filename
from analyse.offre_analyse import extract_skills_and_qualifications
from analyse.cv_analyse import extract_skills_and_experience
from analyse.comparaison import compare_skills_and_experience
from analyse.questions_generation import generate_interview_questions, generate_interview_questions_pdf  # Ajout de l'import

if not os.path.exists('uploads'):
    os.makedirs('uploads')
app = Flask(__name__)


# Configuration for file uploads
app.config['UPLOADED_CV_DEST'] = 'cv'
app.config['UPLOADED_OFFRE_DEST'] = 'offres'
app.config['UPLOADS_DEFAULT_DEST'] = 'uploads'

cv_uploads = UploadSet('cv', DATA)
configure_uploads(app, cv_uploads)

offre_uploads = UploadSet('offre', DATA)
configure_uploads(app, offre_uploads)

ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Main route
@app.route('/')
def home():
    return 'Bienvenue sur votre application Interview Simulator !'

# Route to upload the CV and offer
@app.route('/upload', methods=['POST'])
def upload():
    if 'cv' in request.files and 'offre' in request.files:
        cv = request.files['cv']
        offre = request.files['offre']

        # Verify if it's a CV and save to the "cv" directory
        cv_path = os.path.join(app.config['UPLOADED_CV_DEST'], secure_filename(cv.filename))
        if allowed_file(cv.filename):
            cv.save(cv_path)
        else:
            return "Please upload a valid CV file."

        # Save the offre to the "offres" directory
        offre_path = os.path.join(app.config['UPLOADED_OFFRE_DEST'], secure_filename(offre.filename))
        offre.save(offre_path)

        # Process the CV and offer
        cv_data = extract_skills_and_experience(cv_path)
        offre_data = extract_skills_and_qualifications(offre_path)
        comparison_score = compare_skills_and_experience(offre_data, cv_data)

        # Generate interview questions based on the comparison
        questions = generate_interview_questions(offre_data, cv_data)
        questions_pdf_path = 'uploads/questions.pdf'
        generate_interview_questions_pdf(questions, questions_pdf_path)

        return send_from_directory('uploads', 'questions.pdf', as_attachment=True)

    return "Please select both the CV and offre."

if __name__ == '__main__':
    app.run(debug=True)
