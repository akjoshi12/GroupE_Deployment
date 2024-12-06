pipeline {
    agent any
    environment {
        VENV_PATH = "${WORKSPACE}/venv"  // Define path to virtual environment in workspace
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
                    // Create virtual environment if it doesn't exist
                    sh '''
                        if [ ! -d "${VENV_PATH}" ]; then
                            python3 -m venv ${VENV_PATH}
                        fi
                        source ${VENV_PATH}/bin/activate
                        pip install --upgrade pip
                        pip install docker requests ansible  # Install ansible here
                    '''
                }
            }
        }
        stage('Deploy with Ansible') {
            steps {
                script {
                    // Use the virtual environment's Python interpreter for Ansible
                    sh '''
                        source ${VENV_PATH}/bin/activate
                        ansible-playbook deploy.yml -i hosts -e "image_tag=${BUILD_ID}"
                    '''
                }
            }
        }
    }
}
