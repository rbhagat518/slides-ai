const express = require('express');
const app = express();
const port = 7777;

// get resouces from /public
app.use(express.static(__dirname + '/public'));

// send the index.html file to the user on the GET request
app.get('/', function (req, res){
    res.sendFile('index.html', {root: __dirname + '/public/html'})
});

// listen on the port
app.listen(port, ()=> {
    console.log(`Now listening on port ${port}`);
});