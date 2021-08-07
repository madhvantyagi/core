
let questionCount =0;
const question =document.querySelector(".question");
const option1 =document.querySelector("#option1");
const option2 =document.querySelector("#option2");
const option3 =document.querySelector("#option3");
const option4 =document.querySelector("#option4");
const sumbit =document.querySelector("#sumbit");
const answers = document.querySelectorAll(".answer");

fetch('static/json/fate.json').then(function(response){
    return response.json();


}).then((quizDB)=>{console.log(quizDB)
   console.log(quizDB.length); 
    


    console.log(quizDB[questionCount]);

    const loadQuestion =()=>{
      var range=quizDB[questionCount];
        question.innerHTML = range.question;
        option1.innerHTML=range.option_1;
        option2.innerHTML=range.option_2;
        option3.innerHTML=range.option_3;
        option4.innerHTML=range.option_4;
        
    }

    loadQuestion();

     
const getCheckAnswer =()=>{
    var answer;
    answers.forEach((currentAnsElem)=>{
        if(currentAnsElem.checked){
            answer=currentAnsElem.id;
        }
    })
    return answer;
}




       let score= 0;

   

    const deselAll =()=>{
        answers.forEach((ele)=>{ele.checked=false;})
    }

    sumbit.addEventListener('click',()=>{
        const checkedAnswer =getCheckAnswer();
        console.log(getCheckAnswer());
        if(checkedAnswer===quizDB[questionCount].answer){
            score++;
        };
        deselAll();
        questionCount++;
        console.log(questionCount);
        if(questionCount<quizDB.length){
            loadQuestion();
            
        }else{
          showScore.innerHTML=`
          <h3>You Sored ${score}/${quizDB.length}😙</h3>
          <button class = "btn" onclick ="location.reload()">PLAY AGAIN</button>`;
          showScore.classList.remove('scoreArea');
        }
    });

 
console.log(questionCount);

console.log("hello world");

}).catch(function(error){
    console.error('something wrong');
    console.error(error);
    });





// let showScore =document.querySelector('#showScore');

const getCheckAnswer =()=>{
    var answer;
    answers.forEach((currentAnsElem)=>{
        if(currentAnsElem.checked){
            answer=currentAnsElem.id;
        }
    })
    return answer;
}

const deselAll =()=>{
    answers.forEach((ele)=>{ele.checked=false;})
}



// let score=0;
// sumbit.addEventListener('click',()=>{
//     const checkedAnswer =getCheckAnswer();
//     console.log(getCheckAnswer());
//     if(checkedAnswer==quizDB[questionCount].answer){
//         score++;
//     };
//     deselAll();
//     questionCount++;
//     if(questionCount<quizDB.length){
//         loadQuestion();   
//     }else{
//       showScore.innerHTML=`
//       <h3>You Sored ${score}/${quizDB.length}😙</h3>
//       <button class = "btn" onclick ="location.reload()">PLAY AGAIN</button>`;
//       showScore.classList.remove('scoreArea');
//     }
// })
// const nextQuestion =()=>{
//     questionCount++;
//  deselAll();
// loadQuestion();
// }
// const prevQuestion =()=>{
//     questionCount--; 
//     if(questionCount<=1){
//      questionCount= quizDB.lenght                                                  
//   }       
//     loadQuestion();
// }






























