pipeline {
    agent any

    environment {
        // Explicitly add /usr/local/bin to PATH for Docker
        PATH = "/usr/local/bin:/usr/bin:/bin"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/akjoshi12/GroupE_Deployment',
                        credentialsId: 'github-credentials'
                    ]]
                ])
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Use the full path for Docker explicitly
                    sh '/usr/local/bin/docker build -t streamlit-devops-app:${env.BUILD_ID} .'
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
