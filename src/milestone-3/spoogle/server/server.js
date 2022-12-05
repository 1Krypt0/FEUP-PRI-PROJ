const express = require("express");
const cors = require("cors");
const axios = require("axios");

const BASE_URL = "http://localhost:8983/solr/articles/select";

const solr = axios.create({
  baseURL: BASE_URL,
  timeout: 10000,
});

async function searchSolr(params) {
  const response = await solr.get(BASE_URL, {
    params: params,
  });

  const solrResponse = response.data.response;

  if (solrResponse) {
    const docs = solrResponse.docs;
    const numFound = solrResponse.numFound;
    return {
      docs,
      numFound,
    };
  }
}

const app = express();
app.use(cors());

const port = 3000;

app.get("/article/:id", async (req, res) => {
  const id = req.params.id;
  const query = `id:${id}`;
  const params = {
    "q.op": "OR",
    rows: 1,
    wt: "json",
    q: query,
  };
  const results = await searchSolr(params);
  const article = results.docs[0];
  res.send(article);
});

app.get("/search", async (req, res) => {
  const params = {
    q: req.query.q,
    "q.op": "AND",
    qf: "title^10 content^5 tags^3 sections^3 author date id",
    wt: "json",
    defType: "edismax",
    rows: 8,
    start: req.query.page * 8,
  };
  const results = await searchSolr(params);
  res.send(results);
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
