//throw laver en fejl
//catch redder fejlen
function f1(a,b,c){
    console.log(Math.sqrt(((a+1)/(b-1))-c));

}

function f2(a,b,c){
    try{
        if(((a+1)/(b-1))-c < 0){
            throw "Must be large than zero";
        }
        if(b-1 == 0){
            throw "Division by zero error";
        }
    }
    catch(err){
        console.log("Error: " + err + ".");
    }
    finally{
        console.log("Done")
    }
    f1(a,b,c);
}

f2(10,1,2);