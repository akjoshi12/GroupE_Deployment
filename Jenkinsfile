pipeline {
    agent any
    environment {
        VENV_PATH = "${WORKSPACE}/venv"
        DOCKER_HOST = "unix:///var/run/docker.sock"
        PATH = "/usr/local/bin:$PATH"
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
        stage('Verify Docker') {
            steps {
                script {
                    sh 'docker version'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh '''
                        IMAGE_TAG=${BUILD_ID}
                        docker build -t streamlit-devops-app:$IMAGE_TAG .
                    '''
                }
            }
        }
        stage('Set up Python Virtual Environment') {
            steps {
                script {
                    sh '''
                        if [ ! -d "${VENV_PATH}" ]; then
                            python3 -m venv ${VENV_PATH}
                        fi
                        source ${VENV_PATH}/bin/activate
                        pip install --upgrade pip
                        pip install docker requests ansible
                    '''
                }
            }
        }
        stage('Deploy with Ansible') {
            steps {
                script {
                    sh '''
                        source ${VENV_PATH}/bin/activate
                        ansible-playbook -vvv deploy.yml -i hosts -e "image_tag=${BUILD_ID}"
                    '''
                }
            }
        }
    }
}
