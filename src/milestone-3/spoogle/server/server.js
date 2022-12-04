const express = require("express");
const cors = require("cors");
const axios = require("axios");

const BASE_URL = "http://localhost:8983/solr/articles/select";

const solr = axios.create({
  baseURL: BASE_URL,
  timeout: 10000,
});

async function searchSolr(query) {
  const response = await solr.get(BASE_URL, {
    params: {
      defType: "edismax",
      indent: true,
      "q.op": "AND",
      qf: "title^10 content^5 tags^3 sections^3",
      rows: 8,
      start: 0,
      q: query,
    },
  });

  const solrResponse = response.data.response;

  if (solrResponse) {
    return solrResponse.docs;
  }

  /*.then((response) => {
      const solrResponse = response.data.response;
      if (solrResponse) {
        const docs = solrResponse.docs;
        return docs;
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    })*/
}

const app = express();
app.use(cors());

const port = 3000;

app.get("/article/:id", (req, res) => {
  const id = req.params.id;
  const article = results.find((elem) => elem.id === id);
  res.send(article);
});

app.get("/search", async (req, res) => {
  const results = await searchSolr(req.query.q);
  res.send(results);
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
