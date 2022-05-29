properties([pipelineTriggers([pollSCM('* * * * *')])])
node { 
 stage("clone"){
 git "https://github.com/Maronny3090/Devops1004.git"
 }
stage ("show files"){
    sh "ls -l"
}

}
