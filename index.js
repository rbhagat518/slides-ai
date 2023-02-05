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
    pythonPath: __dirname + '/pyenv/scripts/python.exe',
    pythonOptions: [],
    scriptPath: __dirname + '/pythonScripts',
    args: []
};

// error handling python function
const pythonFunc = function (err, results) {
    if (err) 
      throw err;
    // Results is an array consisting of messages collected during execution
    console.log('results: %j', results);
};

// here you can get the value of from the textbox 
app.post('/',(req,res)=>{
    let text = req.body.theTextbox; 
    console.log(text);
    res.redirect('');

    // call the chat api to get the text file

    // -----

    // call a python script to create the JSON object
    PythonShell.run('createSlidesJSON.py', options, pythonFunc)

    // call the dalle api to get images for the slides

    // -----

    // call a second python script to create the slide show
    PythonShell.run('createPresentation.py', options, pythonFunc)
});