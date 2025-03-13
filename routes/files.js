var express = require("express");
var router = express.Router();

const fs = require("fs");
const path = require("path");

const arquivosPath = path.join(__dirname, "../src/aulas");
const arquivosJsonPath = path.join(__dirname, "../src/arquivos.json");

router.use(express.static(arquivosPath));

router.get("/", (req, res) => {
  fs.readFile(arquivosJsonPath, "utf8", (err, data) => {
    if (err) {
      return res.status(500).send("Erro ao ler o arquivo JSON.");
    }
    res.send(JSON.parse(data));
  });
});

module.exports = router;
