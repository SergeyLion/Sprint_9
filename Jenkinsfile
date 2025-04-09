pipeline {
    agent any

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
                script {
                    allure([
                        commandline: 'allure-2.27.0',
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        report: 'allure-report',
                        results: [[path: 'allure-results']]
                    ])
                }
            }
        }
    }

    post {
        always {
            cleanWs()
            script {
                allure([
                    commandline: 'allure-2.27.0',
                    report: 'allure-report',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}