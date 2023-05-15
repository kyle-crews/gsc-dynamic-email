// In this example, the axios.get call fetches user data from your API, and mustache.render 
// replaces the placeholders in the template with the data from the API.

const axios = require('axios');
const mustache = require('mustache');

axios.get('https://api.yoursite.com/userdata')
    .then(response => {
        const data = response.data;
        const template = `
            <!DOCTYPE html>
            <html>
            <head>
                <title>Dynamic Email</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                    }
                    .content {
                        margin: 0 auto;
                        width: 80%;
                        padding: 20px;
                        background-color: #f0f0f0;
                        border-radius: 10px;
                    }
                </style>
            </head>
            <body>
                <div class="content">
                    <h1>Welcome, {{name}}!</h1>
                    <p>We have some exciting news for you.</p>
                    <h2>Your Latest Score: {{score}}</h2>
                    <p>Keep up the good work!</p>
                </div>
            </body>
            </html>
        `;
        const email = mustache.render(template, data);
        // send the email...
    })
    .catch(error => {
        console.error(error);
    });
