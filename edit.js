function passID(choice){
    localStorage.setItem("passID", choice);
    alert("OLDD ID: " + document.getElementById("filler").id)
    document.getElementById("filler").id = choice;
    alert("NEWIDDD: " + document.getElementById(choice).id);
}

