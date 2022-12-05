import cors from "cors";
import express from "express";

const BASE_URL = "http://localhost:8983/solr/articles/select?";

async function searchSolr(params) {
  const url = BASE_URL + new URLSearchParams(params);
  const fetchResult = await fetch(url, {
    method: "GET",
    headers: {
      "Access-Control-Allow-Methods": "GET",
      "Access-Control-Allow-Headers": "Content-Type",
      "Access-Control-Allow-Credentials": true,
    },
  })
    .then((result) => result.json())
    .then((data) => {
      return {
        docs: data.response.docs,
        numFound: data.response.numFound,
      };
    });

  return fetchResult;
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
    rows: 10,
    start: req.query.page * 10,
  };
  const results = await searchSolr(params);
  res.send(results);
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
