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
                sh 'python api_check.py'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python test_main.py'
            }
        }
    }
    post {
        always {
            echo 'Pipeline complete'
        }
    }
}
