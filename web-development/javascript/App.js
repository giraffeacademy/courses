/*
Javascript is a high-level, dynamically typed and interpreted, programming
language that was created in May of 1995 by Netscape employee Brendan Eich.

The language was famously created in only 10 days and adopted the name Javascript
as a marketing play, playing off the hugly popular Java programming language.
Although ironically the two languages are very different.

Javascript was built with the sole purpose of making websites more responsive and
dynamic. Because it's able to respond to user interactions and access and manipulate
the document object model (DOM), Javascript allows web developers to make
more dynamic websites.

In 1996 the early version of Javascript was adopted into a formal language specification
called ECMAScript, of which Javascript was the most well known implementation.
By specifying the language formally, all browsers could support languages implementing
ECMAScript. So Technically Javascript is based off the ECMAScript specification.

Today Javascript is a staple, used on just about every modern website. It's become
one of the three core web development technologies along-side HTML and CSS.

Because javascript is a core web development technology and most web developers
know it, Javascript has been stretched beyond it's original purpose. Now-a-day's
there are thousands of javascript frameworks and it's even used as a server-side
language.

Javascript utilizes a garbage collector and it's syntax is loosly based on C/C++.

Many developers choose to write Javascript using a basic text editor, generally
Javascript will be written in the same enviornment as the HTML and front end technologies
that it interacts with. In many cases javascript will be written directly inside
of an HTML file, but can also be palced in it's own separate Javascript file and
imported into HTML.
*/

// P R I N T I N G

document.write("<h1>Hello World</h1>");
document.write("<hr>");
document.write("<p>This is a javascript tutorial</p>");
// alert("This is an alert");
// console.log("Logging to the console");




// V A R I A B L E S
/*
Names are case-sensitive and may begin with:
     letters, $, _
After, may include
     letters, numbers, $, _
Convention says
     Start with a lowercase word, then additional words are capitalized
     ex. myFirstVariable
*/
var name = "Mike";                 // String w/ double quotes
var occupation = 'programmer';     // String w/ single quotes

var age = 20;                      // Integer
var gpa = 2.5;                     // Floating point number

var isTall;                        // boolean true/false
isTall = true;

name = "John";

document.write("Your name is " + name);







// C A S T I N G   &   C O N V E R T I N G

document.write( 100 + Number("25") + "<br>");
document.write( 100 + parseInt("50") + "<br>");
document.write( 100 + parseFloat("50.99") + "<br>");





// S T R I N G S

var greeting = "Hello";
//   indexes:   01234

document.write( greeting.length + "<br>" );
document.write( greeting.charAt(0) + "<br>"  );
document.write( greeting.indexOf("llo") + "<br>"  );
document.write( greeting.indexOf("z") + "<br>"  );
document.write( greeting.substring(2) + "<br>"  );
document.write( greeting.substring(1, 3) + "<br>"  );





// N U M B E R S

document.write( 2 * 3 + "<br>" );       // Basic Arithmetic: +, -, /, *
document.write( 2**3 + "<br>" );        // Exponents
document.write( 10 % 3 + "<br>" );      // Modulus Op. : returns remainder of 10/3
document.write( 1 + 2 * 3 + "<br>" );   // order of operations
document.write(10 / 3.0 + "<br><br>");      // int's and doubles


var num = 10;
num += 100;                              // +=, -=, /=, *=
document.write(num + "<br>");

num++;
document.write(num + "<br><br>");

// Math class has useful math methods
document.write( Math.pow(2, 3) + "<br>" );
document.write( Math.sqrt(144) + "<br>" );
document.write( Math.round(2.7) + "<br>" );




// U S E R   I N P U T

var name = window.prompt("Enter your name: ");
alert("Your name is " + name);




// G E T T I N G    H T M L

<h1 id="myHeader" giraffe="Giraffe Attr">Giraffe Academy</h1>

var header = document.getElementById("myHeader");
header.style="color:blue; background-color:red;"
document.write( header.getAttribute("giraffe") );
header.innerHTML = "Elephant Academy";









// A R R A Y S

// luckyNumbers = [];
luckyNumbers = [4, 8, 15, 16, "twenty", false];
//  indexes:    0  1  2   3      4        5

luckyNumbers[0] = 90;
document.write(luckyNumbers[0] + "<br>");
document.write(luckyNumbers[1] + "<br>");
document.write(luckyNumbers.length);





// N Dimensional Arrays

numberGrid = [ [1, 2], [3, 4] ];
numberGrid[0][1] = 99;

document.write(numberGrid[0][0] + "<br>");
document.write(numberGrid[0][1] + "<br>");





// A R R A Y    F U N C T I O N S

friends = new Array();
friends.push("Oscar");
friends.push("Angela");
friends.push("Kevin");

// friends.pop();
document.write( friends + "<br>" );
document.write( friends.indexOf("Angela") + "<br>" );
document.write( friends.indexOf("Z") + "<br>" );
document.write( friends.reverse() + "<br>" );
document.write( friends.sort() + "<br>" );







// Objects

var student = {
     name: "Jim",
     major: "Business",
     age: 19,
     gpa: 2.5
}
student.name = "Andy"
document.write( student.name + "<br>" );
document.write( student.major + "<br>" );
document.write( student.gpa + "<br>" );










// F U N C T I O N S

var sum = addNumbers(4, 60);
document.write(sum);

function addNumbers(num1, num2){
     return num1 + num2;
}





// Inline Event Listeners

<h1 id="myHeader" onclick="handleClick(this)">Giraffe Academy</h1>

function handleClick(element){
     alert("Clicked " + element.id);
}







// Programatic Event Listemers

<h1 id="myHeader">Giraffe Academy</h1>

var header = document.getElementById("myHeader");

header.addEventListener("click", function(){
     alert("You clicked " + header.id);
});

// https://www.w3schools.com/jsref/dom_obj_event.asp
// 'on' prefix when inline, drop 'on' when programatic









// I F    S T A T E M E N T S

var isStudent = false;
var isSmart = false;

if(isStudent && isSmart){
     document.write("You are a student");
} else if(isStudent && !isSmart){
     document.write("You are not a smart student");
} else {
     document.write("You are not a student and not smart");
}
document.write("<br>");

// >, <, >=, <=, !=, ==, String.equals()
if(1 > 3){
     document.write("number comparison was true");
}
document.write("<br>");

if("dog" != "dog"){
     document.write("string comparison was true");
}






// S W I T C H    S T A T E M E N T S

var myGrade = "A";
switch(myGrade){
     case "A":
          document.write("You Pass");
          break;
     case "F":
          document.write("You fail");
          break;
     default:
          document.write("Invalid grade");
}





// W H I L E    L O O P S

index = 1;
while(index <= 5){
     document.write(index);
     index++;
}

// do{
// 	document.write(index);
// 	index++;
// }while(index <= 5);





// F O R    L O O P S

for(var i = 0; i < 5; i++){
     document.write(i);
}

// var luckyNums = [4, 8, 15, 16, 23, 42];
// luckyNums.forEach(function(luckyNum){
//      document.write(luckyNum + "<br>");
// });






// E X C E P T I O N    C A T C H I N G

var x = y + 9;

// try{
//      // throw "Something went wrong"
//      var x = y + 9;
// }catch(err){
//      document.write(err)
// }finally{
//      // this code always gets executed
// }



/* Notes

Javascript is tricky because unlike most programming languages it doesn't
just have one interpreter, each browser is a javascript interpreter and
different browsers support different aspects of the language.

https://www.w3schools.com/js/js_versions.asp

*/

