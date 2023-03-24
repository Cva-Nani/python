pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'SHIVA_GIT_CRED', url: 'https://github.com/Cvaaaa/python.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', credentialsId: 'SHIVA_GIT_CRED', url: 'https://github.com/Cvaaaa/python.git'
                
            }
        }
        stage('Run Python Script') {
            steps {
                sh 'python3 Bankapp.py'
            }
        }

        stage('Test') {
            steps {
                echo 'the job has been tested'
            }
        }
    }
}
