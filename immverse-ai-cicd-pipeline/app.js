const express = require('express');
const app = express();

const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
    res.send(`
    <h1>Immverse AI DevOps Assignment</h1>
    <h2>CI/CD Pipeline Working Successfully</h2>
    <p>Node.js Application Running in Docker</p>
    `);
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
