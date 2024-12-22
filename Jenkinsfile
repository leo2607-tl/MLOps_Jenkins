pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/leo2607-tl/MLOps_Jenkins.git'
            }
        }
        stage('Setup Environment') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Application') {
            steps {
                sh './venv/bin/uvicorn main:app --host 0.0.0.0 --port 8080 --reload &'
            }
        }
        stage('Run Tests') {
            steps {
                sh './venv/bin/pytest tests/'
            }
        }
    }
    post {
        always {
            echo 'Pipeline complete'
        }
    }
}
