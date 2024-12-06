pipeline {
    agent any
    environment {
        VENV_PATH = "${WORKSPACE}/env"  // Use a relative path to the workspace
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
        stage('Set up Python Virtual Environment') {
            steps {
                script {
                    sh '''
                        # Create virtual environment if it doesn't exist
                        if [ ! -d "${VENV_PATH}" ]; then
                            python3 -m venv ${VENV_PATH}
                        fi
                        # Activate virtual environment and install packages
                        source ${VENV_PATH}/bin/activate
                        pip install --upgrade pip
                        pip install docker requests
                    '''
                }
            }
        }
        stage('Deploy with Ansible') {
            steps {
                script {
                    sh '''
                        # Activate virtual environment before running ansible playbook
                        source ${VENV_PATH}/bin/activate
                        ansible-playbook deploy.yml -i hosts -e "image_tag=${BUILD_ID}"
                    '''
                }
            }
        }
    }
}
