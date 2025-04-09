pipeline {
    agent any

    options {
        skipDefaultCheckout true
    }

    stages {
        stage('Prepare') {
            steps {
                cleanWs()
                git branch: 'develop', url: 'https://github.com/SergeyLion/Sprint_9.git'
            }
        }

        stage('Test') {
            steps {
                script {
                    withEnv(["PATH+EXTRA=/usr/local/bin:/opt/chrome"]) {
                        sh '''
                            python3 -m venv venv
                            . venv/bin/activate
                            pip install -r requirements.txt
                            pytest tests/ -n auto
                        '''
                    }
                }
            }
        }

    }
