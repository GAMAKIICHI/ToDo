"use strict";


/*
This class takes a radio button and updates its labels background.
Color1 updates the labels background if the radio button is toggled.
Colorw updates the labels background if the radio button is untoggled.
*/
class Dot{
    constructor(dot, color1, color2){
        this.dot = dot;
        this.color1 = color1;
        this.color2 = color2;
    }

    //returns the current background color
    getColor(){
        return getElementStyle(this.dot, "background-color");
    }

    isChecked(){
        if(!this.dot){
            return;
        }

        return this.dot.checked;
    }

    //toggles radio button and changes its background color to color1 with a 1px black border
    toggle(){

        if(!this.dot){
            return;
        }

        this.dot.checked = true;
        this.dot.labels[0].style.backgroundColor = this.color1;
        this.dot.labels[0].style.border = "1px solid black";
    }

    //untoggles radio button and changes its background color to color2 adn removes the border
    untoggle(){

        if(!this.dot){
            return;
        }

        this.dot.checked = false;
        this.dot.labels[0].style.backgroundColor = this.color2;
        this.dot.labels[0].style.border = "none";
    }
}

document.addEventListener("DOMContentLoaded", () =>{
    const dotToggleLow = document.querySelector("#low");
    const dotToggleMed = document.querySelector("#medium");
    const dotToggleHigh = document.querySelector("#high");

    const green = ["rgba(0, 255, 0)", "rgba(170, 248, 170)"];
    const yellow = ["rgba(255, 255, 0)", "rgba(240, 240, 80)"];
    const red = ["rgba(255, 0, 0)", "rgba(255, 100, 100)"];

    const low = new Dot(dotToggleLow, green[0], green[1]);
    const med = new Dot(dotToggleMed, yellow[0], yellow[1]);
    const high = new Dot(dotToggleHigh, red[0], red[1]);

    /*this is so color gets applied to dot*/
    low.untoggle();
    med.untoggle();
    high.untoggle();

    if(dotToggleLow)
        dotToggleLow.addEventListener("change", () =>{
            low.toggle();
            med.untoggle();
            high.untoggle();
            
        });
    
    if(dotToggleMed)
        dotToggleMed.addEventListener("change", () =>{
            low.untoggle();
            med.toggle();
            high.untoggle();
        });
    
    if(dotToggleHigh)
        dotToggleHigh.addEventListener("change", () =>{
            low.untoggle();
            med.untoggle();
            high.toggle();
        });

    /*Changes the color of the tasks urgency*/
    const taskDots = document.querySelectorAll("span.dot");

    for(let i = 0; i < taskDots.length; i++){
        const urgencyType = taskDots[i].className.slice(-1);

        /* Low Urgency */
        if(urgencyType === 'L'){
            taskDots[i].style.backgroundColor = green[1];
        }
        /* Medium Urgency */
        else if(urgencyType === 'M'){
            taskDots[i].style.backgroundColor = yellow[1];
        }
        /* High Urgency */
        else if(urgencyType === 'H'){
            taskDots[i].style.backgroundColor = red[1];
        }
    }
});

/*
Function that takes a element of any type and the style value you want returned.
Returns the value back as a string if successful otherwise will return a empty string.
*/
function getElementStyle(element, style){
    const compStyles = window.getComputedStyle(element);
    const propertyValue = compStyles.getPropertyValue(style);

    return propertyValue;
}``