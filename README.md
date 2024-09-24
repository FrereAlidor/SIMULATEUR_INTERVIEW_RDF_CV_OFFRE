
# Interview Simulator

## Description

**Interview Simulator** is a project designed to help users prepare for job interviews by simulating 
interviews with standardized questions. The goal is to provide automatic evaluation of responses to
help users improve their interview performance.

## Project Structure

- **analyse/**: Contains Python scripts for analyzing resumes (CVs) and job offers.
  - `comparaison.py`: Script for comparing resumes with job offers.
  - `cv_analyse.py`: Analyzes resumes to identify strengths and weaknesses.
  - `offre_analyse.py`: Analyzes job offers to extract required skills.
  - `questions_generation.py`: Automatically generates interview questions based on the analysis of job offers and resumes.
  
- **cv/**: Folder containing resumes for various positions and fields.

- **offres/**: Folder containing job offers to analyze job requirements.

- **uploads/**: Folder for storing files uploaded by users.

- **.gitignore**: File to exclude certain files from Git tracking, such as auto-generated or temporary files.

- **app.py**: Main entry point for running the application.

- **main.py**: Primary script orchestrating the application.

- **requirements.txt**: List of Python dependencies needed to run the project.

## Features

- **Resume Analysis**: Identifies skills present in resumes and compares them with job offer requirements.
- **Job Offer Analysis**: Extracts job requirements and skills to generate relevant interview questions.
- **Question Generation**: Based on the analyses, customized interview questions are generated to help users prepare.
- **Automatic Evaluation**: Interview responses are automatically evaluated to provide personalized feedback.

## Prerequisites

Before running this project, make sure you have installed:

- Python 3.x
- The libraries listed in `requirements.txt`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/FrereAlidor/SIMULATEUR_INTERVIEW_RDF_CV_OFFRE.git
   ```

2. Navigate to the project directory:

   ```bash
   cd SIMULATEUR_INTERVIEW_RDF_CV_OFFRE
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

## Usage

1. Launch the application and upload a resume or job offer.
2. The application will analyze the file and generate interview questions.
3. Answer the questions and receive automatic evaluation for each response.

## Contributing

Contributions are welcome! If you have suggestions for improvements or fixes, feel free to open an issue or submit a pull request.

## Authors

- **Mbayandjambe Alidor** - mbayandjambealidor@gmail.com

