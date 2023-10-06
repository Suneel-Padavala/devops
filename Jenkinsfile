pipeline {
  agent any
  tools { 
        maven 'Maven_3_5_2'  
    }
   stages{
    stage('Build') { 
            steps { 
               withDockerRegistry([credentialsId: "dockerlogin", url: ""]) {
                 script{
                 app =  docker.build("asg")
                 }
            }
        }
    }

	stage('Push') {
            steps {
                script{
                    docker.withRegistry('https://145988340565.dkr.ecr.us-west-2.amazonaws.com', 'ecr:us-west-2:aws-credentials') {
                    app.push("latest")
                }
            }
        }
    }
	
    stages {
        stage('Create EKS Cluster') {
            steps {
                sh 'eks-cluster.sh'
            }
        }
    }
   
	stage('Deployment of Hello World Falsk Application') {
	   steps {
			withKubeConfig([credentialsId: 'kubelogin']) {
			sh('kubectl delete all --all -n devsecops')
			sh ('kubectl apply -f Helloworld-deployment.yaml --namespace=devsecops')
		    }
	    }
   	}
	   
	stage ('wait_for_testing'){
	   steps {
		   sh 'pwd; sleep 180; echo "Application Has been deployed on K8S"'
	   }
	}
  }
}
