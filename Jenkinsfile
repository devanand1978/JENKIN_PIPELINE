pipeline {
    agent none
    stages {
        stage('Build') {
            agent{
                docker{
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python -n py_compile calc_module.py'
                stash(name:'compiled_results',includes:'*.py')
            }
        }
    }
}