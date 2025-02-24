const express = require("express");
const app = express();
const _ = require("lodash");

app.get("/", (req, res) => {
  res.send("Hello, this is a test app!");
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
