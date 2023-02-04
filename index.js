const express = require('express');
const bodyParser = require('body-parser');
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

// here you can get the value of from the textbox 
app.post('/',(req,res)=>{
    let text = req.body.theTextbox; 
    console.log(text);
    res.redirect('');
});