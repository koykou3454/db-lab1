function passID(choice){
    localStorage.setItem("passID", choice);
    alert("OLDD ID: " + document.getElementById("filler").id)
    document.getElementById("filler").id = choice;
    alert("NEWIDDDEDEDEDED: " + document.getElementById(choice).id);
    write("variables.txt", "testtdog");
    alert('DIEDDED');
}

// alert("Hello World");
// alert(document.getElementById("edit").value;);
// document.getElementById("edit").value;



// console.log("Hello World");

// localStorage.getItem("passID", 3);


// write("helloworld.txt", "testtdog");
// function write(filename, content){
//     fs = require('fs');
//     fs.writeFile(filename, content, function(err,data){
//         if(err){
//             return console.log(err);
//         }
//         console.log(data);
//     });
// }


