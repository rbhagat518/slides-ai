const express = require('express');
const bodyParser = require('body-parser');
const PythonShell = require('python-shell').PythonShell;
const app = express();
const port = 7777;

// get resouces from /public
app.use(express.static(__dirname + '/public'));

// for the post requests
app.use(bodyParser.urlencoded({extended:true}))

// send the index.html file to the user on the GET request
app.get('/', function (req, res){
    res.sendFile('index.html', {root: __dirname + '/public/html'})
});

// listen on the port
app.listen(port, ()=> {
    console.log(`Now listening on port ${port}`);
});

// python options
var options = {
    mode: 'text',
    pythonPath: __dirname + '/python310/scripts/python.exe',
    pythonOptions: [],
    scriptPath: __dirname + '/pythonScripts',
    args: []
};

async function runPython(filename) {
    const { success, err = '', results } = await new Promise((resolve, reject) => {
      PythonShell.run(filename, options, function(
        err,
        results
      ) {
        if (err) {
            console.log(err)
          reject({ success: false, err });
        }
        resolve({ success: true, results });
      });
    });
  };

async function runScripts(){
    options["pythonPath"] = __dirname + '/python310/scripts/python.exe'
    await runPython("textAi.py")
    console.log("text created")
    
    await runPython("createSlidesJSON.py")

    await runPython("imageAi.py")
    console.log("images created")
    
    options["pythonPath"] = __dirname + '/python36/scripts/python.exe'
    await runPython("createPresentation.py")
    console.log("done")
}

// here you can get the value of from the textbox 
app.post('/',(req,res)=>{
    let text = req.body.theTextbox; 
    console.log(text);
    res.redirect('');
    runScripts();
});