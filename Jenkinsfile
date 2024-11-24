pipeline {
    agent any
     parameters {
            choice(name: 'ENV', choices: ['development', 'staging', 'production'], description: 'Select the environment for the application')
            string(name: 'port', defaultValue: '5000:5000', description: 'enter port number')
        }
    stages {
    stage('Initialize') {
        steps {
            script {
                def dockerHome = tool 'mydocker'
                env.PATH = "${dockerHome}/bin:${env.PATH}"
            }
        }
    }

        stage('build') {
            steps {
                sh 'docker build -t myflask .'
            }
        }
        stage('deploy') {
            steps {
        sh "docker run -p ${params.port} --name myflask-${params.ENV} -d myflask"
            }
        }
//          stage('test') {
//             steps {
//                 sh 'mvn --version'
//             }
//         }

    }
}