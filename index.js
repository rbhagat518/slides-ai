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
    pythonPath: __dirname + '/python3_7_1env/scripts/python.exe',
    pythonOptions: [],
    scriptPath: __dirname + '/pythonScripts',
    args: []
};

async function runPython() {
    const { success, err = '', results } = await new Promise((resolve, reject) => {
      PythonShell.run('powerPointify.py', options, function(
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

async function runScripts(theme){
    console.log("loading...")
    await runPython();
    console.log("completed: " + theme);
}

// here you can get the value of from the textbox 
app.post('/', (req,res)=>{
    // save user theme into python args[0]
    theme = req.body.theTextbox
    options['args'].push(theme)

    // run the python script
    runScripts(theme);

    // clear POST variable and stay on the same page
    res.redirect('');
});