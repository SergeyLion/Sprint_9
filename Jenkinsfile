pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '--shm-size=2g'
        }
    }

    stages {
        stage('Setup') {
            steps {
                sh 'python --version'
                sh 'pip install --upgrade pip'
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
                script {
                    allure([
                        commandline: 'allure',
                        results: [[path: 'allure-results']],
                        report: 'allure-report'
                    ])
                }
            }
        }
    }

    post {
        always {
            deleteDir() // Альтернатива cleanWs
            script {
                allure([
                    commandline: 'allure',
                    results: [[path: 'allure-results']],
                    report: 'allure-report'
                ])
            }
        }
    }
}