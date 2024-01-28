let boxes = document.querySelectorAll(".box");
let playagain = document.querySelector("#playagain");
let turn0 = true;
let newgame = document.querySelector("#newGame")


let winPattern = [
    [0,1,2],
    [0,4,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [2,4,6],
    [3,4,5],
    [6,7,8],
];

let count = 0;
boxes.forEach((box) => {
    box.addEventListener("click", () => {
        console.log("Button clicked");
        if (turn0) {
            box.innerText = "O";
            turn0 = false;
        } else {
            box.innerText = "X";
            turn0 = true;
        }
        
        box.disabled = true;
        count++;
        checkWinner();
        tieGame();
        
    });
    
});

const tieGame=()=>{
    if(count===9){
            
        document.querySelector(".msg").innerText =` GAME TIED `;
        document.querySelector(".message").classList.remove("hide");
        BtnDisable();
    

}
}
playagain.addEventListener("click",()=>{
    boxes.forEach((box)=>{
        box.innerText="";
    });
    
    document.querySelector(".message").classList.add("hide");
    BtnEnable();
    count=0;

});

const BtnDisable =()=>{
    for(let box of boxes){
        box.disabled = true;
    }
}
const BtnEnable =()=>{
    for(let box of boxes){
        box.disabled = false;
    }
}


const checkWinner=()=>{
    for(let pattern of winPattern){
        let pos0 = boxes[pattern[0]].innerText;
        let pos1 = boxes[pattern[1]].innerText;
        let pos2 = boxes[pattern[2]].innerText;
        if(pos0!="" && pos1!="" && pos2!=""){
            if(pos0 === pos1 && pos1 === pos2){
                document.querySelector(".msg").innerText =` CONGRATULATIONS , Winner  is  ${pos0} `;
                document.querySelector(".message").classList.remove("hide");
                BtnDisable();
                count=0;
            }
        }
    }
    

}

newgame.addEventListener("click",()=>{
    boxes.forEach((box)=>{
        box.innerText="";
    });
    
    document.querySelector(".message").classList.add("hide");
    BtnEnable();
    count=0;

});
