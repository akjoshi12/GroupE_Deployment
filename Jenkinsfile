pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin"  // Adjust this path based on where ansible is installed
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
                    sh '''
                        IMAGE_TAG=${BUILD_ID}
                        /usr/local/bin/docker build -t streamlit-devops-app:$IMAGE_TAG .
                    '''
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                script {
                    sh '''
                        ansible-playbook deploy.yml -i hosts --private-key /Users/atrijoshi/.jenkins/workspace/Streamlit-Sentiment-Analysis/ssh18358635923941210495.key -u atrijoshi -e "image_tag=${BUILD_ID}"
                    '''
                }
            }
        }
    }
}
