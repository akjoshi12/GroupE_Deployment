pipeline {
    agent any

    environment {
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
                    // Use environment variable properly with shell script
                    sh '''
                        IMAGE_TAG=${BUILD_ID}
                        /usr/local/bin/docker build -t streamlit-devops-app:$IMAGE_TAG .
                    '''
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
