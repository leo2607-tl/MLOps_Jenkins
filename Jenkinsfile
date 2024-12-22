pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/leo2607-tl/MLOps_Jenkins.git'
            }
        }
        stage('Run Application') {
            steps {
                sh 'uvicorn main:app --host 0.0.0.0 --port 8080 --reload &'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
    post {
        always {
            echo 'Pipeline complete'
        }
    }
}
