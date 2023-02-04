const express = require('express');
const app = express();
const port = 7777;

// send the index.html file to the user on the GET request
app.get('/', function (req, res){
    res.sendFile('index.html', {root: __dirname})
});

// listen on the port
app.listen(port, ()=> {
    console.log(`Now listening on port ${port}`);
});