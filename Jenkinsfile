pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '--shm-size=2g -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        stage('Setup') {
            steps {
                sh 'python --version'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/ --alluredir=allure-results'
            }
        }
        stage('Generate Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}