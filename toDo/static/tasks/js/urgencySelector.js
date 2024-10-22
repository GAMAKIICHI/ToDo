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
        return this.dot.checked;
    }

    //toggles radio button and changes its background color to color1 with a 1px black border
    toggle(){
        this.dot.checked = true;
        this.dot.labels[0].style.backgroundColor = this.color1;
        this.dot.labels[0].style.border = "1px solid black";
    }

    //untoggles radio button and changes its background color to color2 adn removes the border
    untoggle(){
        this.dot.checked = false;
        this.dot.labels[0].style.backgroundColor = this.color2;
        this.dot.labels[0].style.border = "none";
    }
}

document.addEventListener("DOMContentLoaded", () =>{
    const dotToggleLow = document.querySelector("#low");
    const dotToggleMed = document.querySelector("#medium");
    const dotToggleHigh = document.querySelector("#high");

    const low = new Dot(dotToggleLow, "rgba(0, 255, 0)", "rgba(170, 248, 170)");
    const med = new Dot(dotToggleMed, "rgba(255, 255, 0)", "rgba(240, 240, 80)");
    const high = new Dot(dotToggleHigh, "rgba(255, 0, 0)", "rgba(255, 100, 100)");

    /*this is so color gets applied to dot*/
    low.untoggle();
    med.untoggle();
    high.untoggle();

    dotToggleLow.addEventListener("change", () =>{
        low.toggle();
        med.untoggle();
        high.untoggle();
        
    });
    dotToggleMed.addEventListener("change", () =>{
        low.untoggle();
        med.toggle();
        high.untoggle();
    });
    dotToggleHigh.addEventListener("change", () =>{
        low.untoggle();
        med.untoggle();
        high.toggle();
    });
});

/*
Function that takes a element of any type and the style value you want returned.
Returns the value back as a string if successful otherwise will return a empty string.
*/
function getElementStyle(element, style){
    const compStyles = window.getComputedStyle(element);
    const propertyValue = compStyles.getPropertyValue(style);

    return propertyValue;
}