const quizDB = [{
    question: "Q1: who is the founder of Google?",
    a: "larry page",
    b: "sundar pichai",
    c: "tom cruise",
    d: " steve jobs",


    ans:"ans1"
}, {
    question: "Q2: who is the founder of ZEROinfinty?",
    a: "larry page",
    b: "Nishant Sharma",
    c: "tom cruise",
    d: " Elon musk",

    ans:"ans2"
}, { 
    question: "Q3: Fastest thing in the world?",
    a: "Flash",
    b: "light",
    c: "Krish",
    d: "human brain ",

    ans:"ans2"
}, {
    question: "Q4: Speed of light?",
    a: "299792458m/s",
    b: "3x10^8m/s",
    c: "50km/hr",
    d: "no one knows",
    

    ans:"ans1"
}
]


const question =document.querySelector(".question");
const option1 =document.querySelector("#option1");
const option2 =document.querySelector("#option2");
const option3 =document.querySelector("#option3");
const option4 =document.querySelector("#option4");
const sumbit =document.querySelector("#sumbit");
const answers = document.querySelectorAll(".answer");
let questionCount =0;

const loadQuestion =()=>{
  var range=quizDB[questionCount];
    question.innerHTML = range.question;
    option1.innerHTML=range.a;
    option2.innerHTML=range.b;
    option3.innerHTML=range.c;
    option4.innerHTML=range.d;
    
}

let showScore =document.querySelector('#showScore');


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

const deselAll =()=>{
    answers.forEach((ele)=>{ele.checked=false;})
}

let score=0;

sumbit.addEventListener('click',()=>{
    const checkedAnswer =getCheckAnswer();
    console.log(getCheckAnswer());
    if(checkedAnswer==quizDB[questionCount].ans){
        score++;
    };
    deselAll();
    questionCount++;
    if(questionCount<quizDB.length){
        loadQuestion();
        
    }else{
      showScore.innerHTML=`
      <h3>You Sored ${score}/${quizDB.length}😙</h3>
      <button class = "btn" onclick ="location.reload()">PLAY AGAIN</button>`;
      showScore.classList.remove('scoreArea');
    }
})






const nextQuestion =()=>{

    questionCount++;
 if(questionCount>3){
     questionCount=0;
 }


loadQuestion();
}

const prevQuestion =()=>{
    questionCount--; 
    if(questionCount<0){
        questionCount=3;
    }
   
    loadQuestion();
}

console.log("hello")