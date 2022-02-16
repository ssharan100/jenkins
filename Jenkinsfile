pipeline {
    agent any

    stages {
        stage('Clone git') {
            steps {
                git 'https://github.com/ssharan100/jenkins.git'
            }
        }
        stage('Build code') {
            steps {
                sh "chmod u+x Prog1.py"
                sh "./Prog1.py"
            }
        }
        stage('Test code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    }
}
