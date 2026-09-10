pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Stage 1: Checking out Student Result project...'

                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Stage 2: Running Student Result program...'

                bat 'py result.py 75 62 45'
            }
        }
    }
}