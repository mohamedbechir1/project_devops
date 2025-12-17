pipeline {
    agent any

    environment {
        DOCKER_REGISTRY   = "docker.io"
        BACKEND_IMAGE     = "docker.io/mohamedbechir1/backend:latest"
        FRONTEND_IMAGE    = "docker.io/mohamedbechir1/frontend:latest"
        AI_SERVICE_IMAGE  = "docker.io/mohamedbechir1/ai-service:latest"
        VM_APP_IP         = "192.168.56.11"
        SSH_KEY           = "~/.ssh/id_jenkins_vm"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/mohamedbechir1/project_devops'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                    docker build -t ${BACKEND_IMAGE} ./backend
                    docker build -t ${FRONTEND_IMAGE} ./frontend
                    docker build -t ${AI_SERVICE_IMAGE} ./ai-service
                '''
            }
        }

        stage('Push Docker Images') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${BACKEND_IMAGE}
                        docker push ${FRONTEND_IMAGE}
                        docker push ${AI_SERVICE_IMAGE}
                    '''
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh '''
                    scp -i ${SSH_KEY} -o StrictHostKeyChecking=no ./deploy/docker-compose.yml vagrant@${VM_APP_IP}:/home/vagrant/
                    ssh -i ${SSH_KEY} -o StrictHostKeyChecking=no vagrant@${VM_APP_IP} "docker-compose down && docker-compose up -d"
                '''
            }
        }

        stage('Configure with Ansible') {
            steps {
                ansiblePlaybook(
                    playbook: 'infra/ansible/playbooks/site.yml',
                    inventory: 'infra/ansible/inventory.ini'
                )
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}