pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("streamlit-devops-app:${env.BUILD_ID}")
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                ansiblePlaybook(
                    playbook: 'deploy.yml',
                    inventory: 'hosts',
                    credentialsId: 'ansible-ssh-key',
                    extras: '-e "image_tag=${env.BUILD_ID}"'
                )
            }
        }
    }
}